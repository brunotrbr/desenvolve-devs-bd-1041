# MER: Modelo Entidade Relacionamento

## Como traduzir requisitos de um problema do mundo real para um modelo conceitual?

Como descrever um banco de dados? Temos um cenário real, mas como podemos modelar isso em um banco de dados utilizável?

&nbsp;

Utilizamos o **Modelo Entidade-Relacionamento (MER)**.

Serve para descrever os conceitos e as restrições básicas dos dados para nossa aplicação.

&nbsp;

> Ex: Cadastro de usuários não pode aceitar CPFs repetidos. O banco de dados usa **chave primária** ou cláusula **unique** para garantir que os valores serão únicos.

&nbsp;

## Modelo Entidade-Relacionamento

Modelo conceitual utilizado para descrever os objetos (**as entidades**), suas características (**os atributos**) e como eles se relacionam entre si (**os relacionamentos**), dado um determinado cenário do mundo real.

&nbsp;

> Obs: Nem sempre precisamos modelar todo o cenário. Podemos ir modelando de acordo com a nossa necessidade.

&nbsp;

### Entidades
Entidade é uma coisa ou pessoa, concreta (física) ou abstrata (lógica), e que pode ser individualmente identificada. 

&nbsp;

Observem a imagem abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/entidades.png width=400>

Figura 1: Entidades

Nela podemos ver:
- *Entidade*: a pessoa que estamos identificando
- *Tipo de entidade*: No processo de descrição, não há interesse em descrever cada entidade individualmente, e sim cada conjunto de elementos comuns a todas as entidades do mesmo tipo (os atributos, as restrições de integridade, etc)
- *Conjunto de entidades*: Coleção de entidades de um mesmo tipo existentes em um dado momento

&nbsp;

**Entidades físicas** são aquelas realmente tangíveis, existentes e visíveis no mundo real.

Ex: Um cliente (uma pessoa, uma empresa, etc).

&nbsp;

**Entidades lógicas** são aquelas que existem em função da interação entre/com entidades físicas, mas não são objetos físicos no mundo real.

Ex: Uma venda realizada em loja.

&nbsp;

Entidades são nomeadas com substativos concretos ou abstratos que representam de forma clara sua função. 

Ex: Cliente, Produto, Venda, Turma.

&nbsp;

As entidades podem ser classificadas de acordo com o motivo de sua existência:

- **Entidades Fortes** são aquelas que existem independente de outras entidades. Ou seja, por si só elas existem. 
  
  Em um sistema de vendas, por exemplo, a entidade **Produto** independe de qualquer outra entidade para existir.

- **Entidades Fracas** são aquelas de dependem de outras entidades para existir pois, individualmente, não fazem sentido existir.
  
  No sistema de vendas, por exemplo, a entidade **Venda** depende da entidade *Produto*, pois não existe uma venda sem itens.

- **Entidades Associativas** são utilizadas para permitir que um relacionamento seja visto como uma entidade. Será visto melhor após explicarmos sobre relacionamentos.

&nbsp;

### Atributos
É uma propriedade ou característica que descreve as entidades, além de restrições destes dados quando aplicáveis.

&nbsp;

Observem a imagem abaixo, novamente:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/entidades.png width=400>

Figura 2: Entidades

A cor da roupa, o sexo, o humor, são exemplos de atributos.

&nbsp;

Entidade **Pessoa**:
- Possui como atributos o **Nome**, a **Idade**, a **Altura** e, pensando no Brasil, um **CPF**.

- Os três primeiros podem ser modificados, enquanto o CPF não pode.
  
- Nesse caso, existe essa restrição de que o CPF não se altera na entidade Pessoa.

&nbsp;

Os atributos podem ser classificados quanto à sua função:

- **Descritivos** representam características intrínsecas de uma entidade, como nome ou cor.
  
- **Nominativos** além de serem descritivos, também tem a função de definir e identificar um objeto, como por exemplo código, número, etc.
  
- **Referenciais** representam a ligação de uma entidade com outra em um relacionamento. Por exemplo, uma venda possui o CPF do cliente, que a relaciona com a entidade **Cliente**.

&nbsp;

Os atributos podem ser classificados quanto ao seu tipo:

- **Simples**: Quando um único atributo define uma característica da entidade. Nome ou Altura são atributos simples.
  
