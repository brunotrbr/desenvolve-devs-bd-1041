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
INSERT INTO filmes (titulo, ano, diretor, genero, atores_principais, duracao_minutos, valor_ingresso)
VALUES
    ('A Origem', 2010, 'Christopher Nolan', 'Ficção Científica', 'Leonardo DiCaprio, Joseph Gordon-Levitt', 148, 25.50),
    ('Titanic', 1997, 'James Cameron', 'Romance', 'Leonardo DiCaprio, Kate Winslet', 195, 27.90),
    ('O Poderoso Chefão', 1972, 'Francis Ford Coppola', 'Crime', 'Marlon Brando, Al Pacino', 175, 24.99),
    ('Star Wars: Episódio IV - Uma Nova Esperança', 1977, 'George Lucas', 'Ficção Científica', 'Mark Hamill, Harrison Ford', 121, 26.25),
    ('Star Wars: Episódio V - O Império Contra-Ataca', 1980, 'Irvin Kershner', 'Ficção Científica', 'Mark Hamill, Harrison Ford', 124, 27.50),
    ('Star Wars: Episódio VI - O Retorno de Jedi', 1983, 'Richard Marquand', 'Ficção Científica', 'Mark Hamill, Harrison Ford', 131, 28.75),
    ('Star Wars: Episódio I - A Ameaça Fantasma', 1999, 'George Lucas', 'Ficção Científica', 'Liam Neeson, Ewan McGregor', 136, 25.99),
    ('Star Wars: Episódio II - O Ataque dos Clones', 2002, 'George Lucas', 'Ficção Científica', 'Hayden Christensen, Natalie Portman', 142, 27.99),
    ('Star Wars: Episódio III - A Vingança dos Sith', 2005, 'George Lucas', 'Ficção Científica', 'Hayden Christensen, Ewan McGregor', 140, 29.50),
    ('Star Wars: Episódio VII - O Despertar da Força', 2015, 'J.J. Abrams', 'Ficção Científica', 'Daisy Ridley, John Boyega', 135, 30.25),
    ('Star Wars: Episódio VIII - Os Últimos Jedi', 2017, 'Rian Johnson', 'Ficção Científica', 'Daisy Ridley, Mark Hamill', 152, 31.50),
    ('Star Wars: Episódio IX - A Ascensão Skywalker', 2019, 'J.J. Abrams', 'Ficção Científica', 'Daisy Ridley, Adam Driver', 142, 32.75),
    ('Cidade de Deus', 2002, 'Fernando Meirelles, Kátia Lund', 'Drama', 'Alexandre Rodrigues, Leandro Firmino', 130, 21.75),
    ('Os Incríveis', 2004, 'Brad Bird', 'Animação', 'Craig T. Nelson, Holly Hunter', 115, 18.99),
    ('Avatar', 2009, 'James Cameron', 'Ficção Científica', 'Sam Worthington, Zoë Saldana', 162, 26.99),
    ('Cosmopolis',2012,'David Cronenberg','Drama','Robert Pattinson, Juliette Binoche, Sarah Gadon, Mathieu Amalric',108,22.99),
    ('Pulp Fiction',1994,'Quentin Tarantino','Crime,Thriller','John Travolta, Uma Thurman and Samuel L. Jackson',154,29.99),
    ('O Grande Lebowski', 1998, 'Joel Coen', 'Comédia', 'Jeff Bridges, John Goodman', 117, 21.75),
    ('Os Suspeitos', 1995, 'Bryan Singer', 'Crime', 'Kevin Spacey, Gabriel Byrne', 106, 22.50),
    ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 'Peter Jackson', 'Fantasia', 'Elijah Wood, Ian McKellen', 178, 29.99),
    ('O Senhor dos Anéis: As Duas Torres', 2002, 'Peter Jackson', 'Fantasia', 'Elijah Wood, Ian McKellen', 179, 28.99),
    ('O Senhor dos Anéis: O Retorno do Rei', 2003, 'Peter Jackson', 'Fantasia', 'Elijah Wood, Ian McKellen', 201, 30.50),
    ('O Resgate do Soldado Ryan', 1998, 'Steven Spielberg', 'Drama', 'Tom Hanks, Matt Damon', 169, 26.75),
    ('Clube da Luta',1999,'David Fincher','Drama','Brad Pitt, Edward Norton and Helena Bonham Carter',139,75.99),
    ('Casablanca',1942,'Michael Curtiz','Drama','Humphrey Bogart, Ingrid Bergman and Paul Henreid',102,62.99),
    ('Matrix',1999,'Andy Wachowski, Lana Wachowski','Ação','Keanu Reeves, Laurence Fishburne and Carrie-Anne',136,28.99),
    ('Seven',1995,'David Fincher','Crime','Morgan Freeman, Brad Pitt and Kevin Spacey',127,42.99),
    ('Forrest Gump - O Contador de Histórias', 1994, 'Robert Zemeckis', 'Drama', 'Tom Hanks, Robin Wright', 142, 21.50),
    ('Os Bons Companheiros', 1990, 'Martin Scorsese', 'Crime', 'Robert De Niro, Ray Liotta', 146, 23.75),
    ('Jurassic Park: Parque dos Dinossauros', 1993, 'Steven Spielberg', 'Aventura', 'Sam Neill, Laura Dern', 127, 24.99),
    ('O Silêncio dos Inocentes', 1991, 'Jonathan Demme', 'Crime', 'Jodie Foster, Anthony Hopkins', 118, 22.90),
    ('Gladiador', 2000, 'Ridley Scott', 'Ação', 'Russell Crowe, Joaquin Phoenix', 155, 25.99),
    ('Toy Story', 1995, 'John Lasseter', 'Animação', 'Tom Hanks, Tim Allen', 81, 19.75),
    ('O Rei Leão', 1994, 'Roger Allers, Rob Minkoff', 'Animação', 'Matthew Broderick, Jeremy Irons', 89, 20.50),
    ('Harry Potter e a Pedra Filosofal', 2001, 'Chris Columbus', 'Fantasia', 'Daniel Radcliffe, Emma Watson', 152, 26.25),
    ('Esqueceram de Mim', 1990, 'Chris Columbus', 'Comédia', 'Macaulay Culkin, Joe Pesci', 103, 18.50),
    ('Todo Mundo em Pânico', 2000, 'Keenen Ivory Wayans', 'Comédia', 'Anna Faris, Jon Abrahams', 88, 19.75),
    ('Austin Powers: O Agente "Bond" Cama', 1999, 'Jay Roach', 'Comédia', 'Mike Myers, Elizabeth Hurley', 94, 20.25),
    ('Quem Vai Ficar com Mary?', 1998, 'Peter Farrelly, Bobby Farrelly', 'Comédia', 'Ben Stiller, Cameron Diaz', 119, 21.50),
    ('O Sexto Sentido', 1999, 'M. Night Shyamalan', 'Suspense', 'Bruce Willis, Haley Joel Osment', 107, 21.99);
