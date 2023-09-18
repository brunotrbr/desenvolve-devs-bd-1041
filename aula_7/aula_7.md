# Manipulando banco de dados

## Merge de duas tabelas

Podemos mergear duas tabelas diferentes em uma só, adicionando e/ou atualizando os dados de uma delas. É um comando útil quando temos tabelas duplicadas e queremos eliminar uma delas.

```sql
-- cria tabelas
CREATE TABLE customer_account (
	id INTEGER PRIMARY KEY,
	amount INTEGER
);

CREATE TABLE customer_account_old_db (
	id INTEGER PRIMARY KEY,
	amount INTEGER
);

-- insere valores
INSERT INTO customer_account VALUES(1, 1000);
INSERT INTO customer_account VALUES(2, 3000);
INSERT INTO customer_account VALUES(3, 5000);

INSERT INTO customer_account_old_db VALUES(1, 10);
INSERT INTO customer_account_old_db VALUES(2, 30);
INSERT INTO customer_account_old_db VALUES(3, 50);
INSERT INTO customer_account_old_db VALUES(4, 100);

-- merge das tabelas na customer_account
MERGE INTO customer_account ca -- ca é um alias para a tabela
USING customer_account_old_db caodb 
-- O comando USING acima pode ser substituida por "USING (SELECT id, amount FROM customer_account_old_db) AS caodb", sem as aspas
ON ca.id = caodb.id
-- se achar o id
WHEN MATCHED THEN
-- atualiza o campo amount
  UPDATE SET amount = ca.amount + caodb.amount
-- se não achar
WHEN NOT MATCHED THEN
-- insere na tabela
  INSERT (id, amount) VALUES (caodb.id, caodb.amount);

-- analisar campos da tabela customer_account
SELECT * FROM customer_account
```

&nbsp;

## Sub-consultas

Com PostgreSQL nós temos dois tipos de subconsultas. Uma delas utilzando a cláusula **WITH**, e a outra usando **SELECT**.

Subconsultas são consultas aninhadas (ou pré-consultas) em conjunto com outros comandos, como SELECT, INSERT, UPDATE, DELETE. É possível ainda encadear subconsultas, colocando uma dentro da outra.

Podem retornar
- Um único valor
- Um conjunto de valores

&nbsp;

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

Como retorna um conjunto de valores, os operadores relacionais tradicionais não podem ser utilizados.

Utilizamos os seguintes operadores

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

#### Cláusula WITH

A cláusula WITH permite que a gente especifique uma ou mais sub-consultas que podem ser referenciadas pelo nome na consulta principal.

A sub-consulta funciona como uma tabela temporária ou view durante a execução da consulta principal. Além disso, cada sub-consulta pode ser um SELECT, INSERT, UPDATE ou DELETE.

&nbsp;

Na consulta abaixo, buscamos os produtos mais vendidos somando as quantidades de cada um deles, e queremos somente os que tiverem vendido mais de 350 unidades ao total.

Depois, selecionamos o nome do produto, o preço e a quantidade total, realizando um JOIN com a sub-consulta de mais vendidos para buscar a quantidade, e ordenamos pela quantidade total

```sql
WITH high_selling_products AS (
  SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items where order_id > 50
  GROUP BY product_id
  HAVING SUM(quantity) > 350
) -- para fazer uma nov sub-consulta, inclua a vírgula, o novo nome da subconsulta e o select
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

## Funções agregadoras

Agrupar valores para gerar resumos ou relatórios com os dados.

Utilizamos funções agregadoras. São chamadas assim porque realizam cálculos em um grupo de linhas de uma determinada coluna (definida na cláusula GROUP BY) e retornam um único valor para aquele conjunto. 

Para filtrar valores agregados, utilizamos a cláusula HAVING, ao invés da cláusula WHERE. O WHERE realiza os filtros **antes** de serem realizados os agrupamentos, e o HAVING **após** os dados terem sido agrupados.

```sql
SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING SUM(quantity) > 350

