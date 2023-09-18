# Ordem sugerida de resolução dos exercícios

Caminho:
Material do Aluno > Turma 941 > DS-PY-006 Banco de Dados I > Tipos de bancos de dados > Exercícios

1) ds-py-941-banco-de-dados-configuracao
2) ds-py-941-banco-de-dados-modelagem
3) ds-py-941-banco-de-dados-generalizacao
4) ds-py-941-banco-de-dados-normalizacao
5) ds-py-941-banco-de-dados-modelagem-logica

&nbsp;

# Vídeos para instalação do PostgreSQL no Windows e no Linux, e como conectar no pgadmin

Os vídeos com as instruções para instalação do PostgreSQL no ambiente local estão no diretório aula_01

&nbsp;

# Modelando o banco de dados

Modelo Conceitual: Descrição da realidade sob um aspecto mais formal, apontando informações. É usada como representação de alto nível e considera exclusivamente o ponto de vista do usuário criador dos dados.

Modelo Lógico: Modelo Lógico agrega mais alguns detalhes de implementação.

&nbsp;

## Pontos centrais

As regras vistas abaixo visam dois objetivos básicos:
- Boa performance no banco de dados, visando diminuir o acesso ao disco.
- Simplificação do desenvolvimento e da manutenção das aplicações.

&nbsp;

### Premissas
- **Evitar joins**. Os bancos de dados armazenam os dados de uma linha em sequência no disco, fazendo com que a recuperação deles seja feita de forma mais rápida e em um único acesso ao disco. Quando fazemos *joins*, os dados não estão em sequência, o que exige mais acessos ao disco, aumentando o tempo da consulta.
- **Diminuir o número de chaves primárias**. Para criar as chaves primárias, o banco de dados usa estruturas auxiliares (os índices). Estes índices tendem a ocupar um espaço considerável em disco. Além do mais, inserções e remoções de entradas no índice podem exigir diversos acessos a disco.

&nbsp;

## Redefinição de nomes
- Adotar nomes mais curtos/abreviados, mas ainda legíveis, e padronizados.
- Eliminar espaços em branco e caracteres especiais

> data de nascimento -> dtNasc ou dt_nasc
> 
> data de início do gerente -> dtIniGer ou dt_inicio_ger
> 
> data de início do gerente -> d_i_g (errado, pois ninguém vai saber o que é d_i_g)

&nbsp;

Para transformar do modelo conceitual para o modelo lógico, seguimos algumas técnicas listadas abaixo:

> Importante:
> 
> Esse é o mapeamento inicial das entidades. Ao longo do processo podem ocorrer alterações nesse mapeamento.

## Entidades
- Entidades são transformadas em tabelas
  
- Definir chave primária
  
  - definir restrições/chave alternativa quando aplicável, usando a cláusula UNIQUE
  
- Cada atributo da entidade se transforma em uma coluna da tabela
  
  - Atributos obrigatórios levam a cláusula NOT NULL
  
  - Atributos opcionais levam a cláusula NULL
  
- Adotar nomes mais curtos/abreviados, mas ainda legíveis, e padronizados
    Ex: Na chave primária, caso seja um código da tabela Pessoa, utilizar o nome CodPessoa

- Se possível, indexar atributos muito consultados. Normalmente é feito quando identificamos atributos que serão muito consultados, e em geral quando a aplicação já está rodando.

- Tentar diminuir a quantidade de chaves primárias

- Tentar evitar cláusulas JOIN 

- Eliminar atributos compostos
    - Esquecer as agregações lógicas, e "aplainar" os atributos (cada atributo ganha uma coluna)
    - Esquecer da composição, e combinar os atributos (tudo vira a coluna *endereço*)

    Exemplo de um atributo simples: endereço

    coluna endereço: avenida ipiranga, 1782, apto 206, bairro santana

    Exemplo de um atributo composto: endereço

    endereco_linha_1: avenida ipiranga

    endereco_linha_2: 

    numero: 1782

    complemento: apto 206

    bairro: santana

- Eliminar atributos multivalorados
    - Substituir por n atributos fixos, desde que se saiba e possa limitar o valor de n
    - Criar uma nova entidade, relacionada com a entidade original. O identificador pode ser o próprio atributo ou um identificador externo.

    Multivalorado: 2 ou 3 endereços pra empresa/casa, 2 graduações, etc

    Atributos fixos:

    tabela pessoa

    colunas endereco_1, endereco_2 (para casos que só tenha 2 endereços)

    Nova entidade: entidade endereços_por_pessoa

    chave primária seria o cpf da pessoa composto com o endereço

    123|abc
    123|def
    123|ghi

