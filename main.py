from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

usuarios = []
produtos = []
    
class Usuarios(BaseModel):
    nome: str
    username: str
    
class Produto(BaseModel):
    nome: str
    preco: float
    quantidade: int

@app.get("/Usuarios")
def Listarusuarios():
    return {"Usuarios": usuarios}

@app.post("/usuarios/inserir")
def InserirUsuario(usuario: Usuarios):
    usuarios.append ([usuario.nome, usuario.username])
    return {"Mensagem": f"O Usuario {usuario.nome} foi cadastrado com sucesso"}

@app.put("/usuarios/editar/{id}")
def editarUsuario(id: int, usuario: Usuarios):
    usuarios[id - 1] = [usuario.nome, usuario.username]
    return {"Mensagem": f"O Usuario n {id} foi editado com sucesso"}

@app.delete("/usuarios/apagar/{id}")
def apagarUsuario(id: int):
    usuarios.pop(id-1)
    return {"Mensagem": f"O Usuario n{id} foi apagado com sucesso"}

@app.get("/produtos")
def listarProdutos():
    return {"Produtos": produtos}

@app.post("/produtos/inserir")
def inserirProduto(produto: Produto):
    produtos.append({
        "nome": produto.nome,
        "preco": produto.preco,
        "quantidade": produto.quantidade
    })
    return {"Mensagem": f"O Produto {produto.nome} foi cadastrado com sucesso"}

@app.put("/produtos/editar/{id}")
def editarProduto(id: int, produto: Produto):
    produtos[id - 1] = {
        "nome": produto.nome,
        "preco": produto.preco,
        "quantidade": produto.quantidade
    }
    return {"Mensagem": f"O Produto n{id} foi editado com sucesso"}

@app.delete("/produtos/apagar/{id}")
def apagarProduto(id: int):
    produtos.pop(id - 1)
    return {"Mensagem": f"O Produto n{id} foi apagado com sucesso"}
    
    
    