- **Compostos**: Quando são usados vários atributos para definir uma informação da entidade. Endereço, por exemplo, pode ser composto por rua, número, bairro, CEP, etc.

&nbsp;

Os atributos podem ser classificados quanto ao tipo de valor que armazenam:

- **Valor único** são atributos que possui um único valor para uma entidade. A idade, por exemplo, é um atributo de valor único pois, mesmo que se altere, só tem um único valor.
  
- **Multivalorado** são atributos que possuem um conjunto de valores para uma entidade. Uma Pessoa pode ter como atributo **formacao acadêmica**, e esse atributo pode possuir nenhum valor, um valor ou mais de um valor caso a pessoa tenha 2 graduação ou mais, ou pós graduação, etc. Atributos multivalorados podem ter um **limite mínimo** e um **limite máximo** para restringir o número de valores permitidos.

&nbsp;

Dois ou mais valores de atributos podem estar relacionados (Ex: data de nascimento e idade). Nesse caso, os atributos também podem ser classificados quanto a forma de armazenamento:

- **Armazenados**: Quando um atributo possui um valor. Por exemplo, a **Data de Nascimento** de uma pessoa.
  
- **Derivados**: Quando seus valores são derivados de outros atributos. O atributo **Idade** de uma pessoa pode ser derivado do atributo **Data de Nascimento** por exemplo.

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/entidades_e_atributos.png width=450>

Figura 2: Entidades e Atributos

&nbsp;

#### Chave primária

Um atributo que identifica uma determinada entidade de forma única, ou seja, sem ambiguidade, é chamado de **Chave Primária**.

Por esse motivo a chave primária de uma entidade é única, e não se repete.

&nbsp;

#### Chave estrangeira

Os atributos referenciais são chamados de **Chave Estrangeira**, e normalmente estão ligados à **chave primária** da outra entidade. Eles servem para identificar, na entidade B, a chave primária da entidade A.

Observem a imagem abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/chave_primaria_e_estrangeira.jpg width=400>

Figura 3: Chave primária e estrangeira

&nbsp;

Temos a tabela Pessoa (entidade), a tabela Automóvel (entidade) e a tabela Propriedade (relacionamento).

Na tabela **Pessoa**, o atributo *Identidade* é uma **chave primária**.

Na tabela **Automóvel**, o atributo *Placa* é uma **chave primária**.

Na tabela **Propriedade**, juntamos a *chave primária Placa* e a *chave primária Identidade*, para compor a chave primária da tabela Propriedade.

Mudando a perspectiva para a tabela **Propriedade**, Placa e Identidade são chaves estrangeiras, pois vieram de outras tabelas (onde são chaves primárias).

Os dois campos em conjunto são a chave primária da tabela Propriedade, então **não pode** ter duas linhas na tabela com os valores **A1/P1** ou **A2/P2**, por exemplo.

&nbsp;

### Relacionamentos

Relacionamentos são uma correspondência entre 2 ou mais entidades, não necessariamente distintas. Cada entidade desempenha um papel no relacionamento.

&nbsp;

Considerem a frase abaixo:

> João trabalha na universidade PUCRS.

Ela poderia ser reescrita como:

> A universidade PUCRS emprega o João.

Neste caso, as entidades são: 

> João e PUCRS

E os papéis são:

> João: empregado
>
> PUCRS: empregador

&nbsp;

A imagem abaixo poderia representar o relacionamento entre o João e a PUCRS, por exemplo.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/relacionamentos.png width=300>

Figura 5: Relacionamentos

&nbsp;

#### Cardinalidade
Aponta a quantidade mínima e a quantidade máxima de objetos envolvidos em cada lado do relacionamento. É a *restrição de integridade* dos relacionamentos, e **obrigatoriamente** deve ser incluída na modelagem. Possui valor mínimo e valor máximo (0, 1 ou n).

Os relacionamentos podem ser classificados de três formas, de acordo com a Cardinalidade:

- **1..1 (um para um)** onde cada uma das entidades envolvidas referenciam obrigatoriamente apenas uma unidade da outra. 
  
  Em um banco de dados de currículos, por exemplo, cada candidato pode ter somente um currículo na base. Ao mesmo tempo, cada currículo pertence a um único usuário cadastrado.
  
