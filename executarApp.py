from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from classes import Biblioteca, Livro

app = Flask(__name__)
app.secret_key = 'secreto'  # Chave secreta para flash messages

# Configuração do Banco de Dados PostgreSQL
POSTGRESQL_IP = "localhost"  # Nome do serviço Docker
POSTGRESQL_LOGIN = "postgres"
POSTGRESQL_PASSWORD = "postgrespw"
POSTGRESQL_DATABASE = "postgres"
POSTGRESQL_PORT = 5435  # Porta padrão do PostgreSQL no Docker

# URI do Banco de Dados
SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRESQL_LOGIN}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_IP}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}'

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição dos modelos
class Livro(db.Model):
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano_de_publicacao = db.Column(db.Integer, nullable=False)
    biblioteca_id = db.Column(db.Integer, db.ForeignKey('biblioteca.id'), nullable=False)

    def __init__(self, titulo, autor, ano_de_publicacao, biblioteca_id):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.biblioteca_id = biblioteca_id

    def __repr__(self):
        return f'<Livro {self.titulo}>'

class Biblioteca(db.Model):
    __tablename__ = 'biblioteca'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    livros = db.relationship('Livro', backref='biblioteca', lazy=True)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'<Biblioteca {self.nome}>'

# Rotas do seu aplicativo
@app.route('/')
def index():
    bibliotecas = Biblioteca.query.all()
    livros = Livro.query.all()
    return render_template('new_index.html', bibliotecas=bibliotecas, livros=livros)

@app.route('/adicionar_livro', methods=['GET', 'POST'])
def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano = request.form['ano']
        biblioteca_id = request.form['biblioteca_id']

        # Validar dados
        if not titulo or not autor or not ano or not biblioteca_id:
            flash('Erro: Todos os campos são obrigatórios.', 'error')
            return redirect('/')

        try:
            ano = int(ano)
            biblioteca_id = int(biblioteca_id)
        except ValueError:
            flash('Erro: O ano e o ID da biblioteca devem ser números inteiros válidos.', 'error')
            return redirect('/')

        # Criar objeto Livro e adicionar ao banco de dados
        livro = Livro(titulo=titulo, autor=autor, ano_de_publicacao=ano, biblioteca_id=biblioteca_id)
        db.session.add(livro)
        db.session.commit()

        flash('Livro adicionado com sucesso!', 'success')
        return redirect('/')

    # Se o método não for POST, renderiza o template com o formulário
    bibliotecas = Biblioteca.query.all()
    return render_template('adicionar_livro.html', bibliotecas=bibliotecas)

@app.route('/adicionar_biblioteca', methods=['GET', 'POST'])
def adicionar_biblioteca():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        nova_biblioteca = Biblioteca(nome=nome, endereco=endereco)

        db.session.add(nova_biblioteca)
        db.session.commit()
        
        return redirect('/')
    
    return render_template('adicionar_biblioteca.html')

if __name__ == '__main__':
    app.run(debug=True)
