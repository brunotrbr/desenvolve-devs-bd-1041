# Manipulando banco de dados

## Criando um banco de dados simples para um e-commerce

Modelagem simplificada:

> Nosso ecommerce atende clientes e vende produtos. Uma venda somente ocorre se tiver pelo menos um produto no carrinho de compras. Os produtos possuem categorias e fornecedores para pesquisar no ecommerce, se necessário.

&nbsp;

Tabelas:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100),
    supplier_email VARCHAR(100),
    supplier_phone VARCHAR(20),
    supplier_address VARCHAR(200)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    description VARCHAR(500),
    price DECIMAL(10, 2),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```


Vamos executar os scripts abaixo para inserir valores nas tabelas

01_insert_customers.sql
02_insert_suppliers.sql
03_insert_categories.sql
04_insert_orders.sql
05_insert_products.sql
06_populate_ecommerce.sql
07_adjust_database.sql


&nbsp;

### Select

&nbsp;

Limitar retorno do banco de dados, ordenar, remover duplicados, condicionais ou pular registros

> LIMIT, DISTINCT, ORDER BY, CASE e OFFSET

```sql
-- Por exemplo, para trazer somente os primeiros 10 clientes utilizamos a cláusula LIMIT


-- Por exemplo, para trazer somente os próximos 10 clientes utilizamos a cláusula LIMIT e OFFSET (ou seja, do 11 ao 20)


-- Para ordenar por ordem alfabética, utilizamos a cláusula ORDER BY (que pode ser asc ou desc, para ascendente ou descendente respectivamente)


-- Para remover estados repetidos, utilizamos a cláusula DISTINCT.Vamos identificar de quais estados são nossos clientes.


-- Podemos também renomear o nome de colunas, utilizando a cláusula AS


-- Podemos adicionar condicionais nos resultados, utilizando as cláusulas AS para adicionar uma nova coluna, e CASE-WHEN-ELSE para definir as condições

```

&nbsp;

Para adicionar filtros no select:

> AND, OR, IN, IS NULL, IS NOT NULL, LIKE e BETWEEN

```sql
-- Recuperar os clientes que vivem nos estados unidos ou na espanha (opção 1)


-- Recuperar os clientes que vivem nos estados unidos ou na espanha (opção 2)


-- Recuperar os clientes que vivem nos estados unidos e possuem um e-mail @harvard.edu
-- O caractere % indica que pode ter qualquer coisa antes do @


-- Buscar os registros cujo país está como null no sistema


-- Buscar os registros cujo país NÃO está como null no sistema


-- Buscar os pedidos com valor maior ou igual que 500 e menor ou igual a 1000 (opção 1)


-- Buscar os pedidos com valor maior ou igual que 500 e menor ou igual a 1000 (opção 2)


-- Buscar os pedidos com valor menor ou igual a 500 e maior ou igual a 1000

```

&nbsp;

Funções para data e hora

> CURRENT_DATE, CURRENT_TIME e NOW

```sql

```

&nbsp;

Formatação de dados:

> ROUND, DATE_PART, DATE_TRUNC, CONCAT, TRIM, LOWER, UPPER, SUBSTRING, POSITION e REPLACE

```sql
-- ROUND Arredonda os valores para a quantidade de casas decimais informadas após a vírgula. (Obs: avg é a média dos valores)



-- DATE_PART retorna somente o campo desejado (mês, neste caso)



-- DATE_TRUNC trunca uma parte da data ou um intervalo de tempo, até o mês neste caso, zerando o resto do resultado. Ou seja, ele retorna ano e mês, e o resto fica zerado.

--order_date   d_month
-- "2017-08-11" "2017-08-01 00:00:00-03"

-- Neste exemplo, ele trunca até os minutos, e zera o restante.



-- CONCAT concatena colunas


-- TRIM remove espaços em branco no início e no fim de uma coluna

-- LOWER e UPPER retornam os valores em minúscula e maiúscula respectivamente


-- POSITION é utilizado para recuperar a posição de um ou mais caracteres em uma coluna. Caso não ache, retorna zero.


-- SUBSTRING é utilizada para extrair um conjunto de caracteres de uma coluna
-- Extrair o domínio completo de um email. Reparem que utilizamos o position + 1, pois queremos a partir do caractere @

-- Extrair os 3 primeiros caracteres do domínio de um email.


-- REPLACE é utilizado para substituir elementos em uma coluna
-- Ele não altera os dados, somente substitui na consulta


```

# Joins

Com frequência, queremos buscar dados relacionados em outras tabelas. Esse é um dos principais motivos de se usar um banco relacional, para que se tenham dados relacionados e seja simples de buscar estas relações.

São exemplos de joins:

> CROSS JOIN, INNER JOIN, RIGHT JOIN, LEFT JOIN, FULL JOIN e SELF JOIN

Cross Join:
<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-6/conteudo/cross_join.png width=500>

&nbsp;

Demais joins:
<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-6/conteudo/sql_joins.png width=700>

```sql
-- CROSS JOIN gera todas as combinações possíveis para cada uma das linhas das tabelas relacionadas



-- INNER JOIN gera as combinações em que a cláusula ON do join seja verdadeira, ou seja que os customer_ids, sejam iguais no exemplo abaixo



-- LEFT JOIN gera as combinações em que a cláusula ON do join seja verdadeira. Caso a tabela do lado esquerdo (a primeira) não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor zerado



-- RIGHT JOIN gera as combinações em que a cláusula ON do join seja verdadeira. Caso a tabela do lado direito (a segunda) não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor zerado

-- Exemplo invertendo as tabelas


-- FULL JOIN gera as combinações em que a cláusula ON do join seja verdadeira. Caso alguma não satisfaça a igualdade da cláusula ON, ela é inclusa no resultado igual, mas com o valor null


-- SELF JOIN é usado para fazer join entre a mesma tabela, mas usando aliases diferentes. Não existe a palavra reservada SELF JOIN, portanto podemos usar o INNER JOIN com alias diferentes.

```
&nbsp;

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.