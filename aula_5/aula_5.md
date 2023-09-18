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


&nbsp;


Vamos criar outras tabelas para demonstrar mais comandos

```sql
-- Criar tabela
CREATE TABLE PUBLIC.tabela_um (
    id INTEGER NOT NULL PRIMARY KEY,
    nome character varying(60)
);

-- Criar tabela se não existe
CREATE TABLE IF NOT EXISTS PUBLIC.tabela_dois
(
    id integer NOT NULL,
    nome character varying(60), 
    tab_um_id integer,
    CONSTRAINT pk_tab_dois PRIMARY KEY (id)
);

-- Criar tabela
CREATE TABLE PUBLIC.tabela_tres (
    id INTEGER NOT NULL,
    nome character varying(60), 
    PRIMARY KEY (id)
);

-- Cria a chave estrangeira que referencia a coluna "tab_um_id" para a coluna "id" da tabela_um. No update da tabela_um a alteração vai ocorrer em cascata para as linhas relacionadas na outra tabela. No delete, a ação vai setar como null os registros da tabela_dois relacionados à linha removida da tabela_um
-- Indica que a restrição ainda não foi validada, ou seja, os dados na tabela podem ainda não coincidir/corresponder à restrição imposta.
ALTER TABLE IF EXISTS public.tabela_dois
    ADD CONSTRAINT fk_tab_um_id_id FOREIGN KEY (tab_um_id)
    REFERENCES public.tabela_um (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE SET NULL
    NOT VALID;

-- Cria a chave estrangeira que referencia a coluna "id" da tabela_tres para a coluna "id" da tabela_quatro. O update vai falhar posi tem linhas relacionadas entre as tabelas tres e quatro. No delete, a ação vai setar como null os registros da tabela_dois relacionados à linha removida da tabela_um
ALTER TABLE IF EXISTS public.tabela_dois
    ADD CONSTRAINT fk_tab_tres_id_id FOREIGN KEY (id)
    REFERENCES public.tabela_tres (id) MATCH SIMPLE
    ON UPDATE RESTRICT
    ON DELETE NO ACTION
    NOT VALID;



-- Os tipos de restrições aplicadas às chaves estrangeiras são:
--  No action: Não realiza nenhuma operação na coluna relacionada
--  Restrict: Previne que um update/delete seja feito caso tenha colunas relacionadas
--  Cascade: Propaga um efeito em cascata nas colunas relacionadas
--  Set null: Seta como null os valores das colunas relacionadas à que foi modificada/excluída
--  Set default: Seta com valor default ('', 0, false, etc) os valores das colunas relacionadas à que foi modificada/excluída



-- Alter table, trocando o nome de tabela_dois para tabela_quatro
ALTER TABLE IF EXISTS tabela_dois
    RENAME TO tabela_quatro;

-- Insert 
INSERT INTO tabela_um VALUES (1,'1');
INSERT INTO tabela_um VALUES (2,'2');
INSERT INTO tabela_um VALUES (3,'3');

INSERT INTO tabela_tres VALUES (1,'1');
INSERT INTO tabela_tres VALUES (2,'2');
INSERT INTO tabela_tres VALUES (3,'3');
INSERT INTO tabela_tres VALUES (4,'4');
INSERT INTO tabela_tres VALUES (5,'5');
INSERT INTO tabela_tres VALUES (6,'6');

INSERT INTO tabela_quatro VALUES (1,'1', 1);
INSERT INTO tabela_quatro VALUES (2,'2', 1);
INSERT INTO tabela_quatro VALUES (3,'3', 2);
INSERT INTO tabela_quatro VALUES (4,'4', 2);
INSERT INTO tabela_quatro VALUES (5,'5', 3);
INSERT INTO tabela_quatro VALUES (6,'6', 3);

-- Lista os valores atuais da tabela quatro
select * from tabela_quatro;

-- Altera o valor do ID da tabela um (update cascade)
update tabela_um set id = 95 where id = 3;

-- Lista novamente os valores atuais da tabela quatro
select * from tabela_quatro;
-- OBS: O update cascade deve ser utilizado com muito cuidado, pois dependendo da quantidade de tabelas relacionadas ele pode realizar o update de uma grande quantidade de registros.

-- Realiza o delete de uma das linhas da tabela um (delete set null)
delete from tabela_um where id = 1;

-- Como existe a restrição on delete set null, na tabela quatro as linhas relacionadas com tabela_um.id = 1 são atualizadas e recebem o valor NULL
select * from tabela_quatro;

-- Update da tabela tres falha pois existe uma linha da tabela_quatro que se relacionada com o id=3 da tabela_tres
update tabela_tres set id=99 where id=3;

-- Delete da tabela tres funciona pois definimos como no action no delete
delete from tabela_tres where id=3;

-- Conferencia de valores
select * from tabela_tres;

-- Drop tabela falha por causa dos dados relacionados (FK)
DROP TABLE tabela_um;

-- Drop tabela em cascata
DROP TABLE tabela_um cascade;

-- Apagar todos os dados restantes da tabela_tres com delete
select * from tabela_tres;
delete from tabela_tres;

-- Apagar todos os dados restantes da tabela_quatro com truncate
TRUNCATE TABLE tabela_quatro;

-- Delete sem where percorre a tabela e apaga todos os dados.
-- Truncate apaga todos os dados sem percorrer a tabela. É mais rápido e libera espaço imediatamente no banco. De acordo com a documentação não deve ser possível dar rollback ao apagar os dados com truncate.

-- Limpa o restante do banco de dados
DROP TABLE tabela_tres, tabela_quatro;
```


