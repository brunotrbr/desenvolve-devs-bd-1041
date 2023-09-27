#  Modelo lógico -> Modelo Físico (SQL)

**Modelo Lógico**: Inclui detalhes da implementação do banco de dados.

**Modelo físico**: É a implementação no banco de dados. Ele demonstra como os dados são fisicamente armazenados.

Agora que fizemos a criação do modelo lógico, vamos criar o que chamamos de modelo físico.


Para passar do modelo lógico para o conceitual, utilizamos os comandos da categoria **DDL** e **DCL**, vistas abaixo.

As demais categorias são utilizadas na manipulação dos dados.

Não vou me aprofundar na descrição de cada um deles aqui, pois vamos falar deles na prática também. Ainda assim, vou deixar a relação abaixo com a descrição de cada uma das categorias e os comandos possíveis.

&nbsp;

## DDL - Data Definition Language

Tem a linguagem de definição de dados (em inglês, DDL), que são os comandos utilizados para definir a estrutura do banco de dados. A DDL inclui os comandos CREATE, ALTER, DROP, TRUNCATE e RENAME:

    - CREATE: usado para criar tabelas, view, index ou outros objetos do banco de dados.

    - ALTER:  Usado para modificar a estrutura de um objeto do banco de dados.

    - DROP: Usado para remover a estrutura de um objeto do banco de dados.

    - TRUNCATE: Usado para remover todos os dados de uma tabela.

    - RENAME: Usado para modificar o nome de um objeto existente no banco de dados.

&nbsp;

## DML - Data Manipulation Language

Tem a linguagem de manipulação de dados (em inglês, DML), que são os comandos utilizados para manipular os dados armazenados no banco de dados. A DML inclui os comandos SELECT, INSERT, UPDATE e DELETE.

    - SELECT: Usado para recuperar dados de uma ou mais tabelas.
    
    - INSERT: Usado para adicionar dados em uma tabela.
    
    - UPDATE: Usado para atualizar dados previamente inseridos em uma tabela.
    
    - DELETE: Usado para remover dados de uma tabela.

    - MERGE: Usado para combinar dados de duas tabelas em uma tabela única.

&nbsp;

## DCL - Data Control Language

Por fim temos a linguagem de controle dos dados (em inglês, DCL), que são os comandos utilizados para controlar o acesso ao banco de dados. A DCL inclui os comandos GRANT, REVOKE e DENY.

    - GRANT: Usado para dar permissões a um usuário para acessar objetos do banco de dados.

    - REVOKE Usado para remover permissões dadas a um usuário para acessar objetos do banco de dados.

    - DENY: Usado para negar acesso a objetos do banco de dados a um usuário.

&nbsp;

## DQL - Data Query Language

Por fim temos a linguagem de consulta dos dados (em inglês, DQL), que são os comandos utilizados para acessar o banco de dados e recuperar valores. A DQL inclui o comando SELECT.

    - SELECT: Usado para recuperar os dados do banco de dados.

&nbsp;

# CRUD em SQL

Acredito que pelo menos metade de vocês já devem ter ouvido a expressão CRUD, certo?

CRUD é a sigla em inglês para Create, Read, Update, Delete. 

São as principais ações que fazemos no banco de dados SQL quando não somos os administradores do banco.

Ou seja, na nossa carreira de DEV.

&nbsp;

## C - Create
É usado tanto para criar tabelas, views e outros objetos do banco quanto para inserir dados.

Para criar tabelas, usamos o comando **CREATE TABLE**. e sua sintaxe é:

```sql
CREATE TABLE <qualificador> <schema>.<nome_da_tabela>
(
    <nome_da_coluna> <tipo(Date, int, varchar, etc)> <opções (NOT NULL, UNIQUE, DEFAULT, etc)>,
    ...
    ...
    <restrições>
);

-- OBS: O <schema> é opcional. O default     é public, mas pode ser alterado nas configurações do banco de dados.
```

&nbsp;

#### Exemplo:
Dado nosso modelo lógico da empresa acme, para a entidade **funcionarios**, vamos escrever o comando para criar a tabela.

    funcionarios (cod, cpf, nome, endereco, salario, genero, dt_nasc, num_dpto, cod_supervisor)
        cod PK
        CPF UNIQUE
        num_dpto FK departamentos
        cod_supervisor FK funcionarios

