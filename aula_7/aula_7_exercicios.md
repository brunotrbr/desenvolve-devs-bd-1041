# Exercícios

## Exercício 1
Encontre o preço médio arredondado com 2 casas decimais dos produtos em cada uma das categorias.
```sql

```
## Exercício 2
Busque todas as informações sobre os produtos que nunca foram comprados (inclusive a descrição da categoria e todos os dados do fornecedor).
```sql

```
## Exercício 3
Encontre os top 5 clientes que mais gastaram dinheiro em compras, exibindo o nome completo e o valor gasto formatado como dinheiro. 

Dica: Formatar como dinheiro pode ser feito assim usando o comando `CAST(xxxxxx AS MONEY)`, como em `SELECT CAST(1000 AS MONEY)`
```sql

```

## Exercício 4

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
-- create tables


--Recuperar uma lista de todas as disciplinas e notas de Silva.


--Listar os nomes dos alunos que realizaram a disciplina Banco de dados oferecida no segundo semestre de 2008 e suas notas nessa turma.

	
--Listar os pré-requisitos do curso de Banco de dados.


--Executar as seguintes atualizações no banco de dados
--Alterar o tipo de aluno de Silva para segundo ano.


--Criar outra turma para a disciplina Banco de dados para este semestre.


--Inserir uma nota A para Silva na turma Banco de dados do último semestre.

```

&nbsp;