&nbsp;

## Relacionamentos

- Os relacionamentos são implementados utilizando a chave estrangeira, e depende principalmente da **cardinalidade** dos relacionamentos. De acordo com ela, existem três técnicas diferentes:

&nbsp;

### Tabela própria ( N:N )

Dada a relação abaixo

<img src=./imagens/01_relacionamento_n_n.jpg width=300>

Figura 01: Relacionamento N:N

OBS: A cardinalidade da entidade Engenheiro é a que fica mais longe da entidade. Ou seja, a cardinalidade do Engenheiro é o (0,n) que está ao lado da entidade Projeto.
&nbsp;

Criamos
- Uma tabela para cada entidade
- Uma tabela para a relação entre as entidades, com as colunas referentes aos atributos nessa nova tabela

Neste caso, teríamos as seguintes tabelas:

    engenheiro (cod_eng, nome)

    projeto (cod_proj, titulo)

    atuacao (cod_eng, cod_proj, funcao)
        cod_eng referencia engenheiro (somente pra frisar a chave estrangeira cod_eng na tabela atuação)
        cod_proj referencia projeto

### Colunas adicionais em uma entidade ( 1:N )
Dada a relação abaixo

<img src=./imagens/02_relacionamento_1_n.jpg width=300>

Figura 02: Relacionamento 1:N

&nbsp;

Criamos
- Uma tabela para cada entidade
- Inserir na tabela correspondente à entidade com cardinalidade máxima 1
  - A coluna identificadora da entidade com cardinalidade n
  - As colunas correspondentes aos atributos do relacionamento

Neste caso, teríamos as seguintes tabelas:

    departamento (cod_dep, nome)

    empregado (cod_emp, nome, cod_dep, dt_lot)
        cod_dep referencia departamento

&nbsp;

### Fusão das tabelas de entidades ( 1:1 )
Dada a relação abaixo

<img src=./imagens/03_relacionamento_1_1.jpg width=300>

Figura 03: Relacionamento 1:1

&nbsp;

Criamos
- Uma única tabela com todos os atributos das entidades e dos relacionamentos

Neste caso, teríamos a seguinte tabela:

    conferencia (cod_conf, nome, dt_inst_com_org, end_com_org)

&nbsp;

A tabela abaixo resume qual a alternativa preferida de acordo com os tipos de relacionamentos

<img src=./imagens/04_regras_implementacao_relacionamentos.jpg width=300>

Figura 04: Regras de implementação de acordo com o relacionamento

&nbsp;

### Relacionamentos 1:1

&nbsp;

#### Quando ambas entidades possuem participação opcional

<img src=./imagens/05_1_1_ambas_opcionais.jpg width=300>

Figura 05: Relacionamento 1:1, ambas entidades opcionais

&nbsp;

Técnica preferida: Colunas adicionais em uma entidade

    Adicionar colunas do homem na mulher. Minimiza o uso de joins, mas exige que as colunas sejam obrigatórias.

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    mulher (identidade, nome, identidade_homem)

    homem (identidade, nome)

&nbsp;

Pode ser utilizada: Tabela própria

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    mulher (identidade, nome)

    homem (identidade, nome)

    casamento (ident_mulher, ident_homem, data_casamento)

&nbsp;

#### Quando uma entidade possui participação opcional

<img src=./imagens/06_1_1_uma_opcional.jpg width=300>

Figura 06: Relacionamento 1:1, uma entidade opcional

&nbsp;

Técnica preferida: Fusão das tabelas de entidades

&nbsp;

Neste caso, teríamos a seguinte tabela:

    correntista (cod_corrent, nome, cod_cartao, data_exp)

&nbsp;

Pode ser utilizada: Colunas adicionais em uma entidade

    Colunas do correntista adicionadas no cartão, pois o cartão é opcional. Mas se existir, vai ser vinculado a um correntista.

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    correntista (cod_corrent, nome)

    cartao (cod_cartao, data_exp, cod_corrent)

&nbsp;

### Relacionamentos 1:N

&nbsp;

#### Quando a entidade com cardinalidade máxima 1 possui cardinalidade mínima 0 (ou 1, pois é o mesmo caso)

<img src=./imagens/07_1_n_min_0_max_1.jpg width=300>

Figura 07: Relacionamento 1:N, a entidade com cardinalidade máxima 1 possui cardinalidade mínima 0 (ou 1, pois é o mesmo caso)

