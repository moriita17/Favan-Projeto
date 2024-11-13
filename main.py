from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

usuarios = []
    
class Usuarios(BaseModel):
    nome: str
    username: str

@app.get("/")
def home():
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
    
    
    
