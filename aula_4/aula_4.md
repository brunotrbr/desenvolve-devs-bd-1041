# Modelo Conceitual -> Modelo Lógico

**Modelo Conceitual**: Descrição da realidade sob um aspecto mais formal. É usada como representação de alto nível e considera exclusivamente o ponto de vista do usuário criador dos dados.

**Modelo Lógico**: Inclui detalhes da implementação do banco de dados.

Para transformar do modelo conceitual para o modelo lógico, seguimos as técnicas que estão listadas abaixo:

## Entidades
- Entidades são transformadas em tabelas. Cada entidade vira uma nova tabela.
  
- Definir chave primária
  
  - definir restrições/chave alternativa quando aplicável, usando a cláusula UNIQUE. Ex: Somente um cpf por tabela.
  
- Cada atributo da entidade se transforma em uma coluna da tabela
  
  - Atributos obrigatórios levam a cláusula **NOT NULL**
  
  - Atributos opcionais levam a cláusula **NULL**

- Adotar nomes mais curtos/abreviados, mas ainda legíveis, e padronizados. Remover espaços em branco.
    - Na chave primária, caso seja um código da tabela Pessoa, utilizar o nome codPessoa ou cod_pessoa. 
    - Data de nascimento pode virar dt_nasc ou dtNasc, etc.

- Eliminar atributos compostos
    - Aplainar os atributos (cada atributo ganha uma coluna)
        
        <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/atributos_compostos_aplainados.png width=400>

        Figura 1: Atributos compostos aplainados
    
    - Combinar os atributos (tudo vira uma única coluna)
        
        <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/atributos_compostos_combinados.png width=200>

        Figura 2: Atributos compostos combinados

- Eliminar atributos multivalorados
    - Substituir por n atributos fixos, desde que se saiba e possa limitar o valor de n
        
        <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/atributos_multivalorados_fixos.png width=300>

        Figura 3: Atributos multivalorados fixos
    
    - Criar uma nova tabela, relacionada com a tabela original. O identificador pode ser o próprio atributo ou um identificador externo.
        
        <img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/atributos_multivalorados_nova_tabela.png width=200>

        Figura 4: Atributos multivalorados em nova tabela

&nbsp;

## Relacionamentos

- Os relacionamentos são implementados utilizando chaves estrangeiras, e dependem principalmente da **cardinalidade** dos relacionamentos. De acordo com ela, existem três técnicas diferentes:

&nbsp;

### Técnica da tabela própria ( N:N )

Dada a relação abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/01_relacionamento_n_n.jpg width=300>

Figura 5: Relacionamento N:N

&nbsp;

Criamos:

- Uma tabela para cada entidade
  
- Uma tabela para a relação entre as entidades, com as colunas referentes aos atributos nessa nova tabela

Neste caso, teríamos as seguintes tabelas:

    engenheiro (cod_eng, nome)

    projeto (cod_proj, titulo)

    atuacao (cod_eng, cod_proj, funcao)
        cod_eng referencia engenheiro
        cod_proj referencia projeto

&nbsp;

### Técnica das colunas adicionais ( 1:N )

Dada a relação abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/02_relacionamento_1_n.jpg width=300>

Figura 6: Relacionamento 1:N

&nbsp;

Criamos:

- Uma tabela para cada entidade

- Inserir na tabela correspondente à entidade com cardinalidade máxima 1
  - A coluna identificadora da entidade com cardinalidade **n**
  - As colunas correspondentes aos atributos do relacionamento

Neste caso, teríamos as seguintes tabelas:

    departamento (cod_dep, nome)

    empregado (cod_emp, nome, cod_dep, dt_lot)
        cod_dep referencia departamento

&nbsp;

### Técnica da fusão das tabelas ( 1:1 )

Dada a relação abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/03_relacionamento_1_1.jpg width=300>

Figura 7: Relacionamento 1:1

&nbsp;

Criamos:

