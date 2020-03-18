# IAS

Este projeto consiste em desenvolver a arquitetura utilizada no computador IAS.

## Arquitetura do projeto

A pasta IAS/ contém o arquivo principal da execução (ias.py) e a pasta IAS/iasLib/ que contém alguns pacotes com módulos necessários para a execução do programa.

### Executando o IAS

**Terminal**:

No diretório ~/IAS/ digite 

```~/ias$ python ias.py```

**Abrindo o arquivo**

Acesse o local do arquivo ias.py e execute-o.

### Executando programas

No arquivo principal (ias.py) insira na variável program o programa a ser carregado na memória e execute o arquivo ias.py. Basta colocar o path para o arquivo .txt. No caso, os programas estão sendo colocados na pasta 'programFiles/'.

A formatação do arquivo 'program.txt' é a seguinte: 'palavra de instrução' + 'comentários'

Cada linha inicia com a palavra de instrução seguida de um possível comentário. 

Exemplo de um programa para somar 1 + 1 com o teste da instrução JUMP+M(X,20:39):

```as
0001000000000000001000000000000000000000 JUMP+M(X,20:39)
0000010100000000010100000000000000000000 ADD M(X)
0000000000000000000000000001000000000100 LOAD M(X)
0000000000000000000000000000000000000000
0000000000000000000000000000000000000001 Number 1
0000000000000000000000000000000000000001 Number 1
```

**OBS:** Não se deve deixar linha em branco no inicio deste arquivo, nem pelo meio do mesmo! 
