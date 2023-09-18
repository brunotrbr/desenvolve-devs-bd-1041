# Ordem sugerida de resolução dos exercícios

Caminho:
Material do Aluno > Turma 941 > DS-PY-006 Banco de Dados I > Tipos de bancos de dados > Exercícios

1) ds-py-941-banco-de-dados-configuracao
2) ds-py-941-banco-de-dados-modelagem
3) ds-py-941-banco-de-dados-generalizacao
4) ds-py-941-banco-de-dados-normalizacao
5) ds-py-941-banco-de-dados-modelagem-logica
6) ds-py-941-banco-de-dados-modelagem-fisica
7) ds-py-941-banco-de-dados-sql-1
8) ds-py-941-banco-de-dados-sql-2

# Manipulando banco de dados

OBS: Os valores de order_id e product_id abaixo vão variar de acordo com a inserção dos dados. Buscar dados atualizados para os exemplos.

## Plano de execução

São os passos adotados pelo SGBD para localizar, buscar e devolver um ou mais registros do banco de dados. Determina os índices ou tabelas que serão acessados, o algoritmo de join para juntar os dados e a ordem que serão realizadas as operações.

Podemos visualizar o plano de execução clicando em EXPLAIN no PGAdmin ou adicionando a palavra EXPLAIN no início da consulta.

```sql
EXPLAIN SELECT * FROM orders WHERE order_date = '2017-08-11';

EXPLAIN SELECT * FROM order_items FROM order_id = 1 AND product_id = 37
```

&nbsp;

A partir do plano de execução conseguimos identificar eventuais gargalos como:
- full table scans
- joins custosos
  
e atuar para melhorar esses pontos:
- Criando novos índices
- reestruturando tabelas

&nbsp;

Observando as consultas acima, podemos ver que foi realizado um **sequential scan** na tabela de pedidos, enquanto na consulta 2 foi realizado um **index Scan**.

&nbsp;

### Scan

#### Sequential Scan

O SGBD percorre todo o disco onde os dados estão armazenados, em busca das linhas da tabela.

Na imagem abaixo:
<img src=./imagens/b_plus_tree.png width=500>

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
<img src=./imagens/b_plus_tree.png width=500>

&nbsp;

Ao procurar pelo registro 0007, o SGBD vai percorrer 0005 > 0007 > 0008/0009 > 0007

```sql
-- Exemplo
EXPLAIN SELECT * FROM order_items WHERE order_id = 1 AND product_id = 37
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

<img src=./imagens/bitmap_scan.png width=400>

&nbsp;

Normalmente ocorre quando a consulta é pequena demais para um sequential scan mas grande demais para um index scan.

```sql
-- Exemplo
SELECT * FROM orders WHERE order_id BETWEEN 1000 AND 2000

SELECT order_id, total_amount FROM orders WHERE order_id BETWEEN 1000 AND 4000

SELECT order_id FROM orders WHERE order_id BETWEEN 1000 AND 3000
--Obs: modifiquem o range de dados do order_id para verificar qual scan está sendo realizado
```

&nbsp;

### Joins

Operação de junção de tabelas para retornar os dados das consultas que envolvem 2 ou mais tabelas.

- Processam somente 2 tabelas por vez.
- Caso tenha mais tabelas, realiza o join de duas tabelas, criando uma tabela intermediária. Depois realiza o join da tabela intermediária com a próxima, gerando outra intermediária. Continua nesse processo até não existirem mais tabelas para serem unidas.

&nbsp;

Existem 3 tipos de joins

- Nested Loops
- Hash Join / Hash
- Merge Join

> Obs: Não temos o controle de qual tipo de join vai ser realizado. Ele é escolhido automaticamente pelo SGBD de acordo com a consulta realizada.

&nbsp;

#### Nested Loops
- Obtém as linhas da tabela 1.
- Para cada linha da tabela 1, tenta realizar o match dos dados com cada linha da tabela dois.

&nbsp;

Exemplo de alto nível:
```python
for linha_tab_1 in tabela_1:
    for linha_tab_2 in tabela_2:
        match dos campos