&nbsp;

```sql
CREATE TABLE public.funcionarios (
	cod int NOT NULL,
    cpf varchar(11) NOT NULL,
	nome varchar(50) NOT NULL,
	endereco varchar(100) NOT NULL,
	salario numeric NOT NULL,
	genero smallint NULL,
	dt_nasc date NOT NULL,
	cod_supervisor int NULL,
	CONSTRAINT funcionarios_pk PRIMARY KEY (cod),
	CONSTRAINT funcionarios_un UNIQUE (cpf)
);
```

&nbsp;

Reparem que não criamos o atributo **num_dpto**, uma vez que para incluir ele precisamos primeiro criar a tabela **departamentos**.

    departamentos (num_dpto, nome_dpto, cod_gerente, data_inicio_gerente)
        num_dpto PK
        nome_dpto UNIQUE
        cod_gerente FK funcionarios

Como o departamento pede o atributo cod_gerente, da tabela de **funcionarios**, vamos deixar o campo cod_gerente como opcional.

```sql
CREATE TABLE departamentos (
	cod int4 NOT NULL,
	nome varchar(50) NOT NULL,
	cod_gerente int4 NULL,
	dt_ini_gerente date NULL,
	CONSTRAINT departamentos_pk PRIMARY KEY (cod),
	CONSTRAINT departamentos_un UNIQUE (nome),
	CONSTRAINT dpto_func_fk FOREIGN KEY (cod_gerente) REFERENCES public.funcionarios(cod)
);
```

Agora vamos alterar a tabela **funcionarios**, para incluir o atributo num_dpto. Obs: Alter table é um comando de update, não de create.

```sql
ALTER TABLE funcionarios ADD COLUMN cod_dpto int NULL;
ALTER TABLE funcionarios ADD CONSTRAINT func_dpto_fk FOREIGN KEY (cod_dpto) REFERENCES departamentos (cod);
```

&nbsp;

Agora podemos começar inserindo os departamentos e os funcionários, usando o comando **INSERT INTO**.

Sua sintaxe é:

```sql
INSERT INTO <nome_da_tabela> (<nome_das_colunas>) VALUES (<valores>)
```

```sql
INSERT INTO departamentos (cod, nome)
VALUES
 (1, 'vendas'),
 (2, 'desenvolvimento'),
 (3, 'financeiro')
;
```

&nbsp;

Por que não inserimos o código do gerente e a data de início do gerente?

Porque são opcionais.

&nbsp;

Agora vamos inserir funcionários.

```sql
-- Com erro de cpf (UNIQUE)
INSERT INTO public.funcionarios
(cod, cpf, nome, endereco, salario, genero, dt_nasc, cod_supervisor, cod_dpto)
VALUES
(1, '123', 'Pedro', 'Avenida um, 55', 2000, 1, 
'2002-02-21', null, 1),
(2, '456', 'Luciana', 'Avenida dois, 44', 3000, 2, '2002-11-6', null, 3),
(3, '789', 'Ísis', 'Avenida três, 12', 2000, 2, '2002-05-19', null, 2),
(4, '159', 'Lucas', 'Avenida quatro, 65', 16000, 1, '1957-08-11', null, 3),
(5, '123', 'Eduardo', 'Avenida cinco, 555', 5000, 1, '1981-04-29', null, 2)
;

INSERT INTO public.funcionarios
(cod, cpf, nome, endereco, salario, genero, dt_nasc, cod_supervisor, cod_dpto)
VALUES
(1, '123', 'Pedro', 'Avenida um, 55', 2000, 1, 
'2002-02-21', null, 1),
(2, '456', 'Luciana', 'Avenida dois, 44', 3000, 2, '2002-11-6', null, 3),
(3, '789', 'Ísis', 'Avenida três, 12', 2000, 2, '2002-05-19', null, 2),
(4, '159', 'Lucas', 'Avenida quatro, 65', 16000, 1, '1957-08-11', null, 3),
(5, '753', 'Eduardo', 'Avenida cinco, 555', 5000, 1, '1981-04-29', null, 2)
;
```

&nbsp;

