# Resolução de Problemas no LeetCode

## Visão Geral
Este repositório contém a resolução de três problemas do LeetCode que abordam conceitos essenciais de algoritmos e estruturas de dados, incluindo métodos clássicos e técnicas avançadas de programação dinâmica.

## Questões
1. [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/description/) - Nível: Difícil

        Descrição: Usa uma tabela dp[i][j], onde dp[i][j] representa o número de formas de formar os primeiros j caracteres de t usando os primeiros i caracteres de s. Se s[i - 1] == t[j - 1], pode incluir esse caractere na subsequência ou ignorá-lo. Caso contrário, a única opção é ignorar o caractere de s.

2. [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/) - Nível: Difícil

        Descrição: Usa busca binária para encontrar o último trabalho que pode ser feito antes do trabalho atual começar. Mantém um array dp onde dp[i] armazena o máximo lucro ao considerar os primeiros i trabalhos. Para cada trabalho, escolhe entre não pegá-lo (dp[i - 1]) ou pegá-lo (dp[idx] + profit).

3. [Seling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood/description/) - Nível: Difícil

        Descrição: Para cada pedaço de madeira (h, w), verifica se pode ser vendido diretamente e tenta dividir em todas as posições horizontais e verticais, somando os lucros dos cortes.


## Como executar
Para cada um desses problemas, o código foi implementado em Python e está disponível neste repositório. Você pode executar os scripts diretamente ou adaptá-los conforme necessário para o seu ambiente de desenvolvimento. Cada problema está isolado em um arquivo de script separado, facilitando o teste individual.

## Vídeo
Para vizualisar o vídeo explicando o projeto clique [AQUI](https://youtu.be/0BkZjH0M5OE).

## Contribuidores
<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/Hellen159">
                <img style="border-radius: 50%;" src="https://github.com/Hellen159.png" width="150px;"/>
                <h5 class="text-center"> <br> Hellen Faria Matrícula: 202016480 </h5>
            </a>
        </td>
      <td align="center">
            <a href="https://github.com/deboracaires">
                <img style="border-radius: 50%;" src="https://github.com/deboracaires.png" width="150px;"/>
                <h5 class="text-center"> <br> Debora Caires Matrícula: 222015103</h5>
            </a>
        </td>
    </tr>
</table>