import mysql.connector
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",         
        password="1312",    
        database="bancocrud" 
    )
    
    class Produto(BaseModel):
      produto: str
      preco: float(input)
      quantidade: int(input)

#CREATE
@app.post("/Usuarios/")
def inserir_usuario(nome, login):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "INSERT INTO usuarios (nome, login) VALUES (%s, %s)"
        cursor.execute(query, (nome, login))

        conexao.commit()
        print("Usuário inserido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()
        
#READ
@app.get("/usuarios/")
def ler_usuarios():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "SELECT id, nome, login FROM usuarios"
        cursor.execute(query)

        usuarios = cursor.fetchall()

        return [{"id": id, "nome": nome, "login": login} 
                for id, nome, login in usuarios]
    except mysql.connector.Error as err:
        return {"Erro": str(err)}
    finally:
        cursor.close()
        conexao.close()

#UPDATE
@app.put("/usuarios/editar/{id}")
def atualizar_usuario(id, nome=None, login=None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        set_clause = []
        params = []

        if nome:
            set_clause.append("nome = %s")
            params.append(nome)
        if login:
            set_clause.append("login = %s")
            params.append(login)

        set_clause_str = ", ".join(set_clause)
        query = f"UPDATE usuarios SET {set_clause_str} WHERE id = %s"
        params.append(id)

        cursor.execute(query, tuple(params))

        conexao.commit()
        print("Usuário atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()
        
#DELETE
@app.delete("/usuarios/apagar/{id}")
def excluir_usuario(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (id,))

        conexao.commit()
        print("Usuário excluído com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()
        
# CREATE 
@app.post("/Produtos/")
def inserir_produto(produto, preco, quantidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "INSERT INTO produtos (produto, preco, quantidade) VALUES (%s, %s, %s)"
        cursor.execute(query, (produto, preco, quantidade))

        conexao.commit()
        print("Produto inserido com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()
        
# READ
@app.get("/produtos/")
def ler_produtos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "SELECT id, produto, preco, quantidade FROM produtos"
        cursor.execute(query)

        produtos = cursor.fetchall()

        return [{"id": id, "produto": produto, "preco": preco, "quantidade": quantidade} 
                for id, produto, preco, quantidade in produtos]
    except mysql.connector.Error as err:
        return {"Erro": str(err)}
    finally:
        cursor.close()
        conexao.close()
        
#UPDATE      
@app.put("/produtos/editar/{id}")
def atualizar_produto(id, produto=None, preco=None, quantidade=None):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        set_clause = []
        params = []

        if produto:
            set_clause.append("produto = %s")
            params.append(produto)
        if preco:
            set_clause.append("preco = %s")
            params.append(preco)
        if quantidade:
            set_clause.append("quantidade = %s")
            params.append(quantidade)

        set_clause_str = ", ".join(set_clause)
        query = f"UPDATE produtos SET {set_clause_str} WHERE id = %s"
        params.append(id)

        cursor.execute(query, tuple(params))

        conexao.commit()
        print("Produto atualizado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()
        
# DELETE
@app.delete("/produtos/apagar/{id}")
def excluir_produtos(id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        query = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(query, (id,))

        conexao.commit()
        print("Produto excluído com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        cursor.close()
        conexao.close()