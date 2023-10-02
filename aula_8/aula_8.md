# Manipulando banco de dados

OBS: Os valores de order_id e product_id abaixo vão variar de acordo com a inserção dos dados. Buscar dados atualizados nos inserts realizados para estudar os exemplos.

## Plano de execução

O plano de execução se refere a uma série de passos que o motor (engine) do banco de dados adota para recuperar os registros, dada uma determinada consulta. Ele determina quais indexes ou tabelas serão acessados, qual algoritmo de join será usado e a ordem em que as operações serão realizadas para executar a consulta.

Ele é gerado pelo planejador de consultas (um subsistema do SGBD), que analisa a consulta e gera o plano otimizado para aquela consulta específica.

Podemos visualizar o plano de execução clicando no botão **explain** no PGAdmin ou adicionando a cláusula **EXPLAIN** no início da consulta.

```sql
EXPLAIN SELECT * FROM orders WHERE order_date = '2017-08-011';

EXPLAIN SELECT * FROM order_items FROM order_id = 1 AND product_id = 1
```

Ao utilizar o EXPLAIN, conseguimos observar o plano de execução para a consulta, contendo informações sobre cada passo do plano, incluindo a ordem em que as operações serão realizadas, o custo estimado de cada operação e o número de linhas que serão retornados a cada passo.

Podemos utilizar o plano de execução para entender como a consulta será realizada, e identificar operações que são particularmente caras para o BD, como full table scans ou determinados joins por exemplo.

A partir dessa análise (considerando os exemplos acima), podemos criar indices para melhorar a performance ou reestruturar a tabela, visando reduzir o número de joins.

Reparem que para cada uma das consultas acima, ocorreu um plano de execução diferente:

&nbsp;

Na consulta 1, foi realizado o que chamamos de **scan sequencial** na tabela de pedidos, enquanto na consulta 2 foi realizado o chamado **Index Scan**.

&nbsp;

### Scan

#### Sequential Scan

O SGBD percorre todo o disco onde os dados estão armazenados, em busca das linhas da tabela.

Na imagem abaixo:
<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-8/conteudo/b_plus_tree.png width=500>

&nbsp;

Ao procurar pelo registro 0007, o SGBD vai iniciar no registro 0001 e percorrer todos até chegar no 0007.

```sql
-- Exemplo
EXPLAIN SELECT * FROM orders WHERE order_date = '2017-08-011';
```

&nbsp;

#### Index Scan
O SGBD percorre exatamente os indices que precisa até localizar as linhas que devem ser retornadas. Ao identificar, percorre as tabelas para buscar todos os dados.

Na imagem abaixo:
<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-8/conteudo/b_plus_tree.png width=500>

&nbsp;

Ao procurar pelo registro 0007, o SGBD vai percorrer 0005 > 0007 > 0008/0009 > 0007

```sql
-- Exemplo
EXPLAIN SELECT * FROM order_items WHERE order_id = 1 AND product_id = 1
```

&nbsp;

#### Index Only Scan
Semelhante ao index scan, mas sem necessidade de acesso às tabelas do banco de dados pois o índice possui acesso a todas as colunas necessárias para realizar a consulta.

```sql
-- Index only scan
SELECT order_id from orders where order_id = 1

-- Index scan
SELECT * from orders where order_id = 1
```

&nbsp;

#### Bitmap Index Scan / Bitmap Heap Scan / Recheck Cond
É como um meio termo entre um scan sequencial e um index scan. Semelhante ao index scan ele busca os índices para determinar exatamente quais dados são necessários, mas realiza a leitura de uma grande quantidade de itens como o scan sequencial.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-8/conteudo/bitmap_scan.png width=400>

&nbsp;

Normalmente ocorre quando a consulta é pequena demais para um sequential scan mas grande demais para um index scan.

```sql
-- Exemplo
SELECT * FROM orders WHERE order_id BETWEEN 1000 AND 2000

--Obs: Podem modificar o range de dados do order_id para ver qual scan está sendo realizado
```

&nbsp;

### Joins

Normalmente, operações **joins** processam somente duas tabelas por vez. Caso a consulta tenha mais do que dois **joins**, elas são executadas sequencialmente: primeiro duas tabelas, depois o resultado intermediário (tabela intermediária) com a próxima tabela, e assim vai até acabar as tabelas.

&nbsp;

Podem ser de 3 tipos:
- Nested Loops
- Hash Join / Hash
- Merge Join

> Obs: Não temos o controle de qual tipo de join vai ser realizado. Ele é escolhido automaticamente pelo SGBD de acordo com a consulta realizada.

&nbsp;

#### Nested Loops
Realiza o **Join** de duas tabelas obtendo as linhas da tabela um e percorrendo a tabela dois linha por linha, realizando o match entre elas.

&nbsp;

