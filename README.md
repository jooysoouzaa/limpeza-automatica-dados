# Limpeza Automática de Dados

Esse projeto tem o objetivo demonstrar um processo simples de **automação com Python e CI/CD utilizando GitHub Actions**.

## 🔍 O que o script faz:
- Lê um arquivo CSV com dados brutos (`data/dados.csv`);
- Remove linhas duplicadas e vazias;
- Salva o novo arquivo limpo em `output/dados_limpos.csv`.

## ⚙️ CI/CD
Toda vez que um novo `push` é feito no repositório, o GitHub Actions executa automaticamente o script de limpeza.

## 📁 Estrutura
```
data/              -> CSV original
output/            -> CSV limpo
limpeza.py         -> Script principal
.github/workflows  -> CI/CD com GitHub Actions
```
