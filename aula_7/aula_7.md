# Manipulando banco de dados

## Funções agregadoras

Com uma certa frequência, queremos agrupar valores para gerar resumos ou relatórios com os dados.

Nestes casos, utilizamos o que chamamos de funções agregadoras. Elas são chamadas assim porque realizam cálculos em um grupo de linhas de uma determinada coluna (definida na cláusula GROUP BY) e retornam um único valor para aquele conjunto. 

Para filtrar valores agregados, utilizamos a cláusula HAVING, ao invés da cláusula WHERE. O WHERE realiza os filtros **antes** de serem realizados os agrupamentos, e o HAVING **após** os dados terem sido agrupados.

```sql
-- quero buscar todos os produtos cuja soma nos pedidos seja superior a 350 (vendeu mais de 350 unidades)
SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING SUM(quantity) > 350


-- quero buscar todos os produtos cuja soma nos pedidos seja superior a 350 e o id do produto seja 249
SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items where product_id = 249
  GROUP BY product_id
  HAVING SUM(quantity) > 350


SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING product_id = 249
```

&nbsp;

São exemplos de funções agregadoras: 

> MAX, MIN, AVG, SUM e COUNT

&nbsp;

OBS: Caso informe alguma coluna não agregada na consulta, por exemplo o nome de um produto ao tentar localizar o maior preço, essa coluna precisa ser inclusa na cláusula GROUP BY.

&nbsp;

```sql
-- MAX pode ser usado para saber o produto com maior preço no sistema
select MAX(price) AS max_price from products order by max_price desc

-- caso informe alguma coluna não agregada na consulta, por exemplo o nome de um produto ao tentar localizar o maior preço, essa coluna precisa ser inclusa na cláusula GROUP BY.
select product_name, MAX(price) AS max_price from products GROUP BY product_name order by max_price desc


-- MIN pode ser usado para saber o produto com menor preço no sistema
select MIN(price) AS min_price from products order by min_price desc
-- caso informe alguma coluna não agregada na consulta, por exemplo o nome de um produto ao tentar localizar o maior preço, essa coluna precisa ser inclusa na cláusula GROUP BY.
select product_name, MIN(price) AS min_price from products GROUP BY product_name order by min_price asc


-- AVG pode ser usado para calcular a média. Neste caso, a média de vendas de agosto de 2017. E arredondamos o valor para 2 casas decimais.
SELECT ROUND(AVG(total_amount), 2) AS avg_sell_2017_08 from orders where order_date BETWEEN '2017-08-01' and '2017-08-31'  


-- SUM pode ser usado para calcular a soma. Neste caso, a soma de vendas de agosto de 2017. E arredondamos o valor para 2 casas decimais.
SELECT ROUND(SUM(total_amount), 2) AS sum_sell_2017_08 from orders where order_date BETWEEN '2017-08-01' and '2017-08-31'

-- Ou podemos calcular a soma de cada um dos produtos vendidos
select pr.product_id, pr.product_name, sum(oi.quantity) AS sum_qty_prod_sell 
from order_items oi
inner join products pr on pr.product_id = oi.product_id
group by pr.product_id, pr.product_name
-- aqui podemos aplicar having para filtrar, por exemplo, só os que tiveram venda acima de 150 unidades
-- HAVING SUM(oi.quantity) > 150
order by sum_qty_prod_sell desc


-- COUNT é usado para contar a quantidade de alguma coisa.
-- Contar a quantidade de registros na tabela
SELECT COUNT(1) FROM customers

-- Contar a quantidade de produtos para cada uma das categorias de produtos
SELECT categories.category_name, COUNT(DISTINCT products.product_id) AS product_count
FROM categories
LEFT JOIN products ON categories.category_id = products.category_id
GROUP BY categories.category_id;

-- Contar a quantidade de pedidos para cada data na tabela de pedidos
SELECT order_date, COUNT(*) AS order_count
FROM orders
GROUP BY order_date
ORDER BY order_date asc
```

&nbsp;

## Sub-consultas

Com PostgreSQL nós temos dois tipos de subconsultas. Uma delas utilzando a cláusula **WITH**, e a outra usando **SELECT**.