- Uma única tabela com todos os atributos das entidades e dos relacionamentos

Neste caso, teríamos a seguinte tabela:

    conferencia (cod_conf, nome, dt_inst_com_org, end_com_org)

&nbsp;

## Regras de implementação

A tabela abaixo resume qual a alternativa preferida de acordo com os tipos de relacionamentos:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/04_regras_implementacao_relacionamentos.jpg width=400>

Figura 8: Regras de implementação de acordo com o relacionamento

&nbsp;

### Relacionamentos 1:1


#### Quando ambas entidades possuem participação opcional

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/05_1_1_ambas_opcionais.jpg width=300>

Figura 9: Relacionamento 1:1, ambas entidades opcionais

&nbsp;

**Técnica preferida**: Colunas adicionais em uma entidade

    mulher (identidade, nome, ident_homem, dt_casamento, regime_casamento)

    homem (identidade, nome)

&nbsp;

    Podemos adicionar colunas do homem na mulher ou da mulher no homem. 
    
    Minimiza o uso de joins, pois os dados da mulher e do casamento estão na mesma linha
    
    Porém, exige o controle dos campos opcionais. Mulheres solteiras possuem os três campos **ident_homem**, **dt_casamento**, **regime_casamento** vazios. Casadas possuem os três campos preenchidos.

&nbsp;

**Técnica alternativa**: Tabela própria

    mulher (identidade, nome)

    homem (identidade, nome)

    casamento (ident_mulher, ident_homem, dt_casamento, regime_casamento)

&nbsp;

    Não precisa mais controlar os campos opcionais, mas força o uso de joins.

&nbsp;

#### Quando uma entidade possui participação opcional ou é obrigatória

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/06_1_1_uma_opcional.jpg width=300>

Figura 10: Relacionamento 1:1, uma entidade opcional ou obrigatória

&nbsp;

**Técnica preferida**: Fusão das tabelas de entidades

    correntista (cod_corrent, nome, cod_cartao, data_exp)

&nbsp;

**Técnica alternativa**: Colunas adicionais em uma entidade

    correntista (cod_corrent, nome)

    cartao (cod_cartao, data_exp, cod_corrent)

&nbsp;

    Colunas do correntista adicionadas no cartão, pois o cartão é opcional. Mas se existir, vai ser vinculado a um correntista.

&nbsp;

### Relacionamentos 1:N

&nbsp;

#### Quando a entidade com cardinalidade máxima 1 possui cardinalidade mínima 0 ou 1

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/07_1_n_min_0_max_1.jpg width=300>

Figura 11: Relacionamento 1:N, a entidade com cardinalidade máxima 1 possui cardinalidade mínima 0 ou 1

&nbsp;

**Técnica preferida**: Colunas adicionais em uma entidade

    financeira (cod_fin, nome)

    venda (id_venda, data, cof_fin, num_parc, tx_juros)

&nbsp;

    Adicionamos as colunas da entidade com cardinalidade n (financeira) na entidade com cardinalidade 0/1 (venda) 

&nbsp;

**Técnica alternativa**: Tabela própria

    financeira (cod_fin, nome)

    venda (id_venda, data)

    financiam (id_venda, cof_fin, num_parc, tx_juros)

&nbsp;

    Desvantagens:
        - Operações que envolvem acesso da venda e do financiamento exigem JOIN
  
        - A chave primária da venda e do financiamento é a mesma
  
    Vantagens:

        - Colunas obrigatórias e opcionais. Na adição de colunas, em caso de venda a vista os campos CodFin, NoParc e TxJuros ficariam vazios, e preenchidos na venda a prazo.


### Relacionamentos N:N

&nbsp;

#### Utilizar técnica da tabela própria

&nbsp;

### Relacionamentos de grau N

&nbsp;

Não possuem regras específicas. Portanto, aplicam-se os seguintes passos:

    - Transformamos o relacionamento em entidade. Essa nova entidade se liga através de um relacionamento binário a cada uma das entidades que participavam do relacionamento original.
  
    - As regras vistas anteriormente são aplicadas às entidades e aos novos relacionamentos criados.

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/08_grau_n_original.jpg width=300>

