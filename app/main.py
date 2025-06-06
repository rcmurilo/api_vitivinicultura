from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.security import authenticate_user
from app.routes import producao, processamento, comercializacao, importacao, exportacao
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return authenticate_user(form_data)

app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)
