# Este é um exemplo de crud's de Funcionario Departamento e Papel

## Instalação

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
export FLASK_CONFIG=development

flask db init
flask db migrate

flask run


Baseado no tutorial

https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one#toc-prerequisites