## R - Read
É usado para buscar valores no banco de dados

Sua sintaxe é:

```sql
SELECT <nome_das_colunas> FROM <nome_da_tabela> <restrições, junções, agrupamentos, etc>;
```

As restrições são impostas utilizando a cláusula **WHERE**, conforme a sintaxe abaixo:

```sql
-- Uma única restrição
WHERE <nome_da_coluna> <operador> <valor>;

-- várias restrições
WHERE <nome_da_coluna> <operador> <valor> AND/OR <nome_da_coluna> <operador> <valor> ... ;
```
&nbsp;


### Exemplos:

```sql
SELECT nome FROM funcionarios;
SELECT nome, cpf FROM funcionarios;
SELECT * FROM funcionarios;
SELECT * FROM funcionarios WHERE cpf = '123';
SELECT * FROM funcionarios WHERE cpf != '123';
SELECT * FROM funcionarios WHERE dt_nasc > '2005-01-01' OR dt_nasc < '1958-01-01' ORDER BY nome;
```

&nbsp;

## U - Update
É usado para atualizar tabelas ou valores no banco de dados

Para atualizar valores, utilizamos a sintaxe:

```sql
-- Uma única coluna 
UPDATE <nome_da_tabela> SET <nome_da_coluna> = <valor> <restrições>;

-- Uma única coluna 
UPDATE <nome_da_tabela> SET <nome_da_coluna> = <valor>, <nome_da_coluna> = <valor> <restrições>;
```

As restrições são iguais à do select.

&nbsp;

### Exemplos
```sql
UPDATE funcionarios SET cod_supervisor = 4 WHERE cod = 2

-- Vamos atualizar o gerente do departamento financeiro para incluir o Lucas como gerente.
UPDATE departamentos SET cod_gerente = 4

-- Lembrar de incluir as restrições SEMPRE!!!!!

-- Primeiro vamos desfazer essa alteração
UPDATE departamentos SET cod_gerente = 0
```

&nbsp;

Reparem que foi possível fazer o update do cod_gerente mesmo sem definir a data de início do gerente. Esses dois campos deveriam ser atualizados simultaneamente.

Para que isso aconteça, precisamos adicionar uma restrição na tabela departamentos, usando o comando **ALTER TABLE** conforme a sintaxe abaixo:

```sql
ALTER TABLE <nome_da_tabela> <operacao>;
```

```sql
ALTER TABLE departamentos ADD CONSTRAINT departamentos_check CHECK ((cod_gerente IS NULL AND dt_ini_gerente IS NULL) OR (cod_gerente IS NOT NULL AND dt_ini_gerente IS NOT NULL));
```

Agora não conseguimos mais fazer essa atualização.

```sql
-- Sem data de início do gerente.
UPDATE departamentos SET cod_gerente = 4 WHERE cod = 2

-- Com data de início do gerente.
UPDATE departamentos SET cod_gerente = 4, dt_ini_gerente = '2004-11-15' where cod = 3
```
&nbsp;

## D - Delete
É usado para remover valores no banco de dados

Sua sintaxe é:

```sql
DELETE FROM <nome_da_tabela> <restrições>;
```

As restrições são iguais à do select.

&nbsp;

### Exemplos
```sql
DELETE FROM funcionarios WHERE cod = 5;
```
----

&nbsp;

Como vocês podem ter visto, nós definimos alguns tipos de dados (como character varying, integer, date, etc)

Mas como eu sei qual é o melhor tipo pra armazenar no banco de dados? Uso integer? big int? small int? O que é o numeric, e por ai vai.

Nesse caso, acessem esse endereço aqui embaixo, que vai ter os tipos suportados atualmente no postgres 15

> https://www.postgresql.org/docs/current/datatype.html

&nbsp;


# Exercício em aula

## Exercício 1

Finalizar o modelo físico criando as demais tabelas e inserir/modificar registros:

    - 10 ou + funcionários (5 funcionários que tenham 2 dependentes ou mais)
    - 5 departamentos (2 deles com 2 localizações diferentes, os demais com 1 localização só)
    - 8 projetos

    - Atualizar 3 dos registros diferentes
    - Remover 2 registros de funcionários
&nbsp;

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.