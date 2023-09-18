# MER: Modelo Entidade Relacionamento

## Como traduzir requisitos de um problema do mundo real para um modelo conceitual?

Como descrever um banco de dados? Temos um cenário real, mas como podemos modelar isso em um banco de dados utilizável?

&nbsp;

Utilizamos o **Modelo Entidade-Relacionamento (MER)**.

Serve para descrever os conceitos e as restrições básicas dos dados para nossa aplicação.

&nbsp;

> Ex: Cadastro de usuários não pode aceitar CPFs repetidos. Nosso banco de dados usa **chave_primária** ou cláusula **unique** para garantir que os valores serão únicos.

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
- *Tipo de entidade*: No processo de descrição, não há interesse em descrever cada entidade individualmente, e sim cada classe de elementos daquela entidade (os atributos, as restrições de integridade, etc)
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

- **Entidades Associativas** surgem quando há a necessidade de associar uma entidade a um relacionamento existente. Na modelagem entidade-relacionamento, **não é possível que um relacionamento seja associado a uma entidade**, então tornamos esse relacionamento uma entidade associativa, que poderá se relacionar com outras entidades.
  
  No nosso sistema de vendas, por exemplo, vamos considerar que a empresa passou a entregar brindes para clientes que comprassem um determinado produto. A entidade **Brinde** não está relacionada nem com a **Venda** nem com o **Produto** em si, e sim com o item da venda (ou seja, com o relacionamento entre Venda e Produto). Como não podemos associar a entidade Brinde com um relacionamento, vamos criar a entidade associativa chamada **Item da venda**, que contém os atributos identificadores das entidades Venda e Produto, além de informações como quantidade, etc. A partir dai podemos relacionar o **Brinde** com o **Item da Venda**, indicando que aquele prêmio foi dado ao cliente por comprar aquele produto em específico.


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

Figura 3: Entidades e Atributos

&nbsp;

#### Chave primária

Um atributo que identifica a entidade em um domínio, e não pode se repetir, é chamado de **Chave Primária**. 

Ex: Cadastro de clientes, na entidade **Cliente** esse atributo poderia ser o **CPF**.

&nbsp;

#### Chave estrangeira

Os atributos referenciais são chamados de **Chave Estrangeira**, e normalmente estão ligados à **chave primária** da outra entidade.

Ex: Sistema de vendas, a entidade **Cliente** possui como chave primária o atributo CPF, e a entidade **Venda** possui um atributo chamado **CPF do cliente**, que seria uma **chave estrangeira** relacionada com o campo CPF da entidade Cliente.

&nbsp;

Observem a imagem abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/chave_primaria_e_estrangeira.jpg width=400>

Figura 4: Chave primária e estrangeira

&nbsp;

Temos a tabela (uma entidade) Pessoa, a tabela Automóvel (uma entidade) e a tabela Propriedade.

Na tabela **Pessoa**, o atributo *Identidade* é uma **chave primária**.

Na tabela **Automóvel**, o atributo *Placa* é uma **chave primária**.

Na tabela **Propriedade**, juntamos a *chave primária Placa* e a *chave primária Identidade*, para compor a chave primária da tabela Propriedade.

Vendo a partir da tabela **Propriedade**, Placa e Identidade são chaves estrangeiras, pois vieram de outras tabelas (onde são chaves primárias).

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
Aponta a quantidade mínima e a quantidade máxima de objetos envolvidos em cada lado do relacionamento. É a *restrição de integridade* dos relacionamentos, e **obrigatoriamente** deve ser incluída na modelagem.

Os relacionamentos podem ser classificados de três formas, de acordo com a Cardinalidade:

- **1..1 (um para um)** onde cada uma das entidades envolvidas referenciam obrigatoriamente apenas uma unidade da outra. 
  
  Em um banco de dados de currículos, por exemplo, cada candidato pode ter somente um currículo na base. Ao mesmo tempo, cada currículo pertence a um único usuário cadastrado.
  
- **1..n ou 1..\* (um para muitos)** onde uma das entidades pode referenciar várias unidades da outra, porem do outro lado cada uma das várias unidades referenciadas só podem estar ligadas em uma única unidade da outra entidade. 
  
  Em um sistema de plano de saúde, um usuário pode ter vários dependentes, mas cada dependente pode estar ligado a somente um usuário principal.
  
- **n..n ou \*..\* (muitos para muitos)** onde ambos os lados podem referenciar múltiplas unidades da outra.
  
  Em um sistema de biblioteca, um título pode ser escrito por vários autores, ao mesmo tempo que um autor pode escrever vários títulos.

&nbsp;

Em geral os relacionamentos são nomeados com **verbos** ou **expressões** que representam a forma como as entidades interagem ou a ação que uma exerce sobre a outra. Essa nomenclatura pode variar de acordo com a direção em que se lê o relacionamento, conforme vimos na frase "João trabalha na universidade PUCRS".

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/relacionamentos.png width=300>

Figura 6: Relacionamentos

&nbsp;

### Diagrama Entidade-Relacionamento

Modelo entidade-relacionamento: um modelo conceitual

Diagrama Entidade-Relacionamento: sua representação gráfica.


Utilizamos o diagrama para representar o modelo conceitual através de símbolos, para auxiliar no desenvolvimento do sistema.

Permite criar uma linguagem comum entre o analista responsável por levantar os requisitos e os desenvolvedores responsáveis por implementar o que foi modelado, facilitando a comunicação da equipe.

&nbsp;

Podemos escrever o diagrama entidade-relacionamento de diversas formas diferentes:

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_1_imobiliaria.png width=300>

Figura 7: Diagrama de um sistema de imobiliária

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_2_vendas.png width=300>

Figura 8: Diagrama de uma venda

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_3_com_atributos.png width=300>

Figura 9: Diagrama com atributos em sua notação original

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/diagrama_4_classes.png width=300>

Figura 10: Diagrama com atributos em sua notação mais atual (diagrama de classes)

&nbsp;

### Ferramentas utilizadas para desenhar os diagramas

Softwares como StarUML BrModelo ou o Draw IO.

https://staruml.io/

http://www.sis4.com/brmodelo/

https://www.brmodeloweb.com/lang/pt-br/index.html

https://www.diagrams.net/

&nbsp;

## Modelando nosso primeiro banco de dados

A empresa ACME registra os funcionários, departamentos e projetos de uma empresa. Após a fase de levantamento e análise de requisitos, chegamos na seguinte descrição:

&nbsp;

> A empresa é organizada em departamentos. Cada departamento tem um nome exclusivo, um número exclusivo e um funcionário em particular que o gerencia. Registramos a data inicial em que esse funcionário começou a gerenciar o departamento. Um departamento pode ter vários locais.
> 
> Um departamento controla uma série de projetos, cada um deles com um nome exclusivo, um número exclusivo e um local exclusivo.
> 
> Armazenamos o nome, número do Cadastro de Pessoa Física, endereço, salário, sexo (gênero) e data de nascimento de cada funcionário. Um funcionário é designado para um departamento, mas pode trabalhar em vários projetos, que não necessariamente são controlados pelo mesmo departamento. Registramos o número atual de horas por semana que um funcionário trabalha em cada projeto. Também registramos o supervisor direto de cada funcionário (que é outro funcionário).
> 
> Queremos registrar os dependentes de cada funcionário para fins de seguro. Para cada dependente, mantemos o nome, sexo, data de nascimento e parentesco com o funcionário.