```

Escreva comandos SELECT para os itens abaixo:

a) o título, o ano e o diretor de todos os filmes.

b) os filmes de Crime produzidos a partir de 1992.

c) o título e o ano dos filmes com duração maior do que 2 horas.

d) o título e a duração das comédias lançadas na década de 90 com pelo menos 1 hora e 20 minutos de duração.

e) o título, o gênero e o valor do ingresso dos filmes a partir de 2006, mostrando os valores inflacionados em 8,63%.

f) a quantidade de filmes de ação com ingressos que custam mais do que R$ 20,00.

g) os nomes de todos os diretores cadastrados, sem repetir, e em ordem alfabética.

&nbsp;

Escreva comandos UPDATE para os itens abaixo:

a) aumentar em 10 minutos a duração dos filmes em que participa a atriz Daisy Ridley.

b) dar um desconto de 10% para os filmes de ação do ano 2011.

c) acrescentar um asterisco (*) no final dos títulos dos filmes com duração menor ou igual a 90 minutos.

&nbsp;

Escreva comandos DELETE para os itens abaixo:

a) excluir os filmes com valor de ingresso superior a R$ 60,00

b) excluir os filmes em cujo título aparece a palavra Star Wars ou cujo sobrenome do diretor é Columbus.

&nbsp;

## Exercício 2

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