Para o próximo comando, vamos criar uma nova tabela
```sql
CREATE TABLE contas (
	id serial PRIMARY KEY,
	usuario VARCHAR ( 50 ) UNIQUE NOT NULL,
	senha VARCHAR ( 50 ) NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	criado_em TIMESTAMP NOT NULL,
  ultimo_login TIMESTAMP,
  CONSTRAINT senha_fraca CHECK (senha <> '123456') NOT VALID
);
```

Onde:
- NOT NULL define que o atributo não pode ser nulo/vazio
- UNIQUE garante que o valor inserido no banco de dados é único para aquela tabela
- CHECK verifica uma condição booleana antes de realizar a operação
- FOREIGN KEY define a chave estrangeira das tabelas


Vamos inserir alguns registros na tabela Contas, criada anteriormente, para demonstrar nosso próximo comando
```sql
INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('johndoe', 'password123', 'johndoe@example.com', now(), now());

INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('janedoe', 'pa$$word456', 'janedoe@example.com', now(), null);

INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('bobsmith', 'abc123', 'bobsmith@example.com', now(), now());

INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('maryjane', 'mary123', 'maryjane@example.com', now(), null);

INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('johncena', 'youcantseeme', 'johncena@example.com', now(), null);

-- Tenta inserir com senha fraca, e da erro
INSERT INTO contas (usuario, senha, email, criado_em, ultimo_login) 
VALUES ('senha_fraca', '123456', 'senha_fraca@example.com', now(), null);

-- Alter table vai falhar porque já existe uma senha chamada 'youcantseeme'
ALTER TABLE IF EXISTS public.contas
    ADD CONSTRAINT senha_diferente_de_youcantseeme CHECK (senha <> 'youcantseeme');


-- Create table a partir de um select, registrando em uma nova tabela a conta, quando foi criada e o último login
CREATE TABLE contas_acessos AS
SELECT usuario, criado_em, ultimo_login
FROM contas
WHERE usuario = 'bobsmith';

-- Podemos utilizar o create table a partir do select para:
-- Simplificar queries complexas: As vezes, temos uma query complexa que envolve join entre multiplas tabelas ou que realiza muitas agregações de dados. Criando uma nova tabela a partir do resultado dessa query, podemos simplificar queries subsequentes, tratando essa tabela como uma única entidade.

-- Salvar o resultado de queries: Se temos uma query que frequentemente retorna uma grande quantidade de dados, podemos salvar esse resultado para ter acesso fácil a ele posteriormente.

-- Sumarizar dados: As vezes temos um dataset muito grande, e queremos sumarizar ele de alguma forma que possa ser aproveitado no nosso trabalho (agrupado por certos critérios, calculando médias, etc). Utilizamos esse select para gerar os dados e salvar na nova tabela o resultado.

-- Filtrar dados: As vezes podemos querer criar uma nova tabela que contenha somente um subconjunto específico de dados existentes na tabela, permitindo que as próximas queries tenham um desempenho melhor.
```
