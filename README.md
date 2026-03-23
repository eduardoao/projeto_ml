# 🚀 Setup Completo - Ambiente de Machine Learning com VS Code (Linux)

## 🎯 Objetivo

Este guia descreve como configurar um ambiente completo de desenvolvimento para projetos de Machine Learning usando:

* Python + venv
* VS Code
* FastAPI
* Estrutura profissional de projeto

---

# 🧠 1. Pré-requisitos

## 🔧 Atualizar sistema

```bash
sudo apt update && sudo apt upgrade -y
```

## 🐍 Instalar Python + ferramentas

```bash
sudo apt install python3 python3-venv python3-pip -y
```

Verificar:

```bash
python3 --version
pip3 --version
```

---

# 💻 2. Instalar VS Code

```bash
sudo snap install code --classic
```

Ou via .deb (opcional)

---

# 🔌 3. Extensões VS Code

Instalar:

* Python (Microsoft)
* Pylance
* Jupyter (opcional)

---

# 📁 4. Criar estrutura do projeto

```bash
mkdir -p projeto_ml/{data/raw,data/processed,notebooks,src/{api,data,features,models,utils},artifacts}
cd projeto_ml
```

---

# 🐍 5. Criar ambiente virtual

```bash
python3 -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

---

# 📦 6. Instalar dependências

```bash
pip install pandas numpy matplotlib seaborn scikit-learn fastapi uvicorn joblib jupyter
```

---

# 📄 7. Criar requirements.txt

```bash
pip freeze > requirements.txt
```

---

# ⚙️ 8. Configurar VS Code

Criar pasta:

```bash
mkdir .vscode
```

---

## 📄 .vscode/settings.json

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.analysis.extraPaths": ["${workspaceFolder}"],
  "python.envFile": "${workspaceFolder}/.env"
}
```

---

## 🐞 .vscode/launch.json

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Treinar Modelo",
      "type": "python",
      "request": "launch",
      "module": "src.models.train_model",
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    },
    {
      "name": "API FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["src.api.main:app"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}"
      }
    }
  ]
}
```

---

# 🌍 9. Variáveis de ambiente

## 📄 .env

```bash
PYTHONPATH=.
DATA_PATH=data/raw/dados.csv
MODEL_PATH=artifacts/model.pkl
```

---

# 🧠 10. Estrutura do projeto

```bash
projeto_ml/
│
├── src/
│   ├── api/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── artifacts/
│   └── model.pkl
│
├── notebooks/
├── .venv/
├── .vscode/
├── .env
├── requirements.txt
└── README.md
```

---

# ▶️ 11. Executar projeto

## 🧠 Treinar modelo

```bash
python -m src.models.train_model
```

---

## 🌐 Rodar API

```bash
uvicorn src.api.main:app --reload
```

Acessar:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 12. Testar import

```bash
python -c "from src.models.predict import predict; print('OK')"
```

---

# ⚠️ Problemas comuns

## ❌ ModuleNotFoundError: src

✔️ Solução:

```bash
PYTHONPATH=. python -m src.models.train_model
```

---

## ❌ Modelo não encontrado

✔️ Treinar antes:

```bash
python -m src.models.train_model
```

---

## ❌ VS Code não reconhece venv

✔️ Selecionar manualmente:

```
Ctrl + Shift + P → Python: Select Interpreter
```

---

# 🧠 Boas práticas

* Separar código (`src`) de dados (`data`)
* Usar `.venv` sempre
* Nunca rodar arquivos diretamente (usar `-m`)
* Usar `Path` ao invés de caminhos fixos

---

# 🚀 Próximos passos

* Docker
* CI/CD
* Deploy (Render / AWS)
* MLflow
* Testes automatizados

---

# 💬 Conclusão

Esse setup permite:

* ambiente reproduzível ✔️
* estrutura escalável ✔️
* compatível com produção ✔️
* padrão profissional ✔️

---


# 🧪 Guia de Testes Automatizados (Pytest + Coverage)

## 🎯 Objetivo

Este guia descreve como configurar e estruturar testes automatizados em um projeto de Machine Learning com:

* Pytest
* Testes unitários e de integração
* Coverage de código

---

# 📦 1. Instalação

Instale as dependências:

```bash
pip install pytest pytest-cov
```

Adicione ao `requirements.txt`:

```txt
pytest
pytest-cov
```

---

# 📁 2. Estrutura de testes

```bash
tests/
├── unit/           # testes isolados
│   └── test_predict.py
│
├── integration/    # testes do sistema completo
│   └── test_api.py
```

---

# 🧠 3. Conceitos

## 🔹 Testes Unitários

* Testam funções isoladas
* Não dependem de arquivos reais
* Usam mocks

## 🔹 Testes de Integração

* Testam múltiplos componentes juntos
* Usam API, modelo real, etc.

---

# 🧪 4. Teste Unitário (Mock)

```python
from unittest.mock import patch

@patch("src.models.predict.joblib.load")
def test_predict_mock(mock_model):

    class FakeModel:
        def predict(self, X):
            return [1]

    mock_model.return_value = FakeModel()

    from src.models.predict import predict

    result = predict({
        "idade": 30,
        "renda": 4000,
        "score": 600
    })

    assert result == 1
```

---

# 🌐 5. Teste de Integração (API)

```python
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_predict_endpoint():
    response = client.post("/predict", json={
        "idade": 30,
        "renda": 4000,
        "score": 600
    })

    assert response.status_code == 200
    assert "prediction" in response.json()
```

---

# ⚠️ Observação importante

Para testes de integração, o modelo precisa existir:

```bash
python -m src.models.train_model
```

---

# ▶️ 6. Executar testes

## Todos os t