Exemplo de consultas que realizam nested loops:
```sql
-- nested loop com 2 tabelas
SELECT * FROM order_items oi 
INNER JOIN products pr on oi.product_id = pr.product_id
INNER JOIN orders od on oi.order_id = od.order_id
WHERE oi.order_id in (1,2,3) and oi.product_id in (1,2,3)

-- nested loop com 3 tabelas
SELECT * FROM order_items oi 
INNER JOIN products pr ON oi.product_id = pr.product_id
INNER JOIN orders od ON oi.order_id = od.order_id
INNER JOIN customers cs ON cs.customer_id = od.customer_id
WHERE oi.order_id IN (1,2,3) AND oi.product_id IN (1,2,3)
```

&nbsp;

#### Hash Join / Hash
O hash join carrega os registros candidatos da tabela A em um *hash table* (marcado com Hash no plano de execução). Para cada linha da tabela B, a tabela de Hash é checada buscando o match entre os registros.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-8/conteudo/hash_table.png width=400 style="background:white">

&nbsp;

Exemplo de consulta que realiza hash join:
```sql
SELECT o.order_id, oi.product_id, oi.quantity, oi.price, p.product_name
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
```

#### Merge Join
Combina duas tabelas. Como pré-requisito, elas precisam estar previamente ordenadas (passo realizado pelo SGBD).

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-8/conteudo/merge_join.gif width=400>

&nbsp;

Exemplo de consulta que realiza merge join:
```sql
-- merge join
SELECT * FROM order_items oi 
INNER JOIN products pr on oi.product_id = pr.product_id
WHERE oi.order_id in (1,2,3) and oi.product_id in (1,2,3)
```

&nbsp;

### Sorting and Grouping

#### Sort / Sort Key
Ordena o conjunto de colunas especificados na cláusula **order by**. A operação de sort necessidade de uma grande quantidade de memória para materializar o resultado intermediário.

&nbsp;

#### GroupAggregate
Agrega um conjunto pré-ordernado de acordo com a cláusula **group by**

&nbsp;

#### HashAggregate
Usa uma tabela de hash temporária para agrupar os registros.

&nbsp;

Exemplos de consultas que realizam sorting and grouping:
```sql
SELECT customer_id, cast(SUM(total_amount) as money) as total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 1000000
order by SUM(total_amount) desc

SELECT *
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc
```

&nbsp;

## Index

O index, ou índice, é um recurso utilizado pelos SGBDs para conseguir localizar mais rapidamente os dados inseridos no banco de dados.

Ele funciona como um apontamento direto para onde o registro está salvo, de forma que a consulta pode ser realizada mais rapidamente.

&nbsp;

Observem esse exemplo. Vamos criar uma tabela que armazena um id serial e uma data, e depois vamos inserir 400.000.000 de registros, sendo 100.000.000 para cada data em 22/04/2023, 22/03/2023, 22/02/2022 e 22/01/2022

&nbsp;

```sql
CREATE TABLE teste_index (
	id serial primary key,
	teste_date date
)

DO $$
DECLARE
  i integer;
BEGIN
  FOR i IN 1..100000000 LOOP
    INSERT INTO teste_index(teste_date) VALUES ('2023-04-22');
  END LOOP;
  FOR i IN 1..100000000 LOOP
    INSERT INTO teste_index(teste_date) VALUES ('2023-03-22');
  END LOOP;
  FOR i IN 1..100000000 LOOP
    INSERT INTO teste_index(teste_date) VALUES ('2023-02-22');
  END LOOP;
  FOR i IN 1..100000000 LOOP
    INSERT INTO teste_index(teste_date) VALUES ('2023-01-22');
  END LOOP;
END $$;
-- Query returned successfully in 1 hr 30 min.
-- Se dividir em 4 inserts diferentes, rodando simultaneamente, cada um levou +- 40 minutos.

-- Conferência de valores
SELECT COUNT(1) FROM teste_index

SELECT DISTINCT(teste_date), COUNT(teste_date) FROM teste_index GROUP BY teste_date
```

&nbsp;

Agora vamos comparar a busca com e sem index

```sql
-- Busca sem índice, fazendo sequence scan
SELECT teste_date FROM teste_index WHERE teste_date = '2023-03-22'
-- Total rows: 1000 of 100000000
-- Query complete 00:02:17.676

-- Criamos o índice
CREATE INDEX teste_date
    ON public.teste_index USING btree
    (teste_date ASC NULLS LAST)
;
-- Query complete 00:08:36.813

-- Repetimos a busca, agora com index scan only
SELECT teste_date FROM teste_index WHERE teste_date = '2023-03-22'
-- Total rows: 1000 of 100000000
-- Query complete 00:00:32.498


-- E com sequence scan
SELECT * FROM teste_index WHERE teste_date = '2023-04-22'
-- Total rows: 1000 of 100000000
-- Query complete 00:02:37.190
```

&nbsp;

## Views e Materialized Views

### Views

Em PostgreSQL, uma **view** é uma tabela virtual que não armazena nenhum dado ou informação, e sim uma "visão" para dados armazenados em outras tabelas. Essencialmente, uma view é uma consulta SQL que é armazenada em um banco de dados e pode ser usada como uma tabela em consultas subsequentes.

