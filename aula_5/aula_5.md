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

Tem a linguagem de manipulação de dados (em inglês, DML), que são os comandos utilizados para manipular os dados armazenados no banco de dados. A DML inclui os comandos INSERT, UPDATE e DELETE.
    
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

    funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, numero_matricula_supervisor, num_dpto)
        numero_matricula PK
        cpf UNIQUE
        num_dpto FK referencia departamentos
        numero_matricula_supervisor FK referencia funcionarios

&nbsp;

```sql
CREATE TABLE IF NOT EXISTS public.funcionarios
(
    numero_matricula int not null,
    cpf varchar(11) not null,
    nome varchar(50) not null,
    endereco varchar(100) not null,
    salario numeric not null,
    genero smallint null,
    dt_nasc date not null,
    numero_matricula_supervisor int null,
    --<restrições>
    constraint funcionarios_pk primary key (numero_matricula),
    constraint funcionarios_un unique (cpf),
    constraint funcionarios_fk foreign key(numero_matricula_supervisor) references funcionarios(numero_matricula)
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
create table if not exists departamentos
(
	num int not null,
	nome varchar(50) not null,
	numero_matricula_gerente int null,
	dt_ini_gerente date null,
	constraint departamentos_pk primary key (num),
	constraint departamentos_un unique (nome),
	constraint dpto_func_fk foreign key (numero_matricula_gerente) references funcionarios (numero_matricula)
	
);
```

Agora vamos alterar a tabela **funcionarios**, para incluir o atributo num_dpto. Obs: Alter table é um comando de update, não de create.

```sql
alter table funcionarios add column num_dpto int null;
alter table funcionarios add constraint func_dpto_fk foreign key (num_dpto) references departamentos (num);
```

&nbsp;

Agora podemos começar inserindo os departamentos e os funcionários, usando o comando **INSERT INTO**.

Sua sintaxe é:

```sql
INSERT INTO <nome_da_tabela> (<nome_das_colunas>) VALUES (<valores>)
```

```sql
-- adicionamos o nome das colunas para garantir a ordem dos valores e poder omitir valores anuláveis
insert into departamentos (num, nome) values (1, 'vendas');

-- podemos não inserir as colunas, mas ai temos que inserir todos os valores incluindo os nulos
insert into departamentos values (2, 'desenvolvimento', null, null);
insert into departamentos (num, nome) values (3, 'financeiro');

-- erro por causa da restrição unique
insert into departamentos (num, nome) values (4, 'financeiro');
insert into departamentos (num, nome, numero_matricula_gerente, dt_ini_gerente) values (4, 'Jurídico', null, null);
insert into departamentos (num, nome, numero_matricula_gerente, dt_ini_gerente) values (5, 'Marketing', null, null);
```

&nbsp;

Por que não inserimos o código do gerente e a data de início do gerente?

Porque são opcionais.

&nbsp;

Agora vamos inserir funcionários.

```sql
insert into funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, numero_matricula_supervisor, num_dpto) values 
(1, '12345678900', 'Pedro', 'Avenida um, 55', 2000, 1, '2002-02-21', null, 4),
(2, '15846845786', 'Luciana', 'Avenida dois, 44', 3000, 2, '2002-11-06', null, 3),
(3, '95168752178', 'Ísis', 'Avenida três, 12', 16000, 2, '1995-05-11', null, 2),
(4, '98751264587', 'Lucas', 'Avenida quatro, 65', 2000, 1, '1957-08-11', null, 1),
(5, '12455684543', 'Eduardo', 'Avenida cinco, 555', 5000, 1, '1981-04-29', null, 5),
(6, '98754148689', 'Ramon', 'Avenida cinco, 15', 4800, 1, '1977-06-13', null, 5),
(7, '54545187983', 'Luiza', 'Avenida cinco, 5', 6900, 2, '1990-02-11', null, 4),
(8, '48451684945', 'Paula', 'Avenida cinco, 49', 16000, 2, '1995-07-27', null, 1),
(9, '56484218546', 'Marcos', 'Avenida cinco, 18', 5810, 1, '1999-12-13', null, 1),
(10, '78218840054', 'Francesca', 'Avenida cinco, 66', 16000, 2, '1988-03-28', null, 3),
(11, '00584984895', 'Marcelo', 'Avenida cinco, 47', 4100, 1, '1976-01-29', null, 3),
(12, '05808843815', 'Flávia', 'Avenida cinco, 128', 2158, 2, '1999-12-13', null, 2),
(13, '56890548054', 'Íris', 'Avenida cinco, 654', 16000, 2, '1987-11-15', null, 4),
(14, '05410048944', 'Ingrid', 'Avenida cinco, 123', 16000, 2, '1991-04-29', null, 5),
(15, '65808498061', 'Daniel', 'Avenida cinco, 789', 3800, 1, '1970-02-10', null, 2)
;
```

&nbsp;

## R - Read
É usado para buscar valores no banco de dados

Sua sintaxe é:

