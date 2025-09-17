# 🐍 Python Playwright Tests

Este repositório contém **testes automatizados usando Playwright + Pytest** para validação de sites.  

Ele demonstra **automação de frontend**, geração de **relatórios HTML** e pode ser integrado com **CI/CD**.

---

## 🛠 Tecnologias utilizadas

- 🐍 Python 3.10+  
- 🎭 Playwright (Python)  
- ⚡ Pytest  
- 📄 Pytest-HTML (para relatórios)  

---

## 🚀 Como rodar os testes localmente

```bash
# Clone o repositório
git clone https://github.com/QAMilenaTorres/python-playwright-tests.git
cd python-playwright-tests

# Instale dependências
pip install -r requirements.txt

# Instale navegadores do Playwright
playwright install

# Execute os testes
pytest
