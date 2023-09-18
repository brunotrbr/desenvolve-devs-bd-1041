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

Nos inserts da tabela orders, adicionamos a data como uma string no formato DD-MM-YYYY (ex: 05-09-2015) e fazemos um cast para o campo date do banco de dados

```sql
INSERT INTO orders VALUES (9993,993,TO_DATE('06-09-2015','DD-MM-YYYY'),1659);
-- E aqui adicionamos a string com um formato diferente, mas mudamos o formato do cast também
INSERT INTO orders VALUES (9994,994,TO_DATE('2015/09/06','YYYY/MM/DD'),1034);
```

&nbsp;

### Select

&nbsp;

Limitar retorno do banco de dados, ordenar, remover duplicados, condicionais ou pular registros

> LIMIT, DISTINCT, ORDER BY, CASE e OFFSET

```sql
-- Por exemplo, para trazer somente os primeiros 10 clientes utilizamos a cláusula LIMIT
SELECT * FROM customers LIMIT 10

-- Por exemplo, para trazer somente os próximos 10 clientes utilizamos a cláusula LIMIT e OFFSET (ou seja, do 11 ao 20)
SELECT * FROM customers LIMIT 10 OFFSET 10

-- Para ordenar por ordem alfabética, utilizamos a cláusula ORDER BY (que pode ser asc ou desc, para ascendente ou descendente respectivamente)
SELECT * FROM customers order by first_name asc LIMIT 10 

-- Para remover estados repetidos, utilizamos a cláusula DISTINCT.Vamos identificar de quais estados são nossos clientes.
SELECT DISTINCT state FROM customers LIMIT 10 

-- Podemos também renomear o nome de colunas, utilizando a cláusula AS
SELECT DISTINCT state as estado FROM customers LIMIT 10

-- Podemos adicionar condicionais nos resultados, utilizando as cláusulas AS para adicionar uma nova coluna, e CASE-WHEN-ELSE para definir as condições
SELECT state,
CASE
WHEN state = 'Bruxelles-Capitale' THEN 'Bélgica'
WHEN state = 'Basse-Normandie' THEN 'França'
WHEN state = 'Friuli-Venezia Giulia' THEN 'Itália'
ELSE 'Desconhecido'
END
AS país
FROM customers limit 10;
```

&nbsp;

Para adicionar filtros no select:

> AND, OR, IN, IS NULL, IS NOT NULL, LIKE e BETWEEN

```sql
-- Recuperar os clientes que vivem nos estados unidos ou na espanha (opção 1)
SELECT * FROM customers WHERE country='EUA' or country='Espanha'

-- Recuperar os clientes que vivem nos estados unidos ou na espanha (opção 2)
SELECT * FROM customers WHERE country in ('EUA','Espanha')

-- Recuperar os clientes que vivem nos estados unidos e possuem um e-mail @harvard.edu
-- O caractere % indica que pode ter qualquer coisa antes do @
SELECT * FROM customers WHERE country='EUA' AND email LIKE '%@harvard.edu'

-- Buscar os registros cujo país está como null no sistema
SELECT * FROM customers WHERE country IS NULL

-- Buscar os registros cujo país NÃO está como null no sistema
SELECT * FROM customers WHERE country IS NOT NULL

-- Buscar os pedidos com valor maior ou igual que 500 e menor ou igual a 1000 (opção 1)
SELECT * FROM orders WHERE total_amount BETWEEN 500 AND 1000

-- Buscar os pedidos com valor maior ou igual que 500 e menor ou igual a 1000 (opção 2)
SELECT * FROM orders WHERE total_amount >= 500 AND total_amount <= 1000

-- Buscar os pedidos com valor menor ou igual a 500 e maior ou igual a 1000
SELECT * FROM orders WHERE total_amount NOT BETWEEN 500 AND 1000
```

&nbsp;

Funções para data e hora

> CURRENT_DATE, CURRENT_TIME e NOW

```sql
SELECT customer_id, first_name, state, CURRENT_DATE, CURRENT_TIME, NOW() FROM CUSTOMERS LIMIT 10 
```

&nbsp;

Formatação de dados:

> ROUND, DATE_PART, DATE_TRUNC, CONCAT, TRIM, LOWER, UPPER, SUBSTRING, POSITION e REPLACE

```sql
-- ROUND Arredonda os valores para a quantidade de casas decimais informadas após a vírgula. (Obs: avg é a média dos valores)
SELECT AVG(total_amount) AS average FROM orders where order_id in (1,2);
SELECT ROUND(AVG(total_amount), 2) AS rounded FROM orders where order_id in (1,2);


-- DATE_PART retorna somente o campo desejado (mês, neste caso)
SELECT order_date, DATE_PART('month', order_date) as month FROM orders;


-- DATE_TRUNC trunca uma parte da data ou um intervalo de tempo, até o mês neste caso, zerando o resto do resultado. Ou seja, ele retorna ano e mês, e o resto fica zerado.
SELECT order_date, DATE_TRUNC('month', order_date) as d_month FROM orders;
--order_date   d_month
-- "2017-08-11" "2017-08-01 00:00:00-03"

-- Neste exemplo, ele trunca até os minutos, e zera o restante.
SELECT order_date, DATE_TRUNC('minutes', order_date) as d_minutes FROM orders;


-- CONCAT concatena colunas
SELECT CONCAT(first_name, ' ', last_name) as nome_completo FROM customers limit 10;

-- TRIM remove espaços em branco no início e no fim de uma coluna
UPDATE customers SET first_name='    Julius    ' WHERE customer_id = 1
SELECT customer_id, first_name FROM customers WHERE CUSTOMER_ID = 1
SELECT customer_id, TRIM(first_name) FROM customers WHERE CUSTOMER_ID = 1

-- LOWER e UPPER retornam os valores em minúscula e maiúscula respectivamente
SELECT customer_id, LOWER(first_name), UPPER(last_name) FROM customers LIMIT 10

-- POSITION é utilizado para recuperar a posição de um ou mais caracteres em uma coluna. Caso não ache, retorna zero.
SELECT customer_id, email, POSITION('@' IN email) AS position_of_at FROM customers WHERE customer_id in (984,256,852);
SELECT customer_id, email, POSITION('@h' IN email) AS position_of_at FROM customers WHERE customer_id in (984,256,852);

-- SUBSTRING é utilizada para extrair um conjunto de caracteres de uma coluna
-- Extrair o domínio completo de um email. Reparem que utilizamos o position + 1, pois queremos a partir do caractere @
SELECT customer_id, email, SUBSTRING(email, POSITION('@' IN email) + 1) as dominio FROM customers WHERE customer_id in (984,256,852);
-- Extrair os 3 primeiros caracteres do domínio de um email.
SELECT customer_id, email, SUBSTRING(email, POSITION('@' IN email) + 1, 3) as dominio FROM customers WHERE customer_id in (984,256,852);

-- REPLACE é utilizado para substituir elementos em uma coluna
-- Ele não altera os dados, somente substitui na consulta
SELECT customer_id, email, REPLACE(email, '@', ' [at] ') as replaced_address FROM customers where customer_id in (984,256,852);
select customer_id, email from customers where customer_id in (984,256,852);

```