Subconsultas são consultas aninhadas (ou pré-consultas) em conjunto com outros comandos, como SELECT, INSERT, UPDATE, DELETE. É possível ainda encadear subconsultas, colocando uma dentro da outra.

Podem retornar
- Um único valor
- Um conjunto de valores

### Sub-consultas que retornam um único valor
Vamos supor que queremos saber quais são os produtos que possuem o preço maior que o produto de ID 3.

```sql
select price from products where product_id = 3
select product_id, product_name, price from products where price > 1457.22
```

&nbsp;

Precisamos de duas consultas. Neste caso, podemos substituir por uma só utilizando sub-consultas
```sql
select product_id, product_name, price from products 
where price > (select price from products where product_id = 3);
```

&nbsp;

Podemos usar todos os operadores relacionais típicos nestas sub-consultas

> \>, >=, <, <=, =, <>

&nbsp;

### Sub-consultas que retornam um conjunto de valores

A ideia neste caso é a mesma, recuperar dados usando subconsultas. Contudo, como retorna um conjunto de valores, os operadores relacionais tradicionais não podem ser utilizados. Neste caso, utilizamos os seguintes operadores

> (NOT) IN, SOME/ANY, ALL e EXISTS

&nbsp;

#### Operador IN

Utilizamos o IN, ou NOT IN para negação, para obter as linhas iguais a **qualquer linha** da subconsulta.

```sql
-- buscamos todos os pedidos de clientes que residam em Abruzzi, ordenados pelo número do pedido
select * from orders 
where customer_id IN (SELECT customer_id from customers where state = 'Abruzzi') 
order by order_id, customer_id asc

-- buscamos todos os pedidos de clientes que tenham o id igual a 20, 21 ou 42, ordenados pelo número do pedido 
select * from orders 
where customer_id IN (20,21,42)
order by order_id, customer_id asc
```

```sql
-- buscamos todos os pedidos de clientes que residam em Abruzzi, ordenados pelo número do pedido
select * from orders 
where customer_id NOT IN (SELECT customer_id from customers where state = 'Abruzzi') 
order by order_id, customer_id asc

-- Para conferência
SELECT COUNT(*) FROM orders
```

&nbsp;

#### Operador SOME/ANY

Utilizamos o SOME/ANY para comparar a linha com **cada uma das linhas** da sub-consulta. Precisamos usar os operadores relacionais tradicionais nesta sub-consulta

Some e any são sinônimos.

&nbsp;

> = ANY -> igual ao IN
> 
> \> ANY -> maior que o menor valor da lista
> 
> < ANY -> menor que o maior valor da lista

&nbsp;

```sql
-- listar os dados (order_id, product_name, quantity e price) dos pedidos cujo valor total seja superior a 220.000,00
select oi.order_id, pr.product_name, oi.quantity, oi.price 
from order_items oi 
inner join products pr on pr.product_id = oi.product_id where oi.order_id = ANY
(select order_id from orders where total_amount > 220000)
order by oi.order_id asc
```

```sql
-- listar os dados (order_id, product_name, quantity e price) dos pedidos cujo id do pedido seja maior que o menor id do pedidos com valor superior a 220.000,00
select oi.order_id, pr.product_name, oi.quantity, oi.price 
from order_items oi 
inner join products pr on pr.product_id = oi.product_id where oi.order_id > ANY
(select order_id from orders where total_amount > 220000)
order by oi.order_id asc
```

```sql
-- listar os dados (order_id, product_name, quantity e price) dos pedidos cujo id do pedido seja menor que o maior id do pedidos com valor superior a 220.000,00 
select oi.order_id, pr.product_name, oi.quantity, oi.price 
from order_items oi 
inner join products pr on pr.product_id = oi.product_id where oi.order_id < ANY
(select order_id from orders where total_amount > 220000)
order by oi.order_id asc
```

&nbsp;

#### Operador ALL

Utilizamos o ALL para comparar a linha com **todas as linhas** da sub-consulta. Precisamos usar os operadores relacionais tradicionais nesta sub-consulta

> = ALL -> precisa dar match com todos os resultados da lista
> 
> \> ALL -> maior que o maior valor da lista
> 
> < ALL -> menor que o menor valor da lista

&nbsp;

