#  SQL

Bom, existem quatro categorias de comandos de SQL, que vamos ver em maior ou menor grau hoje e nas próximas aulas.

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

Tem a linguagem de controle dos dados (em inglês, DCL), que são os comandos utilizados para controlar o acesso ao banco de dados. A DCL inclui os comandos GRANT, REVOKE e DENY.

    - GRANT: Usado para dar permissões a um usuário para acessar objetos do banco de dados.

    - REVOKE Usado para remover permissões dadas a um usuário para acessar objetos do banco de dados.

    - DENY: Usado para negar acesso a objetos do banco de dados a um usuário.

&nbsp;

## DQL - Data Query Language

Por fim temos a linguagem de consulta dos dados (em inglês, DQL), que são os comandos utilizados para acessar o banco de dados e recuperar valores. A DQL inclui o comando SELECT.

    - SELECT: Usado para recuperar os dados do banco de dados.

&nbsp;


# CRUD em SQL

CRUD é a sigla em inglês para Create, Read, Update, Delete.

São as principais ações que fazemos no banco de dados SQL quando não somos os administradores do banco.


&nbsp;

## C - Create
É usado tanto para criar tabelas, views e outros objetos do banco quanto para inserir dados.


### Sintaxe
```sql
CREATE TABLE <qualificador> <nome_da_tabela>(
    <nome_da_coluna> <tipo(Date, int, varchar, etc)> <opções (NOT NULL, UNIQUE, DEFAULT, etc)>,
    ...
    ...
);
```

```sql
INSERT INTO <nome_da_tabela> (<nome_das_colunas>) VALUES (<valores>)
```

&nbsp;

### Exemplos:
```sql
CREATE TABLE IF NOT EXISTS alunos
(
    id integer NOT NULL,
    nome character varying(255) NOT NULL,
    data_de_nascimento date NOT NULL,
    turma character varying(15) DEFAULT 'A1'
);
```

&nbsp;


```sql
INSERT INTO alunos (id,nome,data_de_nascimento, turma)
VALUES
 (1, 'João', '2000-12-03', 'B3'),
 (2, 'Maria', '1995-04-03', 'B2'),
 (3, 'Medge', '1998-10-03', 'B3'),
 (4, 'Carla', '2001-03-04', 'B2'),
 (5, 'Aline', '1995-04-02', 'B3'),
 (6, 'João Carlos', '1986-04-03', 'B2'),
 (7, 'Enzo', '2010-10-10', 'B3'),
 (8, 'Augusto', '1978-07-07', 'B2'),
 (9, 'Fernando', '1986-08-09', 'B3'),
 (10, 'Júlia', '2002-06-04', 'B2'),
 (11, 'Karina', '2005-06-04', 'B3'),
 (12, 'Marcos', '1982-05-06', 'B2'),
 (13, 'Sebastião', '1974-03-02', 'B3'),
 (14, 'Maria da silva', '1999-05-01', 'B2'),
 (15, 'Ana', '2002-07-06', 'B3'),
;
```

&nbsp;

## R - Read
É usado para buscar valores no banco de dados

### Sintaxe
```sql
SELECT <nome_das_colunas> FROM <nome_da_tabela> <restrições, junções, agrupamentos, etc>;
```

### Exemplos
```sql
SELECT nome FROM alunos;
SELECT nome, turma FROM alunos;
SELECT * FROM alunos;
SELECT * FROM alunos WHERE turma = 'B2';
SELECT * FROM alunos WHERE turma = 'B2' AND data_de_nascimento > '2000-01-01';
SELECT * FROM alunos WHERE turma = 'B2' OR data_de_nascimento > '2000-01-01';
SELECT * FROM alunos WHERE turma = 'B1' OR data_de_nascimento > '2000-01-01' ORDER BY nome;
```

## U - Update
É usado para atualizar valores no banco de dados

### Sintaxe
```sql
UPDATE <nome_da_tabela> SET <nome_da_coluna> = <valor> <restrições, junções, agrupamentos, etc>;
```

### Exemplos
```sql
UPDATE alunos SET turma = '1A' WHERE id = 1
UPDATE alunos SET turma = '1A' WHERE id = 1 AND nome = 'João'
```

&nbsp;

# D -> "Delete" == Deletar

É usado para remover linhas/registros do banco de dados.

```sql
DELETE FROM <nome_da_tabela> <restrições, junções, agrupamentos, etc>;
```

&nbsp;

### Exemplos
```sql
DELETE FROM alunos WHERE id = 1;
DELETE FROM alunos WHERE id = 1 OR nome = 'João';
```

&nbsp;

Como vocês podem ter visto, nós definimos alguns tipos de dados (como character varying, integer, date, etc)

Mas como eu sei qual é o melhor tipo pra armazenar no banco de dados? Uso integer? big int? small int? O que é o numeric, e por ai vai.

Nesse caso, acessem esse endereço aqui embaixo, que vai ter os tipos suportados atualmente no postgres 15

> https://www.postgresql.org/docs/current/datatype.html