&nbsp;

Técnica preferida: Colunas adicionais em uma entidade

    Adicionar colunas da financeira na venda. 

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    financeira (cod_fin, nome)

    venda (id_venda, data, cof_fin, num_parc, tx_juros)

&nbsp;

Pode ser utilizada: Tabela própria

    Desvantagens:
        - Operações que envolvem acesso da venda e do financiamento exigem JOIN
  
        - A chave primária da venda e do financiamento é a mesma
  
    Vantagens:

        - Colunas obrigatórias e opcionais. Na adição de colunas, em caso de venda a vista os campos CodFin, NoParc e TxJuros ficariam vazios, e preenchidos na venda a prazo.

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    financeira (cod_fin, nome)

    venda (id_venda, data)

    financiam (id_venda, cof_fin, num_parc, tx_juros)

&nbsp;

### Relacionamentos de grau N

&nbsp;

Não possuem regras específicas.

&nbsp;

Aplicam-se os seguintes passos:

    - Transformamos o relacionamento em entidade. Essa nova entidade se liga através de um relacionamento binário a cada uma das entidades que participavam do relacionamento original.
  
    - As regras vistas anteriormente são aplicadas às entidades e aos novos relacionamentos criados.

<img src=./imagens/08_grau_n_original.jpg width=300>

Figura 08: Relacionamento de grau N original

&nbsp;

<img src=./imagens/09_grau_n_binario.jpg width=300>

Figura 09: Relacionamento de grau N convertido em binário

&nbsp;

Neste caso, teríamos as seguintes tabelas:

    produto (cod_prod, nome)

    cidade (cod_cid, nome)

    distribuidor (cod_distr, nome)

    distribuicao (cod_prod, cod_cid, cod_distr, dt_inicio)
        cod_prod referencia produto
        cod_cid referencia cidade
        cod_distr referencia distribuidor

&nbsp;

### Generalização/especialização

Dado o esquema abaixo, 

<img src=./imagens/10_generalizacao_especializacao.jpg width=300>

Figura 10: Generalização e especialização

Podemos seguir duas abordagens

1) Uma tabela por hierarquia. Neste caso todas as tabelas referentes às especializações de uma entidade genérica são fundidas em uma única tabela. Esta tabela vai ter:
    
    - Chave primária corresponente ao identificador da entidade mais genérica
    - Caso não exista, uma coluna **tipo** que identifica o tipo de entidade especializada que está sendo representada
    - Uma coluna para cada atributo da entidade genérica
    - Colunas referentes aos relacionamentos dos quais participa a entidade genérica e que sejam implementados através da alternativa de adicionar colunas à tabela da entidade genérica
    - Uma coluna para cada atributo de cada entidade especializada, sendo que estas colunas devem ser definidas como **opcionais** obrigatoriamente
    - Colunas referentes aos relacionamentos dos quais participam cada entidade especializada e que sejam implementados através da alternativa de adicionar colunas à tabela da entidade, sendo que estas colunas devem ser definidas como **opcionais** obrigatoriamente

    &nbsp;

    Neste caso, teríamos o seguinte esquema relacional

        Emp (CódigoEmp,Tipo,Nome,CIC,CódigoDept, CartHabil,CREA,CodigoRamo)    
            CódigoDept referencia Depto
            CódigoRamo referencia Ramo
        
        Depto (CódigoDept, Nome)
        
        Ramo (CódigoRamo,Nome)
        
        ProcessTexto (CódigoProc,Nome)
        
        Domínio (CódigoEmp,CódigoProc)
            CódigoEmp referencia Emp
            CódigoProc referencia ProcessTexto
        
        Projeto (CódigoProj,Nome)
        
        Participação (CódigoEmp,CódigoProj)
            CódigoEmp referencia Emp
            CódigoProj referencia Projeto

    &nbsp;
    
    Vantagens:

    - Sem joins, pois todos os dados estão em uma única tabela

    - Chave primária armazenada uma única vez

    &nbsp;