"product_id"	"total_quantity"
248	          351
410	          355

SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items where product_id = 249
  GROUP BY product_id
  HAVING SUM(quantity) > 350
"product_id"	"total_quantity"



SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING product_id = 249

"product_id"	"total_quantity"
249	          209


SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING SUM(quantity) > 350

"product_id"	"total_quantity"
248	          351
410	          355

SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items where product_id = 410
  GROUP BY product_id
  HAVING SUM(quantity) > 350
"product_id"	"total_quantity"
410	          355



SELECT product_id, SUM(quantity) AS total_quantity
  FROM order_items
  GROUP BY product_id
  HAVING product_id = 410

"product_id"	"total_quantity"
410	          355
```

&nbsp;

São exemplos de funções agregadoras: 

> MAX, MIN, AVG, SUM e COUNT

&nbsp;

OBS: Caso informe alguma coluna não agregada na consulta, por exemplo o nome de um produto ao tentar localizar o maior preço, essa coluna precisa ser inclusa na cláusula GROUP BY.

&nbsp;

```sql
-- MAX pode ser usado para saber o produto com maior preço no sistema
select MAX(price) AS max_price from products
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
-- aplicar limit para trazer o top 10
-- limit 10


-- COUNT é usado para contar a quantidade de alguma coisa.
-- Contar a quantidade de registros na tabela
SELECT COUNT(1) FROM customers

-- Contar a quantidade de produtos para cada uma das categorias de produtos
SELECT categories.category_name, COUNT(DISTINCT products.product_name) AS product_count
FROM categories
LEFT JOIN products ON categories.category_id = products.category_id
GROUP BY categories.category_id;

-- Contar a quantidade de pedidos para cada data na tabela de pedidos
SELECT order_date, COUNT(*) AS order_count
FROM orders
GROUP BY order_date
ORDER BY order_date asc
```

## Joins

Buscar dados relacionados em outras tabelas. Esse é um dos principais motivos de se usar um banco relacional, para que se tenham dados relacionados e seja simples de buscar estas relações.

São exemplos de joins:

> CROSS JOIN, INNER JOIN, RIGHT JOIN, LEFT JOIN, FULL JOIN e SELF JOIN

&nbsp;

### Cross Join
Gera todas as combinações possíveis para cada uma das linhas das tabelas relacionadas

<img src=./imagens/cross_join.png width=500>

```sql
SELECT * FROM categories
CROSS JOIN products
limit 100;
```

&nbsp;

### Inner Join
Gera as combinações em que a cláusula ON do join seja verdadeira, ou seja que os customer_ids, sejam iguais no exemplo abaixo

```sql
SELECT o.*, cs.first_name, cs.email FROM orders o
INNER JOIN customers cs ON o.customer_id = cs.customer_id
LIMIT 100;
```

&nbsp;

### Left Join
Gera as combinações em que a cláusula ON do join seja verdadeira. Caso a tabela do lado esquerdo (a primeira) não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor zerado

```sql
SELECT categories.category_name, COUNT(DISTINCT products.product_name) AS product_count
FROM categories
LEFT JOIN products ON categories.category_id = products.category_id
GROUP BY categories.category_id;
```

&nbsp;

### Right Join
Gera as combinações em que a cláusula ON do join seja verdadeira. Caso a tabela do lado direito (a segunda) não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor zerado

```sql
SELECT categories.category_name, COUNT(DISTINCT products.product_id) AS product_count
FROM categories
RIGHT JOIN products ON categories.category_id = products.category_id
GROUP BY categories.category_id;
-- Exemplo invertendo as tabelas
SELECT categories.category_name, COUNT(DISTINCT products.product_id) AS product_count
FROM products
RIGHT JOIN categories ON categories.category_id = products.category_id
GROUP BY categories.category_id;
```

&nbsp;


### Full Join
Gera as combinações em que a cláusula ON do join seja verdadeira. Caso alguma não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor null

```sql
SELECT categories.category_name, products.product_id
FROM categories
FULL JOIN products ON categories.category_id = products.category_id
ORDER BY products.product_id nulls first
```

&nbsp;

### Self Join

É usado para fazer join entre a mesma tabela, mas usando aliases diferentes. Não existe a palavra reservada SELF JOIN, portanto podemos usar o INNER JOIN com alias diferentes.

```sql
CREATE TABLE employee (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR (255) NOT NULL,
	last_name VARCHAR (255) NOT NULL,
	manager_id INT,
	FOREIGN KEY (manager_id) 
	REFERENCES employee (employee_id) 
	ON DELETE CASCADE
);
INSERT INTO employee (
	employee_id,
	first_name,
	last_name,
	manager_id
)
VALUES
	(1, 'Windy', 'Hays', NULL),
	(2, 'Ava', 'Christensen', 1),
	(3, 'Hassan', 'Conner', 1),
	(4, 'Anna', 'Reeves', 2),
	(5, 'Sau', 'Norman', 2),
	(6, 'Kelsie', 'Hays', 3),
	(7, 'Tory', 'Goff', 3),
	(8, 'Salley', 'Lester', 3);
