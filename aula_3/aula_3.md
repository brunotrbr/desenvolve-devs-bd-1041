# MER: Modelo Entidade Relacionamento

## Identificação de entidades

Identificador:

Conjunto de um ou mais atributos (ou relacionamentos) usados pra distinguir uma ocorrência da entidade das demais ocorrências da mesma entidade.

Casos simples
- único atributo como identificador
- exibido como um círculo preto ou um sublinhado abaixo do nome dele.

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/01_identificador_simples.jpg width=200>

Figura 1: Identificador simples

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/02_identificador_simples.jpg width=100>

Figura 2: Identificador simples com diagrama de classes

&nbsp;

Casos complexos

- Mais de um atributo como identificador. 
    
    Ex: Almoxarifado de uma empresa de ferragens, que armazena o estoque em prateleiras. Existem **n** corredores no almoxarifado, com **m** prateleiras. Para identificar onde está um determinado produto, é necessário saber o número do corredor, e o número da prateleira que está.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/03_identificador_composto.jpg width=200>

Figura 3: Identificador composto

&nbsp;

----

## Identificação de relacionamentos

Normalmente, uma ocorrência de relacionamento diferencia-se das demais do mesmo relacionamento pelas ocorrências de entidades que participam dela.

Ex: Casamento. Em geral, não deveriam existir 2 relacionamentos para o mesmo homem e para a mesma mulher.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/04_identificador_de_relacionamento_1.jpg width=300>

Figura 4: Identificador de relacionamento - casamento

&nbsp;

Contudo, há casos em que para as mesmas ocorrências de entidade podem existir diversas ocorrências de relacionamentos.

Ex: Consulta médica, e o sistema de agendamentos de consultas. Para um determinado médico, e um determinado paciente, pode haver diversas consultas diferentes.

Neste caso, é necessário distinguir uma consulta de outra (ou seja, um relacionamento de outro), e utilizamos os identificadores de relacionamentos para isso.

Na consulta médica, em específico, utilizamos a data/hora da consulta para realizar essa diferenciação.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/04_identificador_de_relacionamento_2.jpg width=300>

Figura 4: Identificador de relacionamento - consulta médica

&nbsp;

## Entidades associativas

Permitem que um relacionamento seja visto como uma entidade, pois "transformamos" o relacionamento em uma entidade.

Vamos supor que seja necessário modificar o diagrama da figura 4 com a adição dos medicamentos prescritos pelo médico na consulta realizada.

Como fazemos isso?

Vamos criar uma nova entidade **medicamento**. Mas com qual entidade devemos relacionar **medicamento**? 

Se relacionarmos com **médico**, temos a informação de qual médico prescreveu qual medicação, mas não temos a informação de para quem ela foi prescrita. Se relacionarmos **medicamento** com **paciente**, não sabemos qual médico prescreveu a medicação.

Nesse caso, queremos relacionar **medicamento** com a **consulta**, ou seja, uma entidade com um relacionamento.

A *entidade associativa* serve para que o relacionamento seja visto também como uma entidade, de forma que agora seja possível associar o relacionamento/entidade a outras entidades.

No diagrama entidade-relacionamento, adicionamos um retângulo em torno do relacionamento, como pode ser visto na imagem abaixo.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/05_entidades_associativas.jpg width=300>

Figura 5: Entidade associativa - consulta médica

&nbsp;

OBS:

Caso não quiséssemos utilizar o conceito de *entidade associativa*, poderíamos transformar **consulta** em uma entidade nova, e associar ela com **medicamento**, conforme pode ser visto abaixo.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/06_alternativa_entidades_associativas.jpg width=300>

Figura 6: Alternativa para entidade associativa - consulta médica

&nbsp;

----

## Generalização e especialização

Propriedades podem ser atribuídas a entidades através do conceito de *generalizações/especializações*. Com elas podemos atribuir propriedades particulares a um subconjunto das ocorrências (*especializadas*) de uma entidade *genérica*.

Para representar generalizações, utilizamos um *triângulo*, conforme mostrado na figura abaixo. Nela expressamos a entidade **cliente**, dividida em dois subconjuntos, as entidades **pessoa física** e **pessoa jurídica**, cada uma com seus atributos próprios.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/07_generalizacao_especializacao.jpg width=300>

Figura 7: Generalização e especialização

&nbsp;

Na generalização/especialização, as entidades especializadas herdam os atributos das genéricas.

Na figura 7, por exemplo, a entidade **pessoa física** possui CIC, sexo, nome e código, sendo os dois últimos atributos da entidade genérica **cliente**.

&nbsp;

----

## Relacionamentos de grau N (ou relacionamentos ternários)

Relacionamentos entre mais de duas entidades são chamamos de *relacionamentos de grau N*.

Ex:

Distribuição de produtos nas cidades da sua região.

Existe o relacionamento chamado **distribuição**, onde participam três entidades: a **cidade** onde o produto vai ser distribuído, o **distribuidor** do produto e **produto** a ser distribuído.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/08_rel_grau_n_distribuicao_1.jpg width=300>

