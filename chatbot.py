import os
import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai import types

# Carregar variáveis de ambiente
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("A chave da API não foi encontrada")

genai.configure(api_key=API_KEY)
client = genai.GenerativeModel("gemini-2.5-flash")

# Contexto 
context = [
    {
        "role": "model",  
        "parts": [{
            "text": """
Você é GitBot, um assistente rápido, jovem e direto para ensinar Git.
Regras:
- Sempre responda em português, de forma clara e descontraída.
- Não use negrito, itálico ou Markdown (é só terminal).
- Explique de maneira curta e prática, mostrando comandos Git em exemplos.
- Se o usuário perguntar algo fora de Git, diga: "Ei, só sei falar sobre Git, beleza?"

Tópicos que você cobre:
- git init, git clone, git status, git add, git commit, git push, git pull, git fetch
- Criar, alternar e mesclar branches
- Desfazer mudanças com reset, revert, checkout
- Boas práticas de branch, commits e organização
"""
        }]
    }
]

# Função para pegar texto da resposta
def extrair_texto(resp):
    try:
        return resp.candidates[0].content.parts[0].text.strip()
    except Exception:
        return "Desculpa, não consegui gerar a resposta :( "

# Função para gerar resposta
def gerar_resposta(pergunta: str) -> str:
    resp = client.generate_content(
        contents=context + [
            {"role": "user", "parts": [{"text": pergunta}]}
        ],
        generation_config=types.GenerationConfig(
            temperature=0.6,
            max_output_tokens=1024  
        )
    )
    return extrair_texto(resp)

def main():
    print("--- Chatbot sobre Git ---")
    print("Você pode fazer até 3 perguntas, fique à vontade :D\n")

    respostas = []
    perguntas = []

    for i in range(3):
        pergunta = input(f"Pergunta {i+1}: ").strip()
        perguntas.append(pergunta)
        resposta = gerar_resposta(pergunta)
        respostas.append(resposta)
        print("\nResposta:\n", resposta)
        print("-" * 50)

    # Gerar resumo 
    resumo_prompt = (
        "Você é o GitBot. Faça um resumo curto das respostas anteriores, "
        "citando apenas os comandos Git que o usuário aprendeu."
    )

    # Juntando as respostas anteriores para o resumo
    conteudo_resumo = "\n".join(respostas)

    resumo = client.generate_content(
        contents=context + [
            {"role": "user", "parts": [{"text": resumo_prompt + "\n\nRespostas anteriores:\n" + conteudo_resumo}]}
        ],
        generation_config=types.GenerationConfig(
            temperature=0.6,
            max_output_tokens=500
        )
    )

    print("\nResumo Final!!\n")
    print(extrair_texto(resumo))

if __name__ == "__main__":
    main()