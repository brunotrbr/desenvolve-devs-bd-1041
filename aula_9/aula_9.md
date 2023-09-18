# Data Warehouses

## Cenário hipotético

Vamos supor que montamos nossa empresa, um e-commerce e lojas presenciais. Estamos com ele em funcionamento desde 2017, vendendo em média R$ 100.000.000 por mês desde 2018, e contamos com milhares de funcionários contratados no Brasil inteiro. E os funcionários tem dependentes, e benefícios e etc.

Imaginem que o gerente de vendas queira buscar todas as vendas, os dados dos produtos adquiridos, dos compradores e dos fornecedores de 2017 até março de 2023.

Por quê? Porque ele pode. Alguém teve a brilhante ideia de dar acesso pra ele ao banco de dados e mandou pra ele a consulta pra buscar os dados só de 2017, mas ele entendeu como funcionava e colocou tudo até o mês passado.

Agora imaginem que ao mesmo tempo o gerente do RH quer rodar o cálculo da folha de pagamento e dos benefícios, calculando descontos, salário, comissões, gerar dados para imposto de renda e receita federal, etc.

E outros gerentes de vendas regionais também querem gerar seus relatórios.

E as pessoas continuam buscando produtos e realizando compras.

E nós utilizamos único banco de dados que, por milagre, sempre aguentou o tranco.

Até hoje! 

O que vai acontecer com o sistema? Com o banco de dados? Com nossa aplicação?

&nbsp;

Pode ficar muito lento, prejudicando todos os usuários.

E se o gerente de TI vira pra vocês e dizer: resolvam. O que vocês fazem?

&nbsp;

## Data Warehouses

Para o problema acima poderíamos:
  
  - Tentar aumentar o processamento do servidor, adicionando memória e/ou CPU. O chamado escalonamento vertical. Mas esse não daria conta.
  - Tentar replicar os bancos, dividindo em um banco pra consulta/leitura e outro para inserts/updates/deletes. O chamado escalonamento horizontal. Mas isso também não daria certo.
  - Criar um Data Warehouse

&nbsp;

O que é Data Warehouse?

Um Data Warehouse é uma coleção de dados integrados, orientado por assunto, variável com o tempo e não volátil.

	- organizado por assunto (vendas, metas, financeiro, rh, etc)
	
    - apresenta uma linha histórica dos dados em um determinado tempo e apresenta os dados em um outro tempo. Ou seja, no ano X a empresa estava do jeito X, diferente do ano Y, em que o retrato da empresa era Y.
	
    - não volátil, pois não deve ser permitidas alterações nos dados após a inserção. Caso haja modificação, perdemos o retrato histórico da empresa (como a empresa estava no ano que estamos analizando)
	
    - existe para demonstrar o histórico da empresa ao longo dos anos, permitindo análise para novas ações planejadas pela empresa para futuros negócios.

&nbsp;

> Resumindo, é um banco de dados (um depósito de dados) especializados em consultas e análises gerenciais, normalmente dividido por assunto.


&nbsp;

Vantagens:

    - Alta performance para consultas
  
    - Facilidade para análise de dados

&nbsp;

Desvantagens:

    - Manter o Data Warehouse (backups, sincronização, ETL)


&nbsp;


Considerando o cenário descrito acima, poderíamos ter:

- Um banco chamado **acompanhamento_metas**, para que os gerentes possam acompanhar as vendas correntes

- Um banco chamado **acompanhamento_anual**, para gerar os relatórios de vendas dos anos passados

- Um banco chamado **folha_pagamento** com os dados para processar o pagamento dos funcionários

Dependendo da necessidade, poderíamos criar N bancos no Data Warehouse, com finalidades específicas.

&nbsp;

## Como criamos um Data Warehouse

Para entender melhor como surge o Data Warehouse, vamos observar a imagem abaixo:

<img src=./imagens/data_warehouse.png width=500>

&nbsp;

Na imagem acima, podemos observar diversas fontes geradoras de dados.

