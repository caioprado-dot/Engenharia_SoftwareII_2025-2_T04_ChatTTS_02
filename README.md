# Análise Arquitetural do ChatTTS
## Autores
- Filippi Reis Menezes - 202300027230
- Jackson Santana Carvalho Júnior - 202300027365
- Gabriel Bastos Pimentel - 202300061590 
- Marcos Vinícius Dantas Aguiar - 201800084345
- Caio Victor Prado Cruz - 202100011234
- Yan Victor Araujo do Nascimento - 202100046006
- Leonardo de Souza Aragão - 202200117002
- Vênisson Cardoso Dos Santos – 201700063182

Contribuição:

## Introdução

Este repositório contém o código, artefatos e documentação utilizados
para realizar a análise os **padrões de commits e releases** do projeto
**ChatTTS** (modelo de text-to-speech open-source)(https://github.com/2noise/ChatTTS).\
A análise foi implementada em um **notebook Python executados no Google
Colab**, utilizando diferentes modelos da Hugging Face aplicados nas issues, documentação, releases e pull-requests do repositório original.

**Modelos utilizados**:
- https://huggingface.co/Qwen/Qwen2.5-72B-Instruct

- https://huggingface.co/HuggingFaceH4/zephyr-7b-beta

- https://huggingface.co/google/gemma-2-9b-it

------------------------------------------------------------------------

## Estrutura do Repositório

    .
    ├── Chattts_Atv2.ipynb` -> arquivo contendo a análise com os 3 modelos
    │
    ├── [nome_dos_integrantes].pdf -> tutorial escrito
    └── README.md  ← este arquivo

------------------------------------------------------------------------

## Objetivo do Projeto

O propósito deste estudo é:

1.  **Extrair informações** sobre os **padrões de commits e releases** do repositório ChatTTS.\

### Método
- Foram utilizados 3 modelos(LLMs), tendo como contexto um prompt no qual eles assumem o papel de um engenheiro de software pleno,\
para análisar o repositório(documentação, commits, pull-requests, releases) e classificar as estratégias utilizadas para o desenvolvimento e disponibilização do projeto.
------------------------------------------------------------------------

## Como Executar

Toda a execução é feita **no Google Colab** utilizando o plano Free(gratuito).

### **1. Abrir o Colab**

Faça upload do notebook desejado:

-   `Chattts_Atv2.ipynb.ipynb`

Ou abra diretamente pelo Google Drive.
Então, procure a constante `HF_TOKEN` no arquivo e adicione o seu token do hugging face, atribuindo o valor da seguinte forma:
- HF_TOKEN = "STRING_DO_TOKEN"

------------------------------------------------------------------------

### **2. Executar o notebook**

Basta clicar no botão "Run all" do colab para que as células que fazem os
passos a seguir sejam executadas:

1.  Instalar dependências\
2.  Baixar arquivos do ChatTTS pelo GitHub API.\
3.  Processar os dados e gerar datasets intermediários.\
4.  Rodar inferência nos modelos.

Os resultados são reproduzíveis desde que o ambiente Colab seja mantido
com as versões indicadas.
------------------------------------------------------------------------