Figura 12: Relacionamento de grau N original

&nbsp;

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/09_grau_n_binario.jpg width=300>

Figura 13: Relacionamento de grau N convertido em binário

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

Dado o esquema abaixo:

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-4/conteudo/10_generalizacao_especializacao.jpg width=300>

Figura 14: Generalização e especialização

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

        Empregado (CodigoEmp,Tipo,Nome,CIC,CodigoDept, CartHabil,CREA,CodigoRamo)    
            CodigoDept referencia Departamento
            CodigoRamo referencia Ramo
        
        Departamento (CodigoDept, Nome)
        
        Ramo (CodigoRamo,Nome)
        
        ProcessTexto (CodigoProc,Nome)
        
        Dominio (CodigoEmp,CodigoProc)
            CodigoEmp referencia Empregado
            CodigoProc referencia ProcessTexto
        
        Projeto (CodigoProj,Nome)
        
        Participacao (CodigoEmp,CodigoProj)
            CodigoEmp referencia Empregado
            CodigoProj referencia Projeto

    &nbsp;
    
    Vantagens:

    - Sem joins, pois todos os dados estão em uma única tabela

    - Chave primária armazenada uma única vez

    &nbsp;

    Desvantagem:

     - Grande quantidade de colunas opcionais
  
    &nbsp;


2) Uma tabela para cada entidade especializada. Neste caso todas as tabelas referentes às especializações de uma entidade genérica terão cada uma sua tabela. As demais entidades e relacionamentos seguem as regras vistas anteriormente.
    
    &nbsp;

    Neste caso, teríamos o seguinte esquema relacional

        Emp (CodigoEmp,Tipo,Nome,CIC,CodigoDept)    
            CodigoDept referencia Depto
        
        Motorista(CodigoEmp, CartHabil)
            CodigoEmp referencia Emp

        Engenheiro(CodigoEmp, CREA, CodigoRamo)
            CodigoEmp referencia Emp
            CodigoRamo referencia Ramo

        Depto (CodigoDept, Nome)
        
        Ramo (CodigoRamo,Nome)
        
        ProcessTexto (CodigoProc,Nome)
        
        Dominio (CodigoEmp,CodigoProc)
            CodigoEmp referencia Emp
            CodigoProc referencia ProcessTexto
        
        Projeto (CodigoProj,Nome)
        
        Participacao (CodigoEmp,CodigoProj)
            CodigoEmp referencia Emp
            CodigoProj referencia Projeto

    &nbsp;

    Vantagens:

    - As colunas opcionais que aparecem são somente as que podem ser vazias do ponto de vista da aplicação.

    - Controle do tipo é responsabilidade da aplicação

    Desvantagens:
    - Necessidade de joins para recuperar os dados

    - Maior quantidade de chaves primárias/estrangeiras

&nbsp;

# Exercício em aula

Fazer a modelagem lógica em texto da empresa ACME, com base no diagrama construído nas aulas 2 e 3, seguindo o exemplo abaixo:

&nbsp;

    Entidade (CodigoEntidade,Atributo1,Atributo2,CodigoEntidadeEstrangeira)    
        CodigoEntidadeEstrangeira referencia EntidadeEstrangeira

&nbsp;

### Modelagem conceitual

<img src=https://s3.amazonaws.com/ada.8c8d357b5e872bbacd45197626bd5759/banco-dados-postgres/aula-2/conteudo/empresa_acme_diagrama_completo.png width=600>

&nbsp;

### Modelagem lógica

# Modelagem com numero_matricula como chave primária

### Etapa 1 - Mapeamento das entidades
funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, supervisor)
    numero_matricula PK  ## O boticário utiliza o número de matrícula
    cpf UNIQUE

