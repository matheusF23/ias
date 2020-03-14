# IAS

Este projeto consiste em desenvolver a arquitetura utilizada no computador IAS.

## Arquitetura do projeto

A pasta IAS/ias contém o arquivo principal da execução (ias.py) e alguns pacotes contendo módulos necessários para a execução do programa.

### Executando programas

No arquivo principal (ias.py) insira na variável program o programa a ser carregado na memória e execute o arquivo ias.py. Basta colocar o path para o arquivo .txt.

A formatação do arquivo 'program.txt' é a seguinte: 'palavra de instrução' + 'comentários'

Cada linha inicia com a palavra de instrução seguida de um possível comentário. 

Exemplo de um programa para somar 1 + 1:

```as
0001000000000000001000000000000000000000 JUMP+M(X,20:39)
0000010100000000010100000000000000000000 ADD M(X)
0000000000000000000000000001000000000100 LOAD M(X)
0000000000000000000000000000000000000000
0000000000000000000000000000000000000001 Number 1
0000000000000000000000000000000000000001 Number 1
```
