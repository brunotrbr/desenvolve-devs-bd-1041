## Aula 1
- O que são dados, banco de dados e SGBDs. Onde se encaixa o SGBD dentro da arquitetura de um sistema e como eles são classificados entre relacionais e não-relacionais.

- Quais recursos são oferecidos por um SGBD: Controle de acesso, otimização de consultas, indexação de dados e propriedades ACID.

- Prática com um banco de dados relacional (e.g. Postgres). Instalação, configuração básica e execução de comandos.
  
- Ferramentas para interação com o banco de dados adotado via interface gráfica (e.g. PgAdmin/DBeaver) ou linha de comand (e.g. Psql).

## Aula 2
- Modelagem para um banco de dados relacional utilizando o modelo entidade-relacionamento (MER). Definição de entidade, relacionamento, tipos de atributos e cardinalidade de um relacionamento.

## Aula 3
- Mapeamento do MER (modelo conceitual) para o modelo relacional (modelo lógico). Definição de relações, esquemas, tuplas e atributos.

- Integridade de entidade, suas características e tipos de atributo chave. Integridade referencial, suas características e chaves estrangeiras.

## Aula 4
- Dependência funcional. Normalização de um banco de dados. Vantagens e desvantagens desse processo. Exemplos de banco de dados não normalizados (e.g. Data warehouse).

## Aula 5
- Sintaxe da linguagem SQL e suas principais categorias de comandos: DQL, DDL e DML.

- Comandos DQL para consulta aos dados: SELECT, LIMIT, DISTINCT, ORDER BY e CASE. Operadores AND, OR, IN, IS NULL, IS NOT NULL, LIKE e BETWEEN. Uso de alias (AS) para renomear colunas e tabelas. Sub-consultas utilizando a cláusula WITH.
  
- Utilizando funções prontas: CURRENT_DATE, CURRENT_TIME e NOW. Utilizando funções de formatação de dados: ROUND, DATE_PART, DATE_TRUNC, CONCAT, TRIM, LOWER, UPPER, SUBSTRING, POSITION e REPLACE.

## Aula 6
- Comandos DDL para criação de banco de dados, tabelas, índices e visões: CREATE DATABASE, CREATE TABLE simples, CREATE TABLE com SELECT, CREATE INDEX, CREATE VIEW e CREATE MATERIALIZED VIEW. Definição de CONSTRAINTS, PRIMARY KEY e FOREIGN KEY simples e compostas.

- Comandos DDL para alteração e remoção de tabelas e visões: ALTER TABLE, DROP TABLE, DROP VIEW e REFRESH MATERIALIZED VIEW. Implicações da integridade referencial na alteração de tabelas. Uso das cláusulas ON DELETE e ON UPDATE CASCADE.

## Aula 7
- Comandos DML para inserção, alteração e remoção de dados. INSERT INTO VALUES, INSERT INTO SELECT, UPDATE e DELETE.

- Exportando dados do banco de dados para um arquivo por meio do comando COPY TO. Importando dados de arquivos com o comando COPY FROM.

## Aula 8
- Agrupamento de dados utilizando GROUP BY e funções de agregadoras: MAX, AVG, SUM, COUNT, MIN e MAX. Diferenças entre as cláusulas WHERE e HAVING.

- Junção de tabelas e o produto cartesiano das tuplas. CROSS JOIN, INNER JOIN, RIGHT JOIN, LEFT JOIN, FULL JOIN e SELF JOIN. Junção de tabelas e a união dos dados. UNION e UNION ALL.

## Aula 9
- Avaliação por rúbrica e apresentação do projeto.