SELECT * FROM employee AS e1
INNER JOIN employee AS e2
ON e1.manager_id = e2.employee_id;
```

&nbsp;

Abaixo podemos ver uma imagem resumindo os Joins

<img src=./imagens/sql_joins.png width=700>

&nbsp;

## Union e Union ALL

Algumas vezes, temos 2 tabelas distintas e queremos juntas elas em uma só, para uma determinada consulta. Nesse caso, podemos usar as cláusulas UNION e UNION ALL para juntar as linhas e juntar as linhas incluindo valores repetidos, respectivamente.

```sql
-- Create table1
CREATE TABLE table1 (
  id INTEGER,
  name VARCHAR(50)
);

-- Insert data into table1
INSERT INTO table1 (id, name) VALUES (1, 'Alice');
INSERT INTO table1 (id, name) VALUES (2, 'Bob');
INSERT INTO table1 (id, name) VALUES (3, 'Charlie');

-- Create table2
CREATE TABLE table2 (
  id INTEGER,
  name VARCHAR(50)
);

-- Insert data into table2
INSERT INTO table2 (id, name) VALUES (4, 'David');
INSERT INTO table2 (id, name) VALUES (5, 'Emily');
INSERT INTO table2 (id, name) VALUES (6, 'Frank');
INSERT INTO table2 (id, name) VALUES (2, 'Bob');

-- Union, sem o bob da table2
SELECT * FROM table1
UNION
SELECT * FROM table2;

-- Union2, com o bob da table2
SELECT * FROM table1
UNION ALL
SELECT * FROM table2;
```

Caso uma tabela tenha mais colunas que outra, precisamos "completar" a que tem colunas a menos com "null"

```sql
-- Create table3
CREATE TABLE table3 (
  id INTEGER,
  name VARCHAR(50),
  age INTEGER
);

-- Insert data into table3
INSERT INTO table3 (id, name, age) VALUES (4, 'David', 30);
INSERT INTO table3 (id, name, age) VALUES (5, 'Emily', 25);
INSERT INTO table3 (id, name, age) VALUES (6, 'Frank', 19);
INSERT INTO table3 (id, name, age) VALUES (2, 'Bob', 41);

-- select completando as colunas
SELECT id, name, NULL FROM table2
UNION ALL
SELECT id, name, age FROM table3;
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

&nbsp;


Usado quando:
- Queremos copiar dados de uma tabela para outra
- Queremos filtrar e transformar dados, antes de inserir eles
- Queremos mergear múltiplas tabelas em uma só, gerando um resumo dos dados ou outro conjunto de dados.