Estes dados vão passar por um processo de transformação, chamado de ETL (extract, transform, load) onde

	- Extract refere-se a extração dos dados das mais diversas fontes
  
	- Transform refere-se a transformação dos dados em um dado utilizado para um determinado assunto
  
	- Load é a carga para o Data Warehouse, disponibilizando o conjunto de dados para análise


Após o ETL e a carga das informações no Data Warehouse, ocorre o processo de análise para apoio a tomada de decisões da empresa.

&nbsp;

### OLTP x OLAP

Bancos de dados OLTP (Online Transaction Processing) são destinados a processamentos do dia a dia da empresa. Ex: Nosso postgresql que registra as vendas, o mongoDB que armazena a descrição dos produtos, o elasticsearch que usamos para agilizar o processo de consulta para determinados produtos/pontos do sistema, etc.

Sistemas OLAP (Online Analytical Processing) são utilizados para análise e processamentos de dados. Ex: Um Data Warehouse pode ser um sistema OLAP, ou Data Lake, ou até mesmo outras ferramentas e softwares podem ser sistemas OLAP.

&nbsp;

## Criando nosso Data Warehouse

Nós vamos criar um Data Warehouse super simples usando nosso banco de dados e nossas tabelas.

- Vamos juntar todas as colunas relevantes e não duplicadas em um tabelão único.

- Os dados são históricos, e não transações correntes do dia a dia.

Primeiro vamos criar um novo banco de dados/schema chamado **dw_acompanhamento_vendas**

```sql
CREATE DATABASE dw_acompanhamento_vendas
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1

CREATE SCHEMA dw_acompanhamento_vendas
    AUTHORIZATION postgres;
```

Depois vamos criar uma tabela chamada **vendas** com todas as colunas das outras tabelas do banco de dados, eliminando as repetidas

```sql
CREATE TABLE dw_acompanhamento_vendas.vendas (
    customer_id INT,
	customer_name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    order_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    category_name VARCHAR(100),
    supplier_name VARCHAR(100),
    supplier_email VARCHAR(100),
    supplier_phone VARCHAR(20),
    supplier_address VARCHAR(200),
	product_id INT,
    product_name VARCHAR(100),
    description VARCHAR(500),
    price DECIMAL(10, 2),
    quantity INT
);
```

Agora vamos fazer o processo de ETL, criando uma stored procedure para ler nossas tabelas do banco transacional e inserir os registros no dw_acompanhamento_vendas

```sql
-- PROCEDURE: public.copy_data_to_vendas()

-- DROP PROCEDURE IF EXISTS public.copy_data_to_vendas();

CREATE OR REPLACE PROCEDURE public.copy_data_to_vendas(
	)
LANGUAGE 'plpgsql'
AS $BODY$
DECLARE
    record_to_copy RECORD;
BEGIN
    -- Connecta no banco de dados
    PERFORM pg_catalog.pg_database_size('postgres');
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Database Postgres does not exist.';
    END IF;

    -- Procura os registros nas tabelas do banco A
    FOR record_to_copy IN SELECT cus.customer_id as customer_id, (cus.first_name || ' ' || cus.last_name) as customer_name, cus.email as email, cus.address as address, cus.city as city, cus.state as state, cus.country as country, ord.order_id as order_id, ord.order_date as order_date, ord.total_amount as total_amount, prd.product_id, prd.product_name, prd.description, cat.category_name, sup.supplier_name, sup.supplier_email, sup.supplier_phone, sup.supplier_address, oi.quantity, oi.price
		FROM public.customers cus
		INNER JOIN public.orders ord ON cus.customer_id = ord.customer_id
		INNER JOIN public.order_items oi ON ord.order_id = oi.order_id
		INNER JOIN public.products prd ON prd.product_id = oi.product_id
		INNER JOIN public.categories cat ON cat.category_id = prd.category_id
		INNER JOIN public.suppliers sup ON sup.supplier_id = prd.supplier_id
	LOOP
        -- Verifica se já existe o registro no banco B. Se NÃO EXISTE, insere
		IF NOT EXISTS (SELECT (1) FROM dw_acompanhamento_vendas.vendas WHERE order_id = record_to_copy.order_id AND product_id = record_to_copy.product_id) THEN
			-- Insere os registros na tabela de vendas do banco B
			INSERT INTO dw_acompanhamento_vendas.vendas (
				customer_id,
				customer_name,
				email,
				address,
				city,
				state,
				country,
				order_id,
				order_date,
				total_amount,
				product_id,
				product_name,
				description,
				category_name,
				supplier_name,
				supplier_email,
				supplier_phone,
				supplier_address,
				quantity,
				price
			) VALUES (
				record_to_copy.customer_id,
				record_to_copy.customer_name,
				record_to_copy.email,
				record_to_copy.address,
				record_to_copy.city,
				record_to_copy.state,
				record_to_copy.country,
				record_to_copy.order_id,
				record_to_copy.order_date,
				record_to_copy.total_amount,
				record_to_copy.product_id,
				record_to_copy.product_name,
				record_to_copy.description,
				record_to_copy.category_name,
				record_to_copy.supplier_name,
				record_to_copy.supplier_email,
				record_to_copy.supplier_phone,
				record_to_copy.supplier_address,
				record_to_copy.quantity,
				record_to_copy.price
			);
		END IF;
    END LOOP;
END;
$BODY$;
ALTER PROCEDURE public.copy_data_to_vendas()
    OWNER TO postgres;
```

