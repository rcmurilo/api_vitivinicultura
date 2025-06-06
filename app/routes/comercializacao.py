from fastapi import APIRouter, Depends
from app.auth.security import authorize_user
from app.db.database import SessionLocal
from app.db.models import Comercializacao
from app.services.scrapers import fetch_and_save

router = APIRouter()

@router.get("/comercializacao")
def get_comercializacao(token: str = Depends(authorize_user)):
    db = SessionLocal()
    return fetch_and_save("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04", Comercializacao, db)
