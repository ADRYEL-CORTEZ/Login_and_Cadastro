from flask import Flask, render_template, request, redirect, url_for, flash

meu_site = Flask(__name__)
meu_site.secret_key = 'sua_chave_secreta'

# Simulação de banco de dados para armazenar usuários cadastrados
users = []

@meu_site.route('/')
def index():
    return render_template('login.html')

@meu_site.route('/criar_login', methods=['GET', 'POST'])
def criar_login():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']

        if senha != confirmar_senha:
            flash('As senhas não coincidem. Tente novamente.', 'danger')
        else:
            users.append({
                'nome': nome,
                'cpf': cpf,
                'email': email,
                'telefone': telefone,
                'endereco': endereco,
                'senha': senha
            })
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('index'))

    return render_template('formulario.html')




if __name__ == '__main__':
    meu_site.run(debug=True)
