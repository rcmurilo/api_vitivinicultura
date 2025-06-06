from fastapi import HTTPException
from bs4 import BeautifulSoup
import pandas as pd
import requests

def fetch_and_save(url: str, model, db):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    if not table:
        raise HTTPException(status_code=404, detail="Tabela não encontrada")
    rows = table.find_all('tr')
    data = [[cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])] for row in rows]
    df = pd.DataFrame(data[1:], columns=data[0])
    db.query(model).delete()
    for _, row in df.iterrows():
        db_entry = model(produto=row[0], quantidade=row[1])
        db.add(db_entry)
    db.commit()
    print(df)
    return {"message": f"Dados de {model.__tablename__} carregados e salvos com sucesso."}
