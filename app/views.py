from flask import render_template, url_for, redirect
from app import app
from app.models import Prod,Categ

usuario_logado = False
categs= [
    Categ(1, 'Evas medicinais'),
    Categ(2, 'Especiarias e temperos'),
    Categ(3, 'Grãos e sementes'),
    Categ(4, 'Frutas Cristalizadas'),
    Categ(5, 'Cereais'),
    Categ(6, 'Castanhas'),
    Categ(7, 'Méis'),
    Categ(8, 'azeites e óleos')
]
prods=[
    Prod(1,'Mel de Cajú', 20, 15, '22-03-2018', 7)
]

@app.route('/categorias/inserir')
def inserir_categorias():
    return render_template('inserir_categorias.html',
    categs = categs, 
    msg_nome = "Digite a Categoria"
  
    )

@app.route('/categorias/listar')
def listar_categorias():
    return render_template('listar_categorias.html',
    categs = categs)

@app.route('/categorias/editar/<int:id>')
def editar_categorias(id):
    for categoria in categs:
        if categoria.id == id:
            return render_template('editar_categorias.html',categoria_selecionada = categoria, categs = categs)

@app.route('/produto/inserir')
def inserir_produtos():
    return render_template('inserir_produtos.html',  
    categs = categs,
    msg_id = "Digite o código",
    msg_nome = "Digite o Nome do Produto",
    msg_qtde = "Digite a quantidade de Produtos",
    msg_preco = "Digite o preco",
    msg_data = "dd/mm/aaaa",
    id_categs_selecionada = 5,
    )

@app.route('/produto/listar')
def listar_produtos():
    return render_template('listar_produtos.html',
    prod = prods    
    )

@app.route('/produto/editar/<int:id>')
def editar_produtos(id):
    for prod in prods:
        if prod.id == id:
            return render_template('editar_produtos.html',produto_selecionada = prod)

@app.route('/categs/dropdown/<int:id>')
def dropdown(id):
    for categ in categs:
        if categ.id == id:
            return render_template('dropdown.html', id_categ_selecionada = categ.id, list_categs = categs, nome = categ.nome)
            return redirect(url_for('home'))

@app.route('/')
def home():
    return render_template('index.html', list_categs = categs)
    return redirect(url_for('home'))