```sql
SELECT <nome_das_colunas> FROM <nome_da_tabela> <restrições, junções, agrupamentos, etc>;

-- para retornar todas as colunas, utilizamos o asterisco "*"
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
-- busca todos os funcionarios, e traz todas as colunas
select * from funcionarios;
-- busca os funcionários que recebem mais do que 4000, e traz as colunas numero_matricula, nome, salario
select numero_matricula, nome, salario from funcionarios where salario > 4000
-- busca os funcionários que recebem menos do que 4000, e traz as colunas numero_matricula, nome, cpf, salario
select numero_matricula, nome, cpf, salario from funcionarios where salario < 4000
-- busca os funcionários com cpf diferente de 98751264587, e traz todas as colunas
select * from funcionarios where cpf <> '98751264587' -- diferente de x
-- busca os funcionários com cpf diferente de 98751264587, e traz todas as colunas
select * from funcionarios where cpf != '98751264587' -- diferente de x
-- busca os funcionários com data de nascimento maior que 2000-01-01 OU menor que 1980-01-01, e traz todas as colunas
select * from funcionarios where dt_nasc > '2000-01-01' or dt_nasc < '1980-01-01'
-- busca os funcionários com data de nascimento maior que 2000-01-01 E menor que 1980-01-01, e traz todas as colunas
select * from funcionarios where dt_nasc > '2000-01-01' and dt_nasc < '1980-01-01'
-- busca os funcionários com genero igual a 1 (masculino) E salario maior que 6000, e traz todas as colunas
select * from funcionarios where genero = 1 and salario > 6000
```

&nbsp;

## U - Update
É usado para atualizar tabelas ou valores no banco de dados

Para atualizar valores, utilizamos a sintaxe:

```sql
-- Uma única coluna 
UPDATE <nome_da_tabela> SET <nome_da_coluna> = <valor> <restrições>;

-- Várias colunas
UPDATE <nome_da_tabela> SET <nome_da_coluna> = <valor>, <nome_da_coluna> = <valor> <restrições>;
```

As restrições são iguais à do select.

&nbsp;

### Exemplos
```sql
-- O ideal é utilizar o CPF ou o numero_matricula
-- Caso tivesse duas Lucianas, as duas receberiam na coluna numero_matricula_supervisor o numero 10
update funcionarios set numero_matricula_supervisor = 10 where nome = 'Luciana';

-- Update correto do comando acima
update funcionarios set numero_matricula_supervisor = 10 where numero_matricula = 2

-- Para controlar as transações, usamos o begin/commit/rollback
-- BEGIN
-- ALTERAÇÕES DO BANCO
-- COMMIT OU ROLLBACK, um dos dois

-- -- Relação direta com as propriedades acid (atomicidade, consistencia, isolamento, durabilidade)
-- begin; -- inicia a transação
-- update funcionarios set numero_matricula_supervisor = null; -- update normal, insert, delete, etc (operações de modificação, o select não conta)
-- commit; -- caso tudo esteja certo, finaliza a transação e grava todas as alterações definitivamente no banco
-- -- OU
-- rollback; -- caso esteja errado, cancela todas as alterações e volta o banco de dados para o último estado válido e consistente

update departamentos set nome = 'Comercial' where num = 1;
update departamentos set nome = 'Pesquisa e Desenvolvimento' where num = 2;
update departamentos set nome = 'Financeiro' where num = 3;

-- atualiza numero_matricula_gerente no departamento de numero 2
update departamentos set numero_matricula_gerente = 3 where num = 2
```

&nbsp;

Reparem que foi possível fazer o update do cod_gerente mesmo sem definir a data de início do gerente. Esses dois campos deveriam ser atualizados simultaneamente.

Para que isso aconteça, precisamos adicionar uma restrição na tabela departamentos, usando o comando **ALTER TABLE** conforme a sintaxe abaixo (dica: check):

```sql
ALTER TABLE <nome_da_tabela> <operacao>;
```

```sql
-- adiciona a restrição para que ambos os campos sejam nulos ou ambos sejam preenchidos

-- primeiro zeramos o numero_matricula_gerente
update departamentos set numero_matricula_gerente = 3 where num = 2

-- aplicamos a restrição
alter table departamentos add constraint departamentos_check CHECK (
	(numero_matricula_gerente is null and dt_ini_gerente is null)
	or 
	(numero_matricula_gerente is not null and dt_ini_gerente is not null)
);

-- agora não conseguimos mais fazer essa atualização.
update departamentos set numero_matricula_gerente = null where num = 2

-- precisamos alteramos as duas coisas juntas
UPDATE departamentos SET numero_matricula_gerente = 3, dt_ini_gerente = '2004-11-15' where num = 2;
UPDATE departamentos SET numero_matricula_gerente = 8, dt_ini_gerente = '2004-11-15' where num = 1;
UPDATE departamentos SET numero_matricula_gerente = 10, dt_ini_gerente = '2004-11-15' where num = 3;
UPDATE departamentos SET numero_matricula_gerente = 13, dt_ini_gerente = '2004-11-15' where num = 4;
UPDATE departamentos SET numero_matricula_gerente = 14, dt_ini_gerente = '2004-11-15' where num = 5;
```

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
delete from funcionarios where numero_matricula = 15;
```

&nbsp;

Adicionar e remover colunas na tabela

```sql
-- adiciona a coluna "apagavel" na tabela de funcionarios
alter table funcionarios add column apagavel int null;

-- remover a coluna "apagavel"
alter table funcionarios drop column apagavel;
```

&nbsp;

Como vocês podem ter visto, nós definimos alguns tipos de dados (como character varying, integer, date, etc)

Mas como eu sei qual é o melhor tipo pra armazenar no banco de dados? Uso integer? big int? small int? O que é o numeric, e por ai vai.

Nesse caso, acessem esse endereço aqui embaixo, que vai ter os tipos suportados atualmente na versão corrente do PostgreSQL.

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