```sql
-- Listar todos os pedidos (order_id, customer_id e total_amount) do primeiro cliente encontrado no sistema que resida em Caen ou Saint-Lô
select order_id, customer_id, total_amount from orders where customer_id = ALL (select customer_id from customers where city in ('Caen','Saint-Lô') limit 1);

-- Se remover o limit retorna uma lista de customer_ids, e nenhum cliente pode possuir mais de um customer_id.
select order_id, customer_id, total_amount from orders where customer_id = ALL (select customer_id from customers where city in ('Caen','Saint-Lô'));

-- Listar todos os pedidos (order_id, customer_id e total_amount) do cliente que tem o ID maior que o do primeiro cliente encontrado no sistema que resida em Caen ou Saint-Lô
select order_id, customer_id, total_amount from orders where customer_id > ALL (select customer_id from customers where city in ('Caen','Saint-Lô') limit 1);
-- Tirar o limit, e vai achar todos maiores que o último

-- Listar todos os pedidos (order_id, customer_id e total_amount) do cliente que tem o ID menor que o do primeiro cliente encontrado no sistema que resida em Caen ou Saint-Lô
select order_id, customer_id, total_amount from orders where customer_id < ALL (select customer_id from customers where city in ('Caen','Saint-Lô') limit 1);
-- Tirar o limit, e vai achar todos menores que o primeiro
```
&nbsp;

#### Operador EXISTS

O operador EXISTS é o que chamamos de consulta correlacionada.

Uma consulta é dita correlacionada quando ambas as consultas (interna e externa) são interdependentes. Em outras palavras, para cada linha processada da consulta externa, deve-se processar novamente a consulta interna. A consulta interna depende da consulta externa para ser processada.

Essa construção retorna verdadeiro se a subconsulta possuir **pelo menos** uma linha.

```sql
-- Listar todos os clientes que tiverem realizado pelo menos uma compra em agosto de 2017
-- O select 1 (ou qualquer outro valor constante) não retorna as linhas da tabela de pedidos. Apenas retorna a informação de que existem linhas que batem com o período de datas selecionadas.
-- O where da sub-consulta verifica se o customer_id da tabela customer é igual ao customer_id da tabela de pedidos, e dai analiza o período de tempo definido na sub-consulta
-- Por fim, o select da tabela de customers vai buscar as colunas dos clientes que tiverem pelo menos uma linha na sub-consulta
select * from customers cs
where EXISTS (select 1 from orders o where o.customer_id = cs.customer_id and o.order_date between '2017-08-01' and '2017-08-31') order by customer_id asc;

-- O select abaixo é para caso queira comparar os valores das duas consultas
select customer_id from orders o where o.order_date between '2017-08-01' and '2017-08-31' order by customer_id asc
```

&nbsp;

#### Operador WITH

A cláusula WITH permite que a gente especifique uma ou mais sub-consultas que podem ser referenciadas pelo nome na consulta principal.

A sub-consulta funciona como uma tabela temporária ou view durante a execução da consulta principal. Além disso, cada sub-consulta pode ser um SELECT, INSERT, UPDATE ou DELETE.

&nbsp;

Na consulta abaixo, buscamos os produtos mais vendidos somando as quantidades de cada um deles, e queremos somente os que tiverem vendido mais de 350 unidades ao total.

Depois, selecionamos o nome do produto, o preço e a quantidade total, realizando um JOIN com a sub-consulta de mais vendidos para buscar a quantidade, e ordenamos pela quantidade total

```sql
WITH high_selling_products AS (
  SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING SUM(quantity) > 350
)  -- para fazer uma nov sub-consulta, inclua a vírgula, o novo nome da subconsulta e o select
-- , lower_selling_products AS (
--   SELECT product_id, SUM(quantity) AS total_quantity
--   FROM order_items
--   GROUP BY product_id
--   HAVING SUM(quantity) < 50
-- )
SELECT product_name, price, total_quantity
FROM products
JOIN high_selling_products ON products.product_id = high_selling_products.product_id
ORDER BY total_quantity DESC;
```
&nbsp;

## Union e Union ALL

Algumas vezes, temos 2 tabelas distintas e queremos juntas elas em uma só, para uma determinada consulta. Nesse caso, podemos usar as cláusulas UNION e UNION ALL para juntar as linhas e juntar as linhas incluindo valores repetidos, respectivamente.