Figura 8: Relacionamentos de grau N - Distribuição

&nbsp;

Com relação a cardinalidade, ela refere-se aos **pares de entidades**, ou seja, dadas as entidades A, B e C participantes do relacionamento R, a cardinalidade máxima de A e B dentro de R indica quantas ocorrências de C podem estar associadas a um par de ocorrências A e B.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/09_rel_grau_n_distribuicao_2.jpg width=300>

Figura 9: Relacionamentos de grau N - Distribuição - cardinalidade

&nbsp;

O "1" próximo ao **distribuidor** indica que para uma determinada cidade, e um determinado produto, temos só e somente só um distribuidor.

O "n" próximo ao **produto** indica que um distribuidor pode distribuir em uma cidade muitos produtos.

O "n" próximo a **cidade** indica que um distribuidor pode distribuir um produto em muitas cidades.

&nbsp;


# Modelo lógico / relacional

## Identificando os componentes de um banco de dados

&nbsp;

### Tabelas

Uma tabela é um conjunto não ordenado de **linhas** (ou **tuplas**). Cada linha é composta por uma série de **campos** (ou **valores de atributos**).

Cada campo é identificado por um **nome de campo** (ou **nome do atributo**), e o conjunto de campos das linhas de uma tabela que possuem o mesmo nome formam uma **coluna**.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/10_tabelas.jpg width=400>

Figura 10: Tabelas

&nbsp;

Observações:

- As linhas de uma tabela **não estão ordenadas**.
- Os valores dos campos de uma tabela possuem somente um valor.

&nbsp;

### Chaves

As *chaves* estabelecem relações entre linhas de tabelas de um banco de dados relacional. 

Os principais tipos de chaves são a chave **primária**, chave **estrangeira** e a chave **alternativa**.

&nbsp;

#### Chave primária

É uma coluna ou uma combinação de colunas cujos valores distinguem uma linha das demais dentro de uma tabela.

Na figura abaixo, podemos identificar a tabela **Dependente** que possui uma **chave primária composta**, com as colunas **CodigoEmp** e **NoDepen**.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/11_chave_primaria_composta.jpg width=400>

Figura 11: Chave primária composta

&nbsp;

#### Chave estrangeira

É uma chave estrangeira é uma coluna ou combinação de colunas cujos valores aparecem necessariamente na chave primária de uma tabela. É o mecanismo que permite a implementação de relacionamentos em um banco de dados relacional.

Nas tabelas abaixo, o **CodigoDepto** é a *chave primária* da tabela **Dept**, e chave estrangeira na tabela **Emp** (Empregados), pois indica o departamento que cada empregado está alocado.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/12_chave_estrangeira.jpg width=400>

Figura 12: Chave estrangeira

&nbsp;

A existência da chave estrangeira impõe algumas restrições que devem ser atendidas ao atualizarmos registros no banco de dados:

- Em inserções de novos registros: Devemos garantir que a chave estrangeira exista na outra tabela, como chave primária.

- Em atualizações de registros existentes: Devemos garantir que a chave estrangeira exista na outra tabela, como chave primária.
  
- Em exclusões de registros existentes: Devemos garantir que na chave estrangeira **não** apareça o valor da chave primária que está sendo excluída.

&nbsp;

Importante:

Uma chave estrangeira pode associar a própria tabela, ou seja, a própria chave primária de sua tabela.

A tabela **Emp** possui como chave primária o código do empregado **CodigoEmp**, e uma coluna indicando quem é o gerente daquele empregado (a coluna **CodigoEmpGerente**). Reparem que o gerente é um empregado existente na própria tabela **Emp**. Ou seja, a chave estrangeira está referenciando a chave primária da própria tabela.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/13_chave_estrangeira_mesma_tabela.jpg width=400>

Figura 13: Chave estrangeira na mesma tabela

&nbsp;

#### Chave candidata e chave alternativa 

Quando temos, em uma tabela, mais de uma coluna ou combinações de colunas que podem servir para distinguir uma linha das demais, surge a questão de que critério devemos usar para determinar a chave primária. A estas colunas, ou combinações de colunas, damos o nome de **chaves candidatas**.

Na tabela **Emp** abaixo, tanto o código do empregado quanto o CIC podem ser utilizados como chave primária.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-3/conteudo/14_chave_candidata_alternativa.jpg width=400>

Figura 14: Chave candidata e chave alternativa

&nbsp;

Na figura 14 optou-se por definir o **CodigoEmp** como chave primária e **CIC** como chave alternativa, pois é mais significativo para o sistema ter o **CodigoEmp** como chave estrangeira do que o **CIC**.

&nbsp;

### Domínios e valores vazios

**Domínio da coluna**, ou **domínio do campo** são o conjunto de valores (alfanumérico, numérico, etc) que os campos da coluna podem assumir.

Colunas **obrigatórias** são aquelas que não são admitidos valores vazios (**null**). 

Colunas que aceitam valores vazios são chamadas de **opcionais**.

&nbsp;

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.