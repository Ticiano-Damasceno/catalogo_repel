from flask import Flask, render_template, request, redirect, url_for
from models import db

app = Flask(__name__,template_folder='template')

conexao = db()

@app.route('/')
def index():
    consulta = conexao.consulta_geral()
    return render_template('index.html', dados = consulta)

@app.route('/index')
def inicio():
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        conexao.inserir(
            request.form['descricao'], 
            request.form['referencia'],
            request.form['aplicacao'],
            request.form['codigo_fornecedor'],
            request.form['valor_venda'],
            request.form['observacao']            
        )
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    conexao.excluir(id)
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET','POST'])
def alterar(id):
    if request.method == 'GET':
        resultado = conexao.consulta_unico(id)
        return render_template ('edit.html', dados = resultado)
    else:
        conexao.alterar(
            id, 
            request.form['descricao'], 
            request.form['referencia'],
            request.form['aplicacao'],
            request.form['codigo_fornecedor'],
            request.form['valor_venda'],
            request.form['observacao']
        )
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)