from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
        Renderiza a página home
    """
    return render_template('home/index.html', title="Bem vindo")

@home.route('/dashboard')
@login_required
def dashboard():
    """
        Renderiza a tela de dashboard que requer autênticação    
    """
    return render_template('home/dashboard.html', title="Dashboard")