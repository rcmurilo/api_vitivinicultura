from fastapi import APIRouter, Depends
from app.auth.security import authorize_user
from app.db.database import SessionLocal
from app.db.models import Producao
from app.services.scrapers import fetch_and_save

router = APIRouter()

@router.get("/producao")
def get_producao(token: str = Depends(authorize_user)):
    db = SessionLocal()
    return fetch_and_save("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02", Producao, db)
