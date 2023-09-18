## Exercício 1 (da aula 06)

# Exercícios

## Exercício 1

Dada a tabela abaixo,

```sql
CREATE TABLE filmes
(
    titulo character varying(250) NOT NULL,
    ano integer NOT NULL,
    diretor character varying(100) NOT NULL,
    genero character varying(20) NOT NULL,
    atores_principais character varying(1000) NOT NULL,
    duracao_minutos numeric(4) NOT NULL,
    valor_ingresso numeric(5, 2) NOT NULL,
    CONSTRAINT pk PRIMARY KEY (titulo),
    CONSTRAINT check_year CHECK (ano >= 1900 and ano <= 2200)
);
```


Execute os seguintes inserts (e pode adicionar outros seus também, para complementar)

```sql
insert into filmes (titulo, ano, diretor, genero, atores_principais, duracao_minutos, valor_ingresso) -- somente para especificar quais campos sao inseridos
values('Cosmopolis',2012,'David Cronenberg','Drama','Robert Pattinson, Juliette Binoche, Sarah Gadon, Mathieu Amalric',108,22.99);

insert into filmes
values('The Awakening',2012,'Nick Murphy ','Horror','Rebecca Hall, Dominic West, Imelda Staunton, Lucy Cohu',107,29.99);

insert into filmes
values('The Shawshank Redemption',1994,'Frank Darabont','Drama,Crime','Tim Robbins, Morgan Freeman and Bob Gunton',142,25.99);

insert into filmes
values('Pulp Fiction',1994,'Quentin Tarantino','Crime,Thriller','John Travolta, Uma Thurman and Samuel L. Jackson',154,29.99);

insert into filmes
values('One Flew Over the Cuckoos Nest',1975,'Milos Forman','Drama','Jack Nicholson, Louise Fletcher and Michael Berryman',133,55.99);

insert into filmes
values('Inception',2010,'Christopher Nolan','Action','Leonardo DiCaprio, Joseph Gordon-Levitt and Ellen Page',148,79.99);

insert into filmes
values('Fight Club',1999,'David Fincher','Drama','Brad Pitt, Edward Norton and Helena Bonham Carter',139,75.99);

insert into filmes
values('Casablanca',1942,'Michael Curtiz','Drama','Humphrey Bogart, Ingrid Bergman and Paul Henreid',102,62.99);

insert into filmes
values('The Matrix',1999,'Andy Wachowski, Lana Wachowski','Action','Keanu Reeves, Laurence Fishburne and Carrie-Anne',136,28.99);

insert into filmes
values('Se7en',1995,'David Fincher','Crime','Morgan Freeman, Brad Pitt and Kevin Spacey',127,42.99);
```

Escreva comandos SELECT para os itens abaixo:

a) o título, o ano e o diretor de todos os filmes.

b) os filmes de terror de 2010.

c) o título e o ano dos filmes com duração maior do que 2 horas.

d) o título e a duração das comédias lançadas na década de 90 com pelo menos 1 hora e 20 minutos de duração, dos diretores cujos nomes começam pela letra ‘J’. Pesquise sobre o operador LIKE.

e) o título, o gênero e o valor do ingresso dos filmes a partir de 2006, mostrando os valores inflacionados em 8,63%.

f) a quantidade de filmes de ação com ingressos que custam mais do que R$ 20,00.

g) os nomes de todos os diretores cadastrados, sem repetir, e em ordem alfabética.

&nbsp;

Escreva comandos UPDATE para os itens abaixo:

a) aumentar em 10 minutos a duração dos filmes em que participa a atriz Angelina Jolie.

b) dar um desconto de 10% para os filmes de ação do ano 2011.

c) acrescentar um asterisco (*) no final dos títulos dos filmes com duração menor ou igual a 30 minutos. Use o operador || para concatenar strings.

&nbsp;

Escreva comandos DELETE para os itens abaixo:

a) excluir os filmes com valor de ingresso superior a R$ 60,00

b) excluir os filmes em cujo título aparece a palavra “assombrado” ou cujo sobrenome do diretor é “Johnson”. Use o operador LIKE para realizar essa questão.

&nbsp;


## Exercício 2 (da aula 7)

Dado o modelo textual/lógico abaixo, escreva os comandos SQL para criar as tabelas, suas restrições e relações quando aplicáveis e insira pelo menos 5 registros em cada uma das tabelas.

    alunos(nome, numero_aluno, tipo_aluno, curso)

    disciplinas(nome_disciplina, numero_disciplina, creditos, departamento)

    turmas(identificacao_turma, numero_disciplina, semestre, ano, professor)

    pre_requisitos(numero_disciplina, numero_pre_requisito)

    historico_escolar(numero_aluno, identificacao_turma, nota)

Feito, isso, execute o comando SQL abaixo, para inserir mais registros

