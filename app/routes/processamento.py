from fastapi import APIRouter, Depends
from app.auth.security import authorize_user
from app.db.database import SessionLocal
from app.db.models import Processamento
from app.services.scrapers import fetch_and_save

router = APIRouter()

@router.get("/processamento")
def get_processamento(token: str = Depends(authorize_user)):
    db = SessionLocal()
    return fetch_and_save("http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03", Processamento, db)