Depois, para rodar a procedure, executamos o seguinte código
```sql
CALL public.copy_data_to_vendas()

-- Conferência dos dados
SELECT count(1) FROM dw_acompanhamento_vendas.vendas

-- Conferência dos dados
SELECT count(1) FROM public.order_items
```

Para comparar o desempenho, podemos realizar as seguintes consultas

```sql
-- Tabelas do banco A
SELECT cus.customer_id, (cus.first_name || ' ' || cus.last_name) as customer_name, cus.email as email, cus.address as address, cus.city as city, cus.state as state, cus.country as country, ord.order_id as order_id, ord.order_date as order_date, ord.total_amount as total_amount, prd.product_id, prd.product_name, prd.description, cat.category_name, sup.supplier_name, sup.supplier_email, sup.supplier_phone, sup.supplier_address, oi.quantity, oi.price
FROM public.customers cus
INNER JOIN public.orders ord ON cus.customer_id = ord.customer_id
INNER JOIN public.order_items oi ON ord.order_id = oi.order_id
INNER JOIN public.products prd ON prd.product_id = oi.product_id
INNER JOIN public.categories cat ON cat.category_id = prd.category_id
INNER JOIN public.suppliers sup ON sup.supplier_id = prd.supplier_id

-- Tabela do Data Warehouse
SELECT customer_id, customer_name, email, address, city, state, country, order_id, order_date, total_amount, category_name, supplier_name, supplier_email, supplier_phone, supplier_address, product_id, product_name, description, price, quantity
	FROM dw_acompanhamento_vendas.vendas;
```

Para que o processo como um todo seja funcional, é necessário agendar essa procedure para que ela execute a cada x períodos de tempo (toda noite, todo dia 1º do mês, etc) para que o Data Warehouse fique sempre atualizado.

Não vamos entrar no processo de agendamento, mas seria utilizando uma ferramenta própria do postgresql, chamada pgAgent.

&nbsp;

Caso o Data Warehouse começe a ficar sobrecarregado, por milhares de acessos (exemplo de empresas multinacionais presentes vários países, querendo gerar relatórios simultaneamente), podemos "qubrar" o Data Warehouse em vários **Data Marts** menores.

&nbsp;

## Data Mart

Um data mart é uma forma simples de data warehouse que se concentra em um único assunto ou linha de negócios, como vendas, finanças ou marketing. 

Considerando o foco, os data marts extraem dados de menos fontes do que os data warehouses. Ex: Data Mart do RH do Brasil, das vendas dos EUA, da contabilidade global, etc.