- **1..n ou 1..\* (um para muitos)** onde uma das entidades pode referenciar várias unidades da outra, porem do outro lado cada uma das várias unidades referenciadas só podem estar ligadas em uma única unidade da outra entidade. 
  
  Em um sistema de plano de saúde, um usuário pode ter vários dependentes, mas cada dependente pode estar ligado a somente um usuário principal.
  
- **n..n ou \*..\* (muitos para muitos)** onde ambos os lados podem referenciar múltiplas unidades da outra.
  
  Em um sistema de biblioteca, um título pode ser escrito por vários autores, ao mesmo tempo que um autor pode escrever vários títulos.

&nbsp;

Os relacionamentos podem ser classificadas de acordo com o motivo de sua existência:

- **Relacionamentos Fortes** são aquelas que existem entre duas entidades fortes.

- **Relacionamentos fracos** são aquelas entre uma entidade forte e uma entidade fraca. A chave da entidade fraca vai ser constituída da chave primária da entidade fraca mais a chave primária da entidade forte.

&nbsp;

Em geral os relacionamentos são nomeados com **verbos** ou **expressões** que representam a forma como as entidades interagem ou a ação que uma exerce sobre a outra. Essa nomenclatura pode variar de acordo com a direção em que se lê o relacionamento, conforme vimos na frase "João trabalha na universidade PUCRS".

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/relacionamentos.png width=300>

Figura 4: Relacionamentos

&nbsp;

### Recapitulando: Entidade Associativa

**Entidades Associativas** são utilizadas para permitir que um relacionamento seja visto como uma entidade. Ao ser utilizado, faz com que aquele relacionamento seja utilizado como entidade em outros relacionamentos.

  
  Vamos considerar o sistema de reservas de assentos para vôos de uma companhia aérea. Existe a entidade **Voo**, existe a entidade **Assento**, e existe o relacionamento **Disponibilidade** entre as duas entidades. O **Passageiro**, ao fazer uma **Reserva**, não se relaciona isoladamente com a entidade **Voo** e nem com a entidade **Assento**, e sim com relacionamento (**Disponibilidade**) dessas duas entidades. Mas como entidades não podem se relacionar com relacionamentos, transformamos o relacionamento em uma entidade associativa.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-entidade-associativa.png width=300>

Figura 5: Entidade Associativa

Usamos a entidade associativa quando:
- Existem entidades participantes de um relacionamento que são opcionais (voo-assento-passageiro)
- Existem entidades participantes de um relacionamento que são repetitivas (pessoa_1-pessoa_2-filhos)

&nbsp;

### Diagrama Entidade-Relacionamento

Modelo entidade-relacionamento: um modelo conceitual

Diagrama Entidade-Relacionamento: sua representação gráfica.


Utilizamos o diagrama para representar o modelo conceitual através de símbolos, para auxiliar no desenvolvimento do sistema.

Permite criar uma linguagem comum entre o analista responsável por levantar os requisitos e os desenvolvedores responsáveis por implementar o que foi modelado, facilitando a comunicação da equipe.

&nbsp;

#### Elementos-base do diagrama entidade-relacionamento

- **Entidades**

  - As `entidades fortes` são representadas por um retângulo.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-entidade-forte.png width=100>

    Figura 6: Entidade forte

  &nbsp;

  - As `entidades fracas` são representadas por dois retângulos.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-entidade-fraca.png width=100>

    Figura 7: Entidade fraca
    
  &nbsp;

  - As `entidades associativas` são representadas por um losango envolto em um retângulo.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-entidade-associativa.png width=400>

    Figura 8: Entidade associativa

&nbsp;

- **Atributos**

  - Os `atributos simples de valor único e armazenados` podem ser representados tanto por uma elipse quando por um pequeno círculo.
  
    Deve-se escolher um deles e utilizar somente ele durante a representação.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-atributo-simples.png width=200>

    Figura 9: Atributo simples de valor único e armazenado

  &nbsp;

   - Os `atributos compostos` são representados por uma elipse principal com outras elipses ligadas a ela.

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-atributo-composto.png width=200>

      Figura 10: Atributo composto

  &nbsp;

   - Os `atributos multivalorados` são representados por duas elipses.

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-atributo-multivalorado.png width=100>

      Figura 11: Atributo multivalorado
  
  &nbsp;

   - Os `atributos derivados` são representados por uma elipse tracejada.

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-atributo-derivado.png width=100>

      Figura 12: Atributo derivado