```

&nbsp;

Exemplo de consultas que realiza nested loop:
```sql
-- nested loop com 2 tabelas
SELECT * FROM order_items oi 
INNER JOIN products pr on oi.product_id = pr.product_id
INNER JOIN orders od on oi.order_id = od.order_id
WHERE oi.order_id in (1,2,3) and oi.product_id in (37,119,123, 291)

-- nested loop com 3 tabelas
SELECT * FROM order_items oi 
INNER JOIN products pr ON oi.product_id = pr.product_id
INNER JOIN orders od ON oi.order_id = od.order_id
INNER JOIN customers cs ON cs.customer_id = od.customer_id
WHERE oi.order_id IN (1,2,3) and oi.product_id in (37,119,123, 291)
```

&nbsp;

#### Hash Join / Hash
- Carrega os registros candidatos da tabela 1 em uma tabela de hash (hash table).
- Para cada linha da tabela 2, tenta dar match com os registros da tabela de hash

<img src=./imagens/hash_table.png width=400 style="background:white">

Tabela de hash

&nbsp;

Exemplo de consulta que realiza hash join:
```sql
SELECT o.order_id, oi.product_id, oi.quantity, oi.price, p.product_name
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
```

&nbsp;

#### Merge Join
Combina duas tabelas. Como pré-requisito, elas precisam estar previamente ordenadas (passo realizado pelo SGBD).


<img src=./imagens/merge_join.gif width=400>

&nbsp;

Exemplo de consulta que realiza merge join:
```sql
-- merge join
-- Não consegui criar um exemplo.
```

&nbsp;

### Sorting and Grouping

&nbsp;

#### Sort / Sort Key
- Ordena o conjunto de colunas especificados na cláusula **order by**.
- Requer grande quantidade de memória para materializar o resultado intermediário.

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

- Localizar mais rapidamente os dados inseridos no banco de dados
- Apontamento direto para onde o registro está salvo
  
&nbsp;

Exemplo:

    Vamos criar uma tabela que armazena um id serial e uma data, e depois vamos inserir 400.000.000 de registros, sendo 100.000.000 para cada data em 22/04/2023, 22/03/2023, 22/02/2022 e 22/01/2022


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
SELECT COUNT(1) FROM teste_index;

SELECT DISTINCT(teste_date), COUNT(teste_date) FROM teste_index GROUP BY teste_date;
```

&nbsp;

### busca com index x busca sem index

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
- Tabela virtual que não armazena dados, e sim uma "visão" dos dados armazenados em outras tabelas.
- É uma consulta SQL armazenada no banco de dados, para ser usada em consultas subsequentes.

> IMPORTANTE:
> Os dados de product id são referentes ao insert que fizemos em aula. Para que os comandos funcionem, devem pesquisar os product_ids dos inserts no próprio banco de vocês. Ex: no do professor o product_id era 37, no meu vai ser xxxx.


&nbsp;

Dada a consulta SQL abaixo:

```sql
SELECT cs.customer_id, cs.first_name, cs.last_name, cs.email, cs.address, cs.city, cs.state, cs.country, od.order_id, od.order_date, od.total_amount, oi.quantity, oi.price, pr.product_id, pr.product_name, pr.description, pr.price AS product_price, pr.category_id
FROM customers cs
INNER JOIN orders od on od.customer_id = cs.customer_id
INNER JOIN order_items oi on oi.order_id = od.order_id
INNER JOIN products pr on pr.product_id = oi.product_id
ORDER BY od.total_amount desc
-- Query complete 00:00:00.529
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

Para utilizar a view basta utilizar o comando select com o nome da view

```sql
SELECT * FROM customer_order_product_view;
-- Query complete 00:00:00.330
```

&nbsp;

### Materialized view
- Cópia física do resultado de uma consulta que é armazenada no banco de dados como uma tabela
- Pode ser indexada e/ou consultada como qualquer outra tabela
- Útil para consultas complexas frequentemente executadas e que requerem um tempo significativo de processamento.

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
```

