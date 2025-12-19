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
A análise foi implementada em **notebooks Python executados no Google
Colab**, utilizando diferentes modelos da Hugging Face aplicados nas issues e pull-requests do repositório original.

------------------------------------------------------------------------

## Estrutura do Repositório

    .
    ├── modelo1/
    │   └── ChatTTSTestes.ipynb     → Pipeline 1
    │
    ├── modelo2/
    │   └── script.ipynb            → Pipeline 2
    │
    ├── [nome_dos_integrantes].pdf -> tutorial escrito
    └── README.md  ← este arquivo

------------------------------------------------------------------------

## Objetivo do Projeto

O propósito deste estudo é:

1.  **Extrair informações** sobre os **padrões de commits e releases** do repositório ChatTTS.\

Três pipelines foram desenvolvidas:

### **Pipeline 1:**

Localizada em: `./nome_do_arquivo.ipynb`

------------------------------------------------------------------------

## Como Executar

Toda a execução é feita **no Google Colab** utilizando o plano Free(gratuito).

### **1. Abrir o Colab**

Faça upload do notebook desejado:

-   `nome_do_arquivo.ipynb`

Ou abra diretamente pelo Google Drive.

------------------------------------------------------------------------

### **2. Executar o notebook**

Basta clicar no botão "Run all" do colab para que as células que fazem os
passos a seguir sejam executadas:

1.  Instalar dependências\
2.  Baixar arquivos do ChatTTS pelo GitHub API.\
3.  Processar os dados e gerar datasets intermediários.\
4.  Rodar inferência nos modelos.\
5.  Exportar outputs para `results/`.

Os resultados são reproduzíveis desde que o ambiente Colab seja mantido
com as versões indicadas.
------------------------------------------------------------------------
