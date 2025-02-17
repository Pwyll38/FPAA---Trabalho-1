## Implementação do Algoritmo de Karatsuba em Python

O presente projeto é uma implementação do método de Karatsuba tem como objetivo a multiplicação de dois numeros de forma mais fácil do que o método iterativo. Para isso, o algoritmo emprega a lógica de "divide and conquer", na qual se substitui a multiplicação de dois números grandes por três números menores. 

### Como executar o projeto

Passo 1: Entrar no diretório do projeto, usando o seguinte comando: 
    ``` cd "trabalho 1"```

Passo 2: Executar o comando: 
    ```python3 main.py```

Passo 3: Digitar o primeiro numero à ser multiplicado

Passo 4: Digitar o segundo numero à ser multiplicado

#### Versão do python

Este projeto foi desenvolvido na versão 3.12.3 do Python.

### Descrição do projeto

#### Arquivo: main.py**

Objetivo: Este arquivo principal configura e executa o método de Karatsuba.

#### Descrição das funções**

**findSum(str1, str2)**

Encontra a soma de números em formato String.

Parametros: 
    str1: Primeiro número a ser somado.
    str2: Segundo número a ser somado.

Retorno: 
    A soma da String dos números 

**findDif(str1, str2)**

Encontra a diferença de números em formato String.

Parametros: 
    str1: Primeiro número a ser subtraido.
    str2: Segundo número a ser subtraido.

Retorno: 
    A diferença entre a String dos números 

**removeLeadingZeros(s)**

Remove os zeros iniciais de uma dada string.

Parametros:
    s: String cujos zeros serão removidos.

Retorno:
    s sem os zeros inciais. 

**karatsuba(str1, str2)**

Utiliza o método de karatsuba para multiplicar dois números. 

Parametros: 
    A: Primeiro número à ser multiplicado.
    B: Segundo número à ser multiplicado.

Retorno:
    Produto dos números A e B

**Estrutura do arquivo**

1. Importa o módulo necessário
2. Define as funções a serem utilizadas
3. Recebe os números a serem múltiplicados
4. Executa o método de Karatsuba e imprime o resultado


#### Relatório técnico 

**Complexidade ciclomática**

Fluxo de controle: 
    1. Verifica se o arquivo rondando o código é o main.
        Se verdadeiro: continua a execussão do programa
        Se falso: Finaliza a execussão
    2. Receber o primeiro número.
    3. Receber o segundo número.
    4. Executa a função "karatsuba" com os dois números como entrada.
    5. Verifica se os números são maiores que 10
        Se verdadeiro: retorna a multiplicação dos números pelo método tradicional. 
        Se falso: continua a execussão do método
    6. Guarda o maior entre os dois números
    7. Pega a metade desse valor. 
    8. Preenche a string de 0s até o tamanho do maior número no primeiro.
    9. Preenche a string de 0s até o tamanho do maior número no segundo. 
    10. Separa as metades do primero número.
    11. Separa as metades do segundo número.
    12. Calcula o produto da primeira metade dos números divididos.
    13. Calcula o produto da segunda metade dos números divididos.
    14. Adiciona as metades e encontra o produto dos dois
    15. Encontra a diferença entre as metades.
    16. Retorna o valor sem os 0s a mais.

**Valor da complexidade**

Nós(N): 26
Arestas(E): 25

Complexidade ciclomática(M) = E - N + 2P

Complexidade ciclomática = 25 - 26 + 2*1

Complexidade ciclomática = 2

**Complexidade Assintótica**

Complexidade espacial: O(n)
Complexidade da multiplicação: O(n^log2(3))

#### Grafo de fluxo

#### Links úteis
https://en.wikipedia.org/wiki/Karatsuba_algorithm

https://www.geeksforgeeks.org/karatsuba-algorithm-in-python/ 

https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PROJETOS

http://www.ccas.ru/personal/karatsuba/divcen.pdf 

https://www.bigocalc.com/ 