&nbsp;

Depois, para utilizar a materialized view basta utilizar o comando select com o nome da view

```sql
SELECT * FROM customer_order_product_mat_view;
```

&nbsp;

**Importante:**

> Materialized view é uma tabela física, e por isso os dados podem ficar desatualizados.
>
> É necessário reatualizar ela (refresh)

&nbsp;

```sql
-- Ver quantidades antes de inserir
-- Update da tabela order_items
UPDATE order_items SET quantity=10 WHERE order_id = 1 AND product_id = 37

-- Adicionar a diferença no preço 
-- Update da tabela orders
UPDATE orders SET total_amount = (SELECT total_amount FROM orders WHERE order_id = 1) + (SELECT price FROM products WHERE product_id = 37)
```

&nbsp;

Se fizermos a consulta na tabela e na materialized view, teremos valores diferentes para a coluna total_amount e a quantidade do produto 37

```sql
-- select na tabela orders
SELECT * FROM orders WHERE order_id = 1
--"order_id"	"customer_id"	"order_date"	"total_amount"
--1	          37	          "2017-08-11"	108934.14

-- select na materialized view
SELECT order_id, product_id, order_date, total_amount FROM mat_customer_order_product_view WHERE order_id = 1 and product_id = 37
--"order_id"	"product_id"	"order_date"	"total_amount"
--1	          37            "2017-08-11"	106529.00

-- select na tabela order_items
SELECT * FROM order_items WHERE order_id = 1 AND product_id = 37
--"order_id"	"product_id"	"quantity"	"price"
--1	          37            10	        2405.14

-- select na materialized view
SELECT order_id, product_id, quantity, price FROM mat_customer_order_product_view WHERE order_id = 1 AND product_id = 37
--"order_id"	"product_id"	"quantity"	"price"
--1	          37            9	        2405.14
```

&nbsp;

Fazendo refresh dos dados na materialized view

```sql
-- refresh
REFRESH MATERIALIZED VIEW mat_customer_order_product_view;

-- select na materialized view
SELECT order_id, product_id, order_date, total_amount FROM mat_customer_order_product_view WHERE order_id = 1 and product_id = 37
--"order_id"	"customer_id"	"order_date"	"total_amount"
--1	          37	           "2017-08-11"	108934.14

-- select na materialized view
SELECT order_id, product_id, quantity, price FROM mat_customer_order_product_view WHERE order_id = 1 AND product_id = 37
--"order_id"	"product_id"	"quantity"	"price"
--1	          37            10	        2405.14
```


&nbsp;

### Bonus: Criação de trigger para atualizar materialized view

#### Trigger

A cada ação realizada, dispara um evento. ex: ao inserir um pedido, modifica o campo last_order_date na tabela de customers.

#### Stored procedures

Rotinas e processos que podem ser chamados a qualquer momento no banco de dados, dentro ou fora de triggers, etc.

&nbsp;

Para criar uma função e uma trigger, siga os passos abaixo:

```sql
-- Os comandos abaixo sãu utilizados para criar uma função chamada update_materialized_view(), que é a responsável por fazer o refresh na materialized view. 
CREATE OR REPLACE FUNCTION update_materialized_view() RETURNS TRIGGER AS $$
BEGIN
    REFRESH MATERIALIZED VIEW mat_customer_order_product_view;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- A trigger dessa função é a cada insert na tabela order_items
CREATE TRIGGER update_mat_view_order_item
AFTER INSERT ON order_items
FOR EACH ROW
EXECUTE FUNCTION update_materialized_view();

-- Aqui são códigos de teste para ver se a função/trigger estão funcionando corretamente.
INSERT INTO orders VALUES (9997,3,TO_DATE('15-03-2023','DD-MM-YYYY'),20000.00);
select * from orders where order_id = 9997
select * from order_items where order_id = 9997
select * from customers where customer_id = 3
SELECT * FROM mat_customer_order_product_view where order_id = 9997
```