2) Uma tabela para cada entidade especializada. Neste caso todas as tabelas referentes às especializações de uma entidade genérica terão cada uma sua tabela. As demais entidades e relacionamentos seguem as regras vistas anteriormente.
    
    &nbsp;

    Neste caso, teríamos o seguinte esquema relacional

        Emp (CódigoEmp,Tipo,Nome,CIC,CódigoDept)    
            CódigoDept referencia Depto
        
        Motorista(CodigoEmp, CartHabil)
            CodigoEmp referencia Emp

        Engenheiro(CodigoEmp, CREA, CodigoRamo)
            CodigoEmp referencia Emp
            CodigoRamo referencia Ramo

        Depto (CódigoDept, Nome)
        
        Ramo (CódigoRamo,Nome)
        
        ProcessTexto (CódigoProc,Nome)
        
        Domínio (CódigoEmp,CódigoProc)
            CódigoEmp referencia Emp
            CódigoProc referencia ProcessTexto
        
        Projeto (CódigoProj,Nome)
        
        Participação (CódigoEmp,CódigoProj)
            CódigoEmp referencia Emp
            CódigoProj referencia Projeto

    &nbsp;

    Vantagens:

        - As colunas opcionais que aparecem são somente as que podem ser vazias do ponto de vista da aplicação.
        - Controle do tipo é responsabilidade da aplicação


----
# Exercício em aula

## Exercício 1

Fazer a modelagem lógica em texto mesmo, do diagrama abaixo, conforme exemplo

&nbsp;

> Emp (CódigoEmp,Tipo,Nome,CIC,CódigoDept)    
>     CódigoDept referencia Depto

&nbsp;

<img src=./imagens/exercicio_1_diagrama_empresa_acme.jpg width=600>

&nbsp;

## Exercício 2

Fazer a modelagem conceitual e lógica da descrição abaixo:

> App OurNote
>
> &nbsp;
> 
> O OurNote permite registrar Anotações e Lembretes.
>
> Cada Anotação tem um título, um texto formatado, uma data de criação e uma data de alteração. É possível atribuir Rótulos às Anotações. Os Rótulos têm um nome e uma cor.
>
> É possível, ainda, vincular uma Anotação a um Lembrete. Os Lembretes têm uma data e uma hora para serem dados. Um Lembrete pode dar ou não um sinal visual ou sonoro com uma antecedência definida em minutos em relação a sua data e hora.
>
> As Anotações, Lembretes e Rótulos são criados pelos Usuários, que possuem login e senha.

Modelagem conceitual
<img src=./imagens/exercicio_2_diagrama_our_note.png width=600>

&nbsp;

Modelagem lógica

Etapa 1: Mapear as entidades
    usuarios (login, senha)
        login PK
    
    anotacoes (id_anot, titulo, texto, dt_criac, dt_alter)
        id_anot PK
    
    rotulos (id_rot, nome, cor)
        id_rot PK
    
    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia)
        id_lembr PK
        sinal_visual OPCIONAL
        sinal_sonoro OPCIONAL

Etapa 2: Mapear os relacionamentos 1:1
    vinculada
    anotacoes (id_anot, id_lembr, xxx)
        id_anot PK
        id_lembr FK lembretes
    # Se seguir essa abordagem, quando uma anotação não tiver lembrete, o id_lembr será nulo

    lembretes (id_lembr, data_hora, sinal_visual, sinal_luminoso, antecedencia, id_anot)
        id_lembr PK
        sinal_visual OPCIONAL
        sinal_sonoro OPCIONAL
        id_anot FK anotacoes

Etapa 3: Mapear os relacionamentos 1:N
    criar_lembretes:
    lembretes (id_lembr, data_hora, sinal_visual, sinal_luminoso, antecedencia, id_anot, login_usuario)
        id_lembr PK
        sinal_visual OPCIONAL
        sinal_sonoro OPCIONAL
        id_anot FK anotacoes
        login_usuario FK usuarios

    criar_anotacoes:
    anotacoes (id_anot, titulo, texto, dt_criac, dt_alter, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    criar_rotulos
    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

Etapa 4: Mapear os relacionamentos N:N
    possui:
    anotacoes_rotulos (id_anot, id_rot)
        id_anot PK / FK anotacoes
        id_rot PK / FK rotulos

Etapa 5: Mapear os atributos multivalorados
    N/A

Resultado final: Juntar tudo

    usuarios (login, senha)
        login PK
        
    lembretes (id_lembr, data_hora, sinal_visual, sinal_luminoso, antecedencia, id_anot, login_usuario)
        id_lembr PK
        sinal_visual OPCIONAL
        sinal_sonoro OPCIONAL
        id_anot FK anotacoes
        login_usuario FK usuarios

    anotacoes (id_anot, titulo, texto, dt_criac, dt_alter, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

    anotacoes_rotulos (id_anot, id_rot)
        id_anot PK / FK anotacoes
        id_rot PK / FK rotulos
        