departamentos (num, nome, gerente, localizacoes)
    num PK
    nome UNIQUE

projetos (num, nome, local, dpto_gerencia)
    num PK
    nome UNIQUE
    local UNIQUE

dependentes (cpf, nome, genero, dt_nasc, grau_parent_func, numero_matricula_func)
    cpf PK
    numero_matricula_func FK referencia funcionarios

<!-- # Modelagem com CPF como chave primária
funcionarios (cpf, nome, endereco, salario, genero, dt_nasc, supervisor)
    cpf PK

departamentos (num, nome, gerente, localizacoes)
    num PK
    nome UNIQUE

projetos (num, nome, local, dpto_gerencia)
    num PK
    nome UNIQUE
    local UNIQUE

dependentes (cpf, nome, genero, dt_nasc, grau_parent_func, cpf_func)
    cpf PK
    cpf_func FK referencia funcionarios -->

### Etapa 2 - Mapeamento dos relacionamentos 1:1

    Gerencia:
    departamentos (num, nome, numero_matricula_gerente, dt_ini_gerente, localizacoes)
        num PK
        nome UNIQUE
        numero_matricula_gerente FK referencia funcionarios

### Etapa 3 - Mapeamento dos relacionamentos 1:N
    Trabalha para:
    funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, supervisor, num_dpto)
        numero_matricula PK
        cpf UNIQUE
        num_dpto FK referencia departamentos

    Controla:
    projetos (num, nome, local, num_dpto)
        num PK
        nome UNIQUE
        local UNIQUE
        num_dpto FK referencia departamentos

    Supervisão:
    funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, numero_matricula_supervisor, num_dpto)
        numero_matricula PK
        cpf UNIQUE
        num_dpto FK referencia departamentos
        numero_matricula_supervisor FK referencia funcionarios

    Dependente de:
    dependentes (cpf, nome, genero, dt_nasc, grau_parent_func, numero_matricula_func)
        cpf PK
        numero_matricula_func PK / FK referencia funcionarios

### Etapa 4 - Mapeamento dos relacionamentos N:N

    Trabalha em:
    funcionarios_projetos (numero_matricula_func, num_proj, horas_trabalhadas, mes)
        numero_matricula_func PK / FK referencia funcionarios
        num_proj PK / FK referencia projetos


### Etapa 5 - Mapeamento dos atributos multivalorados

    localizações departamentos:
    localizacoes_departamentos (num_dpto, endereco)
        numero_dpto PK / FK referencia departamentos


### Resultado Final: Juntar Tudo

    funcionarios (numero_matricula, cpf, nome, endereco, salario, genero, dt_nasc, numero_matricula_supervisor, num_dpto)
        numero_matricula PK
        cpf UNIQUE
        num_dpto FK referencia departamentos
        numero_matricula_supervisor FK referencia funcionarios

    departamentos (num, nome, numero_matricula_gerente, dt_ini_gerente, localizacoes)
        num PK
        nome UNIQUE
        numero_matricula_gerente FK referencia funcionarios

    projetos (num, nome, local, num_dpto)
        num PK
        nome UNIQUE
        local UNIQUE
        num_dpto FK referencia departamentos

    dependentes (cpf, nome, genero, dt_nasc, grau_parent_func, numero_matricula_func)
        cpf PK
        numero_matricula_func PK / FK referencia funcionarios

    funcionarios_projetos (numero_matricula_func, num_proj, horas_trabalhadas_func)
        numero_matricula_func PK / FK referencia funcionarios
        num_proj PK / FK referencia projetos

    localizacoes_departamentos (num_dpto, endereco)
        numero_dpto PK / FK referencia departamentos

&nbsp;

# Caixa de sugestões

Tem alguma sugestão para melhorar o andamento das aulas? Por favor preencha o formulário abaixo.

https://forms.gle/Yg6pSQFaoSYtZ4nG8


Não deixe a sugestão de melhorias para depois! Compartilhe antes, que corrijo o mais rápido possível.