&nbsp;

Dada a consulta SQL abaixo:

```sql
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, oi.quantity, oi.price, pr.product_id, pr.product_name, pr.description, pr.price AS product_price, pr.category_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc
```

&nbsp;

vamos criar uma view chamada **customer_order_product_view** com o seguinte comando:
```sql
CREATE VIEW customer_order_product_view AS
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, oi.quantity, oi.price, pr.product_id, pr.product_name, pr.description, pr.price AS product_price, pr.category_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc;

-- OBS: caso uma coluna tenha nome repetido, a criação da view vai falhar
CREATE VIEW customer_order_product_view AS
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, od.customer_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
ORDER BY od.total_amount desc;

-- mas adicionar um alias já resolve, caso realmente queira adicionar as colunas duplicadas
CREATE VIEW customer_order_product_view AS
SELECT cs.customer_id as cs_customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, od.customer_id as od_customer_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
ORDER BY od.total_amount desc;
```

&nbsp;

Depois, para utilizar a view basta utilizar o comando select com o nome da view

```sql
SELECT * FROM customer_order_product_view;
```

&nbsp;

### Materialized view
Uma **materialized view** é uma cópia física do resultado de uma consulta que é armazenada no banco de dados como uma tabela. Diferente da view, a view materializada pode ser indexada e consultada como qualquer outra tabela. Ela é particularmente útil quando temos uma query muito complexa que é frequentemente executada e requer um tempo significativo de processamento.

&nbsp;

Dada a consulta SQL abaixo:

```sql
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, oi.quantity, oi.price, pr.product_id, pr.product_name, pr.description, pr.price AS product_price, pr.category_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc
```

&nbsp;

vamos criar uma materialized view chamada **customer_order_product_view** com o seguinte comando:
```sql
CREATE MATERIALIZED VIEW customer_order_product_mat_view AS
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, oi.quantity, oi.price, pr.product_id, pr.product_name, pr.description, pr.price AS product_price, pr.category_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc;

SELECT DISTINCT(teste_date), COUNT(teste_date) FROM teste_index GROUP BY teste_date
```

&nbsp;

Depois, para utilizar a materialized view basta utilizar o comando select com o nome da view

```sql
SELECT * FROM customer_order_product_mat_view;
```

&nbsp;

Como a materialized view é uma tabela física, pode acontecer de os dados ficarem desatualizados. Por exemplo, depois de fechado e registrado o pedido, foi incluso mais um ítem, alterando o valor total do pedido.

```sql
-- Ver quantidades antes de inserir, para poder comparar e ver se de fato vai aumentar
-- Update da tabela order_items
UPDATE order_items SET quantity=10 WHERE order_id = 1 AND product_id = 1

-- Adicionar a diferença no preço (diff_qtde * (select price.....))
-- Update da tabela orders
UPDATE orders SET total_amount = (SELECT total_amount FROM orders WHERE order_id = 1) + (SELECT price FROM products WHERE product_id = 1)
```

Se fizermos a consulta na tabela e na materialized view, teremos valores diferentes para a coluna total_amount e a quantidade do produto 1

```sql
-- select na tabela orders
SELECT * FROM orders WHERE order_id = 1
--"order_id"	"customer_id"	"order_date"	"total_amount"
--1	            1	            "2017-08-11"	108934.14

-- select na materialized view
SELECT order_id, product_id, order_date, total_amount FROM customer_order_product_mat_view WHERE order_id = 1 and product_id = 1
--"order_id"	"product_id"	"order_date"	"total_amount"
--1	            1	            "2017-08-11"	106529.00

-- select na tabela order_items
SELECT * FROM order_items WHERE order_id = 1 AND product_id = 1
--"order_id"	"product_id"	"quantity"	"price"
--1	            1	            10	        2405.14

-- select na materialized view
SELECT order_id, product_id, quantity, price FROM customer_order_product_mat_view WHERE order_id = 1 AND product_id = 1
--"order_id"	"product_id"	"quantity"	"price"
--1	            1	            9	        2405.14
```

&nbsp;

Neste caso, é necessário fazer o refresh dos dados, utilizando o comando abaixo. Com isso, a materialized view passa a estar atualizada.
```sql
-- refresh
REFRESH MATERIALIZED VIEW customer_order_product_mat_view;

-- select na materialized view
SELECT order_id, product_id, order_date, total_amount FROM customer_order_product_mat_view WHERE order_id = 1 and product_id = 1
--"order_id"	"customer_id"	"order_date"	"total_amount"
--1	            1	            "2017-08-11"	108934.14

-- select na materialized view
SELECT order_id, product_id, quantity, price FROM customer_order_product_mat_view WHERE order_id = 1 AND product_id = 1
--"order_id"	"product_id"	"quantity"	"price"
--1	            1	            10	        2405.14
```

&nbsp;