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