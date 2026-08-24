# Semana 06 - Formulários Web

Projeto Flask personalizado para:

- Nome: Taissa
- Instituição: IFSP
- Disciplina inicial: DSWA5
- Usuário PythonAnywhere: taissapieri

## URL esperada

Depois de publicar:

https://taissapieri.pythonanywhere.com

## Estrutura

```text
flask_semana06_taissa/
├── app.py
├── requirements.txt
├── WSGI_PYTHONANYWHERE.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   └── login.html
└── static/
    └── favicon.ico
```

## Caminho no PythonAnywhere

Envie a pasta para:

```text
/home/taissapieri/flask_semana06_taissa
```

## Instalação

No console Bash do PythonAnywhere:

```bash
cd /home/taissapieri/flask_semana06_taissa

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Configuração do Web App

Crie o Web App usando "Manual configuration".

No campo Virtualenv, use:

```text
/home/taissapieri/flask_semana06_taissa/venv
```

No arquivo WSGI, use:

```python
import sys

path = '/home/taissapieri/flask_semana06_taissa'

if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

Depois clique em Reload.

A URL deverá ser:

```text
https://taissapieri.pythonanywhere.com
```
