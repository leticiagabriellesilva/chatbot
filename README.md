# GitBot 🤖

GitBot é um chatbot interativo feito em Python que ensina comandos Git de forma simples, rápida e descontraída.  
Ele responde perguntas sobre Git diretamente no terminal e, no final da interação, gera um resumo com os comandos que você aprendeu.  

### ✨ Funcionalidades

- Responde até **3 perguntas** por execução.
- Explica comandos básicos e intermediários de Git:
  - `git init`, `git clone`, `git status`, `git add`, `git commit`, `git push`, `git pull`, `git fetch`
  - Criar, alternar e mesclar branches
  - Desfazer mudanças com `reset`, `revert`, `checkout`
  - Boas práticas de branches e commits
- Gera um **resumo final** com os comandos Git mencionados nas respostas.

### 🛠 Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

E configurar uma **chave de API do Google Gemini**:  
1. Crie uma conta no [Google AI Studio](https://aistudio.google.com/).  
2. Gere uma API Key.  


### 📦 Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/leticiagabriellesilva/chatbot-python.git
cd chatbot-python
pip install -r requirements.txt
```

Principais dependências: 
1. python-dotenv: para carregar variáveis de ambiente
2. google-generativeai: cliente da API Gemini

### ▶️ Como rodar
1. Crie um arquivo `.env` na raiz do projeto com o conteúdo:  
```env
GEMINI_API_KEY="sua_chave_aqui"
```

2. Execute no terminal:
```bash
python chatbot.py
```

### 📝 Exemplo
```
--- Chatbot sobre Git ---
Você pode fazer até 3 perguntas, fique à vontade!

Pergunta 1: como criar uma branch?

Resposta:
Pra criar uma branch nova: git checkout -b minha-branch

--------------------------------------------------
Pergunta 2: como desfazer um commit?

Resposta:
Você pode usar git reset --soft HEAD~1 (mantém alterações) ou git reset --hard HEAD~1 (descarta alterações).

--------------------------------------------------
Pergunta 3: como atualizar minha branch?

Resposta:
Use git pull pra trazer as últimas mudanças do repositório remoto.

--------------------------------------------------

Resumo Final!

Você aprendeu os comandos: git checkout -b, git reset, git pull
```

### 📂 Estrutura do projeto
```
chatbot/
│– chatbot.py        # Código principal do chatbot
│– requirements.txt  # Dependências do projeto
│– .env.example      # Exemplo de configuração da API Key
│– README.md         # Documentação do projeto
```
