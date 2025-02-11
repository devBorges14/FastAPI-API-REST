## API com FastAPI
O objetivo deste projeto é desenvolver uma API REST para gerenciar um sistema de usuários. 
A API permitirá criar, listar, atualizar e excluir usuários por meio de requisições HTTP

## Funcionalidades
- GET /usuarios → Lista todos os usuários.
- GET /usuarios/{id_usuarios} → Procura um usuário por ID.
- POST /add/usuarios → Cria um novo usuário.
- PUT /edit/usuarios/{id} → Atualiza um usuário existente.
- DELETE /delete/usuarios/{id} → Remove um usuário.
    Implementação da API

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework web principal do projeto.
    <a href="https://fastapi.tiangolo.com">_Documentação do FastAPI_<a>
    
## Pré Requisitos
Antes de executar o projeto, certifique-se de ter as ferramentas necessárias instaladas:

1. **Python 3+**  
   - Faça o download em [python.org/downloads](https://www.python.org/downloads/).
       
   Após a instalação, verifique se o Python foi instalado corretamente:
   ```bash
   python --version
   ```
   ou
   ```bash
   python3 --version
   ```

2. **Dependências Python**   
Instale as dependências listadas no arquivo `requirements.txt` com o comando:  
```bash
pip install -r requirements.txt
```
**Ou instale manualmente:**  
    - **uvicorn **: Um servidor ASGI para rodar o FastAPI.
     ```bash
     pip install uvicorn 
     ```
    - **fastapi **: Para usar a FastAPI.
     ```bash
     pip install fastapi 
     ```
    - **pydantic  **: validação e modelagem de dados com BaseModel.
     ```bash
     pip pydantic   
     ``` _(Já vem com FastAPI)_

---
## Como Rodar o Projeto

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/devBorges14/FastAPI-API-REST
   cd FastAPI-API-REST
   ```
2. **Instale os pré-requisitos** conforme listado acima.

3. **Execute o programa**:
   ```bash
   python main.py
   ```
---

## Recursos Adicionais

- [Documentação da FastAPI](https://fastapi.tiangolo.com)  

---
