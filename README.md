# 🚀 Engenharia de Software II – Análise Arquitetural do Projeto ChatTTS com LLMs
## 📋 Sumário

1. [Sobre o Projeto](#1--sobre-o-projeto)
2. [Projeto Selecionado – ChatTTS](#projeto-selecionado--chattts)
3. [Objetivos da Análise](#objetivos-da-análise)
4. [Metodologia Utilizada](#metodologia-utilizada)
5. [Modelos de Linguagem Utilizados](#modelos-de-linguagem-utilizados)
6. [Estrutura do Repositório](#estrutura-do-repositório)
7. [Instalação e Execução](#instalação-e-execução)
8. [Reprodutibilidade do Experimento](#reprodutibilidade-do-experimento)
9. [Autores e Contribuições](#autores-e-contribuições)
    
## 📌 1. Sobre o Projeto

Este repositório contém os artefatos, código e documentação utilizados na análise dos padrões de commits, branching e releases do projeto ChatTTS, um modelo open-source de Text-to-Speech (TTS).

A análise foi realizada como parte da disciplina de Evolução de Software, utilizando Large Language Models (LLMs) para avaliar estratégias de desenvolvimento e disponibilização do software, com base em dados extraídos de:

- Documentação oficial

- Issues

- Pull Requests

- Commits

- Releases

Toda a análise foi implementada em um notebook Python, executado no Google Colab, utilizando modelos da plataforma Hugging Face.

🔗 Repositório analisado:
https://github.com/2noise/ChatTTS

## 🧩 2. Projeto Selecionado – ChatTTS

O ChatTTS é um projeto open-source voltado para conversão de texto em fala, utilizando técnicas modernas de síntese de voz baseadas em modelos de linguagem.

Características principais:

- Geração de áudio natural a partir de texto

- Aplicável em assistentes virtuais, acessibilidade e aplicações interativas

- Projeto ativo, com histórico relevante de commits e releases

Essas características tornam o ChatTTS um excelente candidato para análise de governança de software e práticas evolutivas.

## 🎯 3. Objetivos da Análise

O objetivo principal deste estudo é:

- Identificar os padrões de commits utilizados no projeto

- Analisar a estratégia de releases adotada

- Avaliar se modelos de linguagem conseguem inferir corretamente práticas de engenharia de software

- Comparar as respostas entre diferentes LLMs, observando convergências e divergências

## 🧪 4. Metodologia Utilizada

A metodologia adotada consistiu nos seguintes passos:

- Coleta de dados do repositório ChatTTS via GitHub API

- Extração de:
  - Commits

  - Pull Requests

  - Releases

  - Documentação

- Construção de um prompt estruturado, onde os modelos assumem o papel de um engenheiro de software pleno

- Execução da inferência utilizando 3 modelos distintos

- Consolidação dos resultados em um relatório final

Toda a execução ocorreu de forma automatizada dentro de um notebook Python no Google Colab.

## 🤖 5. Modelos de Linguagem Utilizados

Foram utilizados três Large Language Models (LLMs), escolhidos por sua capacidade de raciocínio e análise de texto técnico:

- Qwen/Qwen2.5-72B-Instruct
https://huggingface.co/Qwen/Qwen2.5-72B-Instruct

- HuggingFaceH4/zephyr-7b-beta
https://huggingface.co/HuggingFaceH4/zephyr-7b-beta

- google/gemma-2-9b-it
https://huggingface.co/google/gemma-2-9b-it

Cada modelo foi submetido ao mesmo contexto e prompt, permitindo uma comparação direta entre os resultados.


## 📁 6. Estrutura do Repositório

```text
.
├── Chattts_Atv2.ipynb          # Notebook com toda a análise e inferência dos modelos
├── relatorio_final_ia.txt      # Resultados consolidados das análises com os 3 LLMs
├── [nome_dos_integrantes].pdf  # Tutorial / relatório escrito da atividade
└── README.md                   # Este arquivo
```

## 🛠️ 7. Instalação e Execução

Toda a execução do projeto é feita no Google Colab (plano gratuito).

### Passo 1 – Abrir o Notebook

- Faça upload do arquivo Chattts_Atv2.ipynb no Google Colab

- Ou abra diretamente pelo Google Drive

### Passo 2 – Configurar Token da Hugging Face

No notebook, localize a constante:

```text
HF_TOKEN = "STRING_DO_TOKEN"
```

Substitua pelo seu token pessoal da Hugging Face.

### Passo 3 – Executar o Notebook

Clique em “Run all” no Colab.

As seguintes etapas serão executadas automaticamente:

- Instalação das dependências

- Download dos dados do ChatTTS via GitHub API

- Processamento e geração de datasets intermediários

- Execução da inferência nos três modelos

- Geração dos resultados finais

## ♻️ 8. Reprodutibilidade do Experimento

Os resultados obtidos são reprodutíveis, desde que:

- O ambiente do Google Colab seja mantido

- As versões das bibliotecas sejam preservadas

- O mesmo conjunto de prompts seja utilizado

## 👥 9. Autores e Contribuições
| Nome Completo | Matrícula | Contribuição na Atividade |
|--------------|-----------|----------------------------|
| Filippi Reis Menezes | 202300027230 |Construção e Análise dos Modelos DistilGPT2, FLAN-T5, bart-large-mnli|
| Jackson Santana Carvalho Júnior | 202300027365 |Construção e Análise dos Modelos DistilGPT2, FLAN-T5, bart-large-mnli|
| Gabriel Bastos Pimentel | 202300061590 |Construção e Análise dos Modelos Qwen2.5, Zephyr 7B, Gemma 2|
| Marcos Vinícius Dantas Aguiar | 201800084345 |Construção e Análise dos Modelos DistilGPT2, FLAN-T5, bart-large-mnli|
| Caio Victor Prado Cruz | 202100011234 |Análise Manual e Revisão|
| Yan Victor Araujo do Nascimento | 202100046006 |Construção e Análise dos Modelos Qwen2.5, Zephyr 7B, Gemma 2|
| Leonardo de Souza Aragão | 202200117002 |Construção e Análise dos Modelos Qwen2.5, Zephyr 7B, Gemma 2|
| Vênisson Cardoso dos Santos | 201700063182 |Análise Manual e Revisão|

Estrutura de trabalho:
O grupo atuou de forma colaborativa na:
- Coleta de dados
- Definição da metodologia
- Execução das análises
- Consolidação dos resultados