&nbsp;

- **Chave primária**

  - A `Chave primária` pode ser representada tanto por uma elipse com sublinhado no nome quanto por um pequeno círculo com fundo preto.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-chave-primaria.png width=200>

    Figura 13: Chave Primária

&nbsp;

- **Relacionamentos**

  - Os `relacionamentos fortes` são representados por um losango.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-relacionamento-forte.png width=400>

    Figura 14: Relacionamento forte

  &nbsp;
  
  - Os `relacionamentos fracos` são representados por dois losangos, com a linha de ligação duplicada.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-relacionamento-fraco.png width=400>

    Figura 15: Relacionamento fraco

&nbsp;

  - **Cardinalidades**

    - `Cardinalidade 1..1` No mínimo 1, no máximo 1. Obs: o mínimo também pode ser zero, ai seria (0:1) 

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-cardinalidade-1-1.png width=400>

      Figura 16: Cardinalidade 1..1
  
    &nbsp;

    - `Cardinalidade 1..n` No mínimo 1, no máximo n. Obs: o mínimo também pode ser zero, ai seria (0:n).

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-cardinalidade-1-n.png width=400>

      Figura 17: Cardinalidade 1..n
  
    &nbsp;

    - `Cardinalidade n..n`  No mínimo n, no máximo n. Obs: o mínimo também pode ser maior que 1, como por exemplo (3:n).

      <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-cardinalidade-n-n.png width=400>

      Figura 18: Cardinalidade n..n
  
&nbsp;

  - `Leitura da cardinalidade` Na leitura das cardinalidades, por exemplo na relação *titular-dependente*, dizemos que o titular registra no mínimo 1 e no máximo n dependentes. Ou seja, identificamos a entidade, pulamos a cardinalidade que está na entidade lida, identificamos o relacionamento e depois a cardinalidade oposta à primeira entidade, e por fim a entidade restante.

    <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/mer-ler-cardinalidade.png width=400>

    Figura 19: Cardinalidade n..n

&nbsp;

Podemos escrever o diagrama entidade-relacionamento de diversas formas diferentes:

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_1_imobiliaria.png width=300>

Figura 20: Diagrama de um sistema de imobiliária com cardinalidade simplificada

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_2_vendas.png width=300>

Figura 21: Diagrama de uma venda

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_3_com_atributos.png width=300>

Figura 22: Diagrama com atributos em sua notação original

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_4_classes.png width=300>

Figura 23: Diagrama com atributos em sua notação mais atual (diagrama de classes)

&nbsp;

### Ferramentas utilizadas para desenhar os diagramas

Softwares como StarUML BrModelo ou o Draw IO.

https://staruml.io/

http://www.sis4.com/brmodelo/

https://www.brmodeloweb.com/lang/pt-br/index.html

https://www.diagrams.net/

&nbsp;

Em aula vamos utilizar o último da lista, Draw IO (ou diagrams.net).

## Modelando nosso primeiro banco de dados

A empresa ACME registra os funcionários, departamentos e projetos dela. Após a fase de levantamento e análise de requisitos, chegamos na seguinte descrição:

&nbsp;

> A empresa é organizada em departamentos. Cada departamento tem um nome exclusivo, um número exclusivo e um funcionário em particular que o gerencia. Registramos a data inicial em que esse funcionário começou a gerenciar o departamento. Um departamento pode ter vários locais.
> 
> Um departamento controla uma série de projetos, cada um deles com um nome exclusivo, um número exclusivo e um local exclusivo.
> 
> Armazenamos o nome, número do Cadastro de Pessoa Física, endereço, salário, sexo (gênero) e data de nascimento de cada funcionário. Um funcionário é designado para um departamento, mas pode trabalhar em vários projetos, que não necessariamente são controlados pelo mesmo departamento. Registramos o número atual de horas por semana que um funcionário trabalha em cada projeto. Também registramos o supervisor direto de cada funcionário (que é outro funcionário).
> 
> Queremos registrar os dependentes de cada funcionário para fins de seguro. Para cada dependente, mantemos o nome, sexo, data de nascimento e parentesco com o funcionário, aleḿ do Cadastro de Pessoa Física desse dependente.


&nbsp;

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.
