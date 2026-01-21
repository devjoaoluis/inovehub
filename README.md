# 🚀 InoveHub - Dashboard de Gestão

Este projeto é um Dashboard interativo para gestão de Inovação (Empresas, Investimentos e Contatos), desenvolvido com Python, Panel, Plotly e PostgreSQL.

## 📋 Pré-requisitos

- Python 3.10+ instalado.
- PostgreSQL instalado e rodando.
- Git instalado.

---

## 🛠️ Instalação e Configuração

Siga os passos abaixo para rodar o projeto localmente após fazer o clone.

### 1. Clone o repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd inovehub

```

### 2. Crie e ative o Ambiente Virtual

Isso isola as bibliotecas do projeto.

**No Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

**No Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt

```

### 4. Configuração do Banco de Dados

1. Crie um banco de dados vazio no seu PostgreSQL chamado **`inovehub_db`**.
2. Na raiz do projeto, crie um arquivo chamado **`.env`** (sem nome, só a extensão).
3. Cole o conteúdo abaixo e ajuste sua senha:

```env
DATABASE_URL = "postgresql://usuario:senha@host:porta/nome_banco"
```

> **Nota:** Se sua senha tiver caracteres especiais (como `@`, `ç`), certifique-se de que eles estejam codificados (URL Encoded) na `DATABASE_URL`.

---

## ▶️ Como Executar

Com o ambiente virtual ativado e o banco configurado, você tem duas opções:

### Opção A: Rodar como Aplicação Web (Recomendado)

Isso abrirá o dashboard direto no navegador, parecendo um site real.

```bash
# Substitua 'seu_arquivo.ipynb' pelo nome real do seu notebook
panel serve seu_arquivo.ipynb --autoreload

```

### Opção B: Abrir no Jupyter Notebook

Para ver o código e editar:

```bash
jupyter notebook

```

---

## 🐛 Solução de Problemas Comuns

- **Erro de "Path too long" no Windows:** Mova a pasta do projeto para um caminho mais curto (ex: `C:\dev\inovehub`).
- **Erro de conexão (senha):** Verifique se o arquivo `.env` está salvo e se a senha do Postgres está correta.
- **Tabela não existe:** Na primeira execução, o script Python deve criar as tabelas automaticamente. Se der erro, verifique se o banco `inovehub_db` foi criado no PgAdmin.