```sql
INSERT INTO alunos
(nome, numero_aluno, tipo_aluno, curso)
VALUES('Silva', 17, 1, 'CC');

INSERT INTO alunos
(nome, numero_aluno, tipo_aluno, curso)
VALUES('Braga', 8, 2, 'CC');

INSERT INTO disciplinas
(numero_disciplina, creditos, departamento, nome_disciplina)
VALUES('CC1310', 4, 'CC', 'Introd. à ciência da computação');

INSERT INTO disciplinas
(numero_disciplina, creditos, departamento, nome_disciplina)
VALUES('CC3320', 4, 'CC', 'Estruturas de dados');

INSERT INTO disciplinas
(numero_disciplina, creditos, departamento, nome_disciplina)
VALUES('MAT2410', 3, 'MAT', 'Matemática discreta');

INSERT INTO disciplinas
(numero_disciplina, creditos, departamento, nome_disciplina)
VALUES('CC3380', 3, 'CC', 'Banco de dados');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(85, 'MAT2410', 'Segundo', 2007, 'Kleber');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(92, 'CC1310', 'Segundo', 2007, 'Anderson');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(102, 'CC3320', 'Primeiro', 2008, 'Carlos');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(112, 'MAT2410', 'Segundo', 2008, 'Chang');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(119, 'CC1310', 'Segundo', 2008, 'Anderson');

INSERT INTO turmas
(identificacao_turma, numero_disciplina, semestre, ano, professor)
VALUES(135, 'CC3380', 'Segundo', 2008, 'Santos');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(17, 112, 'B');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(17, 119, 'C');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(8, 85, 'A');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(8, 92, 'A');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(8, 102, 'B');

INSERT INTO historicos_escolares
(numero_aluno, identificacao_turma, nota)
VALUES(8, 135, 'A');

INSERT INTO pre_requisitos
(numero_disciplina, numero_pre_requisito)
VALUES('CC3380', 'CC3320');

INSERT INTO pre_requisitos
(numero_disciplina, numero_pre_requisito)
VALUES('CC3380', 'MAT2410');

INSERT INTO pre_requisitos
(numero_disciplina, numero_pre_requisito)
VALUES('CC3320', 'CC1310');
```

Executar as seguintes consultas:

- Recuperar uma lista de todas as disciplinas e notas de Silva.
- Listar os nomes dos alunos que realizaram a disciplina Banco de dados oferecida no segundo semestre de 2008 e suas notas nessa turma.
- Listar os pré-requisitos do curso de Banco de dados.


Executar as seguintes atualizações no banco de dados

- Alterar o tipo de aluno de Silva para segundo ano.
- Criar outra turma para a disciplina Banco de dados para este semestre.
- Inserir uma nota A para Silva na turma Banco de dados do último semestre.


&nbsp;

## Resposta

```sql
CREATE TABLE alunos (
	nome varchar NULL,
	numero_aluno int NOT NULL,
	tipo_aluno int NULL DEFAULT 1,
	curso varchar NULL,
    CONSTRAINT alunos_pk PRIMARY KEY (numero_aluno)
);

CREATE TABLE disciplinas (
	numero_disciplina varchar NOT NULL,
    nome_disciplina varchar NULL,
	creditos int NULL,
	departamento varchar NULL,
    CONSTRAINT disciplinas_pk PRIMARY KEY (numero_disciplina)
);

CREATE TABLE turmas (
	identificacao_turma int NOT NULL,
	numero_disciplina varchar NOT NULL,
	semestre varchar NULL,
	ano int NULL,
	professor varchar NULL,
	CONSTRAINT turmas_pk PRIMARY KEY (identificacao_turma),
	CONSTRAINT turmas_fk FOREIGN KEY (numero_disciplina) REFERENCES disciplinas(numero_disciplina)
);

CREATE TABLE historicos_escolares (
	numero_aluno int NOT NULL,
	identificacao_turma int NOT NULL,
	nota character NOT NULL,
	CONSTRAINT historicos_escolares_pk PRIMARY KEY (numero_aluno,identificacao_turma),
	CONSTRAINT historicos_escolares_fk FOREIGN KEY (identificacao_turma) REFERENCES turmas(identificacao_turma),
	CONSTRAINT historicos_escolares_fk_1 FOREIGN KEY (numero_aluno) REFERENCES alunos(numero_aluno)
);

CREATE TABLE pre_requisitos (
	numero_disciplina varchar NOT NULL,
	numero_pre_requisito varchar NOT NULL,
	CONSTRAINT pre_requisitos_pk PRIMARY KEY (numero_disciplina,numero_pre_requisito),
	CONSTRAINT pre_requisitos_fk FOREIGN KEY (numero_disciplina) REFERENCES disciplinas(numero_disciplina),
	CONSTRAINT pre_requisitos_fk_1 FOREIGN KEY (numero_pre_requisito) REFERENCES disciplinas(numero_disciplina)
);
```

&nbsp;