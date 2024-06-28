from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instância do SQLAlchemy

class Biblioteca(db.Model):
    __tablename__ = 'bibliotecas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Livro(db.Model):
    __tablename__ = 'livros'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    ano_de_publicacao = db.Column(db.Integer, nullable=False)
    biblioteca_id = db.Column(db.Integer, db.ForeignKey('bibliotecas.id'), nullable=False)
    biblioteca = db.relationship('Biblioteca', backref=db.backref('livros', lazy=True))

    def __init__(self, titulo, autor, ano_de_publicacao, biblioteca_id):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.biblioteca_id = biblioteca_id
