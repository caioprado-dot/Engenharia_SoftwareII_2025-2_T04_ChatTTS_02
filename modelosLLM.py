# Instalação de dependências
!pip install huggingface_hub pandas matplotlib seaborn requests -q

import requests
import pandas as pd
import matplotlib.pyplot as plt
import textwrap
from huggingface_hub import InferenceClient

# Configuração de keys
HF_TOKEN = "" 
GITHUB_TOKEN = "" 

# Repositório Alvo
REPO_OWNER = "2noise"
REPO_NAME = "ChatTTS"

# ------------------------------------------------------------------------------
# 1. Coleta de Dados
# ------------------------------------------------------------------------------
print(f"Iniciando coleta de dados de {REPO_OWNER}/{REPO_NAME}...")

def get_headers():
    return {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Coleta de Commits
url_commits = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits?per_page=100"
res_commits = requests.get(url_commits, headers=get_headers())

if res_commits.status_code != 200:
    print(f"Erro ao baixar commits: {res_commits.status_code}")
    commits_data = []
else:
    commits_data = res_commits.json()

# Coleta de Tags
url_tags = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/tags"
res_tags = requests.get(url_tags, headers=get_headers())
tags_data = res_tags.json() if res_tags.status_code == 200 else []

if commits_data:
    # Processamento
    df_commits = pd.DataFrame([{
        "date": c["commit"]["author"]["date"],
        "message": c["commit"]["message"],
        "sha": c["sha"]
    } for c in commits_data if isinstance(c, dict) and "commit" in c])

    # Cálculo de Métricas
    total_commits = len(df_commits)
    merge_commits = df_commits[df_commits['message'].str.contains("Merge pull request", case=False)].shape[0]
    direct_commits = total_commits - merge_commits
    
    merge_ratio = (merge_commits / total_commits * 100) if total_commits > 0 else 0
    tag_list = [t['name'] for t in tags_data[:5]]

    print(f"\nResumo dos Dados:")
    print(f"- Commits Analisados: {total_commits}")
    print(f"- Merges de PR: {merge_commits} ({merge_ratio:.1f}%)")
    print(f"- Versões Recentes: {tag_list}")

    # Visualização
    plt.figure(figsize=(6,6))
    plt.pie([merge_commits, direct_commits], labels=['Merges (PRs)', 'Commits Diretos'], 
            autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], explode=(0.1, 0))
    plt.title(f"Estrutura de Commits: {REPO_NAME}")
    plt.savefig("grafico_commits.png")
    print("Gráfico salvo como 'grafico_commits.png'.")

else:
    print("Falha na coleta de dados. Verifique conexão ou limites da API.")
    total_commits = 0
    merge_ratio = 0
    tag_list = []

# ------------------------------------------------------------------------------
# 2. Utilização das LLMs
# ------------------------------------------------------------------------------
if total_commits > 0:
    prompt = f"""
    Atue como um Engenheiro de Software Sênior. Analise as métricas extraídas do repositório '{REPO_NAME}':

    DADOS TÉCNICOS:
    1. Padrão de Commit: De {total_commits} commits recentes, {merge_ratio:.1f}% foram Merges de Pull Request explícitos. A maioria ({100-merge_ratio:.1f}%) são commits diretos ou "squashed".
    2. Histórico de Versões (Tags): As últimas tags lançadas foram: {', '.join(tag_list)}.
    3. Contexto: Projeto Open Source de IA/Deep Learning.

    TAREFA:
    Com base APENAS nestes dados, responda de forma técnica e concisa:
    A) Qual é o Modelo de Ramificação (Branching Model)? (Gitflow, GitHub Flow ou Trunk-Based?). Justifique com base na linearidade dos commits.
    B) Qual é a Estratégia de Release? (Rapid Release, Release Train ou Ad-hoc?). Analise a periodicidade das tags para justificar.
    """

    modelos = [
        "Qwen/Qwen2.5-72B-Instruct",
        "HuggingFaceH4/zephyr-7b-beta",
        "google/gemma-2-9b-it"
    ]

    print("\nIniciando inferência dos modelos...")
    client = InferenceClient(token=HF_TOKEN)
    resultados = []

    for modelo in modelos:
        print(f"Consultando: {modelo}...")
        try:
            msgs = [{"role": "user", "content": prompt}]
            # Temperatura baixa para maior precisão técnica
            res = client.chat_completion(model=modelo, messages=msgs, max_tokens=500, temperature=0.2)
            resposta_texto = res.choices[0].message.content
            
            print(f"\nSaída ({modelo}):")
            print("-" * 60)
            print(textwrap.fill(resposta_texto, width=80))
            print("-" * 60)
            
            resultados.append({"Modelo": modelo, "Análise": resposta_texto})
            
        except Exception as e:
            print(f"Erro no modelo {modelo}: {e}")
            if "google" in modelo:
                print("Tentando fallback (Phi-3)...")
                try:
                    res = client.chat_completion(model="microsoft/Phi-3-mini-4k-instruct", messages=msgs, max_tokens=500)
                    print("Resposta de fallback recebida.")
                except: pass

    # Exportação do Relatório
    with open("relatorio_final_ia.txt", "w", encoding='utf-8') as f:
        f.write(f"RELATÓRIO DE ANÁLISE AUTOMATIZADA - {REPO_NAME}\n")
        f.write("="*50 + "\n\n")
        for item in resultados:
            f.write(f"MODELO: {item['Modelo']}\n")
            f.write("-" * 20 + "\n")
            f.write(f"{item['Análise']}\n\n")
            f.write("="*50 + "\n\n")

    print("\nProcessamento concluído. Arquivos gerados:")
    print("1. grafico_commits.png")
    print("2. relatorio_final_ia.txt")

else:
    print("Análise abortada por falta de dados.")
