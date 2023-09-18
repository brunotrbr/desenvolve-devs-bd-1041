# IMPORTANTE:

Foi necessário atualizar nosso modelo da empresa ACME, adicionando as cardinalidades mínimas e máximas, para que possamos utilizar a tabela de regras de forma adequada.

&nbsp;

## Exercício 1

A empresa ACME registra os funcionários, departamentos e projetos de uma empresa. Após a fase de levantamento e análise de requisitos, chegamos na seguinte descrição:

> A empresa é organizada em departamentos. Cada departamento tem um nome exclusivo, um número exclusivo e um funcionário em particular que o gerencia. Registramos a data inicial em que esse funcionário começou a gerenciar o departamento. Um departamento pode ter vários locais.
> 
> Um departamento controla uma série de projetos, cada um deles com um nome exclusivo, um número exclusivo e um local exclusivo.
> 
> Armazenamos o nome, número do Cadastro de Pessoa Física, endereço, salário, sexo (gênero) e data de nascimento de cada funcionário. Um funcionário é designado para um departamento, mas pode trabalhar em vários projetos, que não necessariamente são controlados pelo mesmo departamento. Registramos o número atual de horas por semana que um funcionário trabalha em cada projeto. Também registramos o supervisor direto de cada funcionário (que é outro funcionário).
> 
> Queremos registrar os dependentes de cada funcionário para fins de seguro. Para cada dependente, mantemos o nome, sexo, data de nascimento e parentesco com o funcionário.
> 

&nbsp;

Fazer a modelagem lógica em texto mesmo, do diagrama abaixo, conforme exemplo

> Emp (CódigoEmp,Tipo,Nome,CIC,CódigoDept)    
>     CódigoDept referencia Depto

&nbsp;

<img src=./imagens/exercicio_1_diagrama_empresa_acme.png width=600>

&nbsp;

**Resposta:**

Etapa 1: Mapear as entidades

    funcionarios (cpf_func, nome, endereco, salario, genero, dt_nasc)
        cpf_func PK

    departamentos (num_dpto, nome_dpto)
        num_dpto PK
        nome_dpto UNIQUE

    projetos (num_proj, nome_proj, loc_proj)
        num_proj PK
        nome_proj UNIQUE
        loc_proj UNIQUE

    dependentes (cpf_dep, nome, genero, dt_nasc, grau_parent)
        cpf_dep PK

&nbsp;

Etapa 2: Mapear os relacionamentos 1:1

    Gerencia:
    departamentos (num_dpto, nome_dpto, cpf_gerente, data_inicio_gerente)
        num_dpto PK
        nome_dpto UNIQUE
        cpf_gerente FK funcionarios

&nbsp;

Etapa 3: Mapear os relacionamentos 1:N
    
    trabalha_para:
    funcionarios (cpf_func, nome, endereco, salario, genero, dt_nasc, num_dpto)
        cpf_func PK
        num_dpto FK departamentos

    controla:
    projetos (num_proj, nome_proj, loc_proj, num_dpto)
        num_proj PK
        nome_proj UNIQUE
        loc_proj UNIQUE
        num_dpto FK departamentos

    supervisao:
    funcionarios (cpf_func, nome, endereco, salario, genero, dt_nasc, num_dpto, cpf_supervisor)
        cpf_func PK
        num_dpto FK departamentos
        cpf_supervisor FK funcionarios

&nbsp;

Etapa 4: Mapear os relacionamentos N:N

    trabalha_em:
    funcionarios_projetos (cpf_func, num_proj, horas)
        cpf_func PK / FK funcionarios
        num_proj PK / FK projetos

&nbsp;

Etapa 5: Mapear os atributos multivalorados

    localizações departamento:
    localizacoes_departamentos (num_dpto, endereco)
        num_dpto PK / FK departamentos
        endereco PK

&nbsp;

Resultado final: Juntar tudo

    funcionarios (cpf_func, nome, endereco, salario, genero, dt_nasc, num_dpto, cpf_supervisor)
        cpf_func PK
        num_dpto FK departamentos
        cpf_supervisor FK funcionarios

    departamentos (num_dpto, nome_dpto, cpf_gerente, data_inicio_gerente)
        num_dpto PK
        nome_dpto UNIQUE
        cpf_gerente FK funcionarios

    projetos (num_proj, nome_proj, loc_proj, num_dpto)
        num_proj PK
        nome_proj UNIQUE
        loc_proj UNIQUE
        num_dpto FK departamentos

    dependentes (cpf_dep, nome, genero, dt_nasc, grau_parent, cpf_func)
        cpf_dep PK
        cpf_func FK funcionarios

    funcionarios_projetos (cpf_func, num_proj, horas)
        cpf_func PK / FK funcionarios
        num_proj PK / FK projetos

    localizacoes_departamentos (num_dpto, endereco)
        num_dpto PK / FK departamentos
        endereco PK

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

&nbsp;

**Resposta:**

<img src=./imagens/exercicio_2_diagrama_our_note.png width=400>

&nbsp;

Etapa 1: Mapear as entidades

    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao)
        id_anot PK

    rotulos (id_rot, nome, cor)
        id_rot PK


    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia)
        id_lembr PK

    usuarios (login, senha)
        login PK

&nbsp;

Etapa 2: Mapear os relacionamentos 1:1

    vinculada:
    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot)
        id_lembr PK
        id_anot FK anotacoes

&nbsp;

Etapa 3: Mapear os relacionamentos 1:N
    
    criar lembrete:
    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot, login_usuario)
        id_lembr PK
        id_anot FK anotacoes
        login_usuario FK usuarios

    criar anotacao:
    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    criar rotulos:
    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

&nbsp;

Etapa 4: Mapear os relacionamentos N:N

    possui:
    anotacoes_rotulos (id_anot, id_rotulo)
        id_anot PK / FK anotacoes
        id_rotulo PK / FK rotulos

&nbsp;

Etapa 5: Mapear os atributos multivalorados
    
    N/A

&nbsp;

Resultado final: Juntar tudo

    lembretes (id_lembr, data_hora, sinal_visual, sinal_sonoro, antecedencia, id_anot, login_usuario)
        id_lembr PK
        id_anot FK anotacoes
        login_usuario FK usuarios

    anotacoes (id_anot, titulo, conteudo, dt_criacao, dt_atualizacao, login_usuario)
        id_anot PK
        login_usuario FK usuarios

    rotulos (id_rot, nome, cor, login_usuario)
        id_rot PK
        login_usuario FK usuarios

    usuarios (login, senha)
        login PK

    anotacoes_rotulos (id_anot, id_rotulo)
        id_anot PK / FK anotacoes
        id_rotulo PK / FK rotulos