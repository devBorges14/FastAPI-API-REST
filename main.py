"""
Projeto: Criando uma API REST Simples
O objetivo deste projeto é desenvolver uma API REST para gerenciar um sistema de usuários. A API permitirá criar, listar, atualizar e excluir usuários por meio de requisições HTTP.

Passos do Projeto
    1)Configuração do Ambiente
        Escolher a linguagem de programação (Python).
    2)Instalar as dependências necessárias (Flask ou FastAPI).

    3)Criar a Estrutura do Projeto

    4) Definir os Endpoints da API
        GET /usuarios → Lista todos os usuários.
        GET /usuarios/{id_usuarios} → Procura um usuário por ID.
        POST /add/usuarios → Cria um novo usuário.
        PUT /edit/usuarios/{id} → Atualiza um usuário existente.
        DELETE /delete/usuarios/{id} → Remove um usuário.
        Implementação da API

    5) Criar uma estrutura para armazenar os usuários (pode ser um dicionário ou banco de dados).
    6)Criar funções para cada endpoint, processando as requisições e retornando respostas no formato JSON.
Testar a API
    	Utilizar o Postman ou cURL para testar os endpoints.
        Verificar se todas as operações funcionam corretamente.

Melhorias e Segurança
    Adicionar validações nos dados recebidos.
    Implementar autenticação, se necessário. 
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Caminho do arquivo JSON
ARQUIVO_JSON = "usuarios.json"

# Função para carregar os usuários do arquivo
def carregar_usuarios():
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Função para salvar os usuários no arquivo
def salvar_usuarios():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

# Carrega os usuários ao iniciar a API
usuarios = carregar_usuarios()
# Modelo para receber os dados
class Usuario(BaseModel):
    nome: str
    email: str

# Visualizar todos
@app.get("/usuarios") 
def lista_de_usuarios():
    return usuarios # Retornando os usuários

# Visualizar por id
@app.get("/usuarios/{id_usuarios}")
def procurar_por_id(id_usuarios: int): # Recebendo o id do usuário
    if id_usuarios in usuarios: # Verificando se o ID existe
        return usuarios[id_usuarios] # Retornando o usuário com o ID selecionado
    else:
        return "Error: ID inexistente"
# Adicionar
@app.post("/add/usuarios")
def adicionar_usuario(id: int, nome: str, gmail: str): # Adicionando um novo usuário
    try:
        novo_usuario = {"nome": nome, "gmail": gmail} # Criando um novo usuário
        usuarios[id] = novo_usuario # Adicionando o novo usuário ao dicionário
        return ({"mensagem": "Usuário criado com sucesso!", "usuario": novo_usuario})

    except ValueError as e:
        raise HTTPException(status_code=400, detail="Erro de validação: " + str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno: " + str(e))

# Editar usuário
@app.put("/edit/usuarios/{id}")
def editar_usuario(id: int, usuario_alterado: Usuario):
    for indice, chave in enumerate(usuarios):
        if chave == id:
            usuarios[chave]["nome"] = usuario_alterado.nome
            usuarios[chave]["gmail"] = usuario_alterado.email
            return {"mensagem": "Usuário atualizado com sucesso!", "usuario": usuarios[chave]}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
# Excluir
@app.delete("/delete/usuarios/{id}")
def excluir_usuario(id: int):
    print("Usuários antes da exclusão:", usuarios)  # Debug para ver os usuários antes

    if id not in usuarios:  # IDs são inteiros no dicionário, então não converta para string!
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    del usuarios[id]  # Remove o usuário corretamente
    return {"mensagem": "Usuário excluído com sucesso!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