```sql
-- Create tabela_um
CREATE TABLE tabela_um (
  id INTEGER,
  name VARCHAR(50)
);

-- Insert data into tabela_um
INSERT INTO tabela_um (id, name) VALUES (1, 'Alice');
INSERT INTO tabela_um (id, name) VALUES (2, 'Bob');
INSERT INTO tabela_um (id, name) VALUES (3, 'Charlie');

-- Create tabela_dois
CREATE TABLE tabela_dois (
  id INTEGER,
  name VARCHAR(50)
);

-- Insert data into tabela_dois
INSERT INTO tabela_dois (id, name) VALUES (4, 'David');
INSERT INTO tabela_dois (id, name) VALUES (5, 'Emily');
INSERT INTO tabela_dois (id, name) VALUES (6, 'Frank');
INSERT INTO tabela_dois (id, name) VALUES (2, 'Bob');

-- Union, sem o bob da tabela_dois
SELECT * FROM tabela_um
UNION
SELECT * FROM tabela_dois;

-- Union2, com o bob da tabela_dois
SELECT * FROM tabela_um
UNION ALL
SELECT * FROM tabela_dois;
```

Caso uma tabela tenha mais colunas que outra, precisamos "completar" a que tem colunas a menos com "null"

```sql
-- Create tabela_tres
CREATE TABLE tabela_tres (
  id INTEGER,
  name VARCHAR(50),
  age INTEGER
);

-- Insert data into tabela_tres
INSERT INTO tabela_tres (id, name, age) VALUES (4, 'David', 30);
INSERT INTO tabela_tres (id, name, age) VALUES (5, 'Emily', 25);
INSERT INTO tabela_tres (id, name, age) VALUES (6, 'Frank', 19);
INSERT INTO tabela_tres (id, name, age) VALUES (2, 'Bob', 41);

-- select completando as colunas
SELECT id, name, NULL FROM tabela_dois
UNION ALL
SELECT id, name, age FROM tabela_tres;
```

## Insert into select

Quando vimos o insert, utilizamos somente o comando INSERT INTO VALUES. Contudo, o PostgreSQL possui também um segundo insert, que é o INSERT INTO SELECT

```sql
CREATE TABLE public.tabela_um
(
    id integer,
    nome character varying(10),
    PRIMARY KEY (id)
);

CREATE TABLE public.tabela_dois
(
    id integer,
    nome character varying(10),
    PRIMARY KEY (id)
);

INSERT INTO tabela_um VALUES(1,'um');
INSERT INTO tabela_um VALUES(2,'dois');
INSERT INTO tabela_um VALUES(3,'tres');

-- Inserir dados a partir de um select
INSERT INTO tabela_dois SELECT id, nome FROM tabela_um WHERE id = 2
```

Usado quando:
- Queremos copiar dados de uma tabela para outra
- Queremos filtrar e transformar dados, antes de inserir eles
- Queremos mergear múltiplas tabelas em uma só, gerando um resumo dos dados ou outro conjunto de dados.


## Exercícios

## Exercício 1
Encontre o número total de pedidos realizados por clientes que compraram o produto 957
```sql

```

## Exercício 2
Exiba o nome completo e o valor total dos pedidos feitos por cada cliente, formatado como dinheiro. Ordene em ordem alfabética.
```sql

```

## Exercício 3
Encontre e exiba todas as informações dos produtos e do fornecedor cujo id do fornecedor seja o número 9
```sql

```

## Exercício 4
Encontre e exiba o nome do produto e a quantidade de produtos comprados por cada cliente cujo nome inicie por "AN", ordenado pelo sobrenome. Informe o nome completo do cliente. Desconsidere letras maiúsculas ou minúsculas ao procurar o cliente.
```sql

```

## Exercício 5
Exiba o total gasto por cada cliente que gastou mais de 1000000 em pedidos. Informe o nome completo do cliente, e os valores formatados como dinheiro, ordenados por valor decrescente.
```sql

```

## Exercício 6
Encontre e informe o nome e a quantidade de pedidos dos 5 produtos mais comprados, ordenados por quantidade decrescente
```sql

```

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.