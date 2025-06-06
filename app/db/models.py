from sqlalchemy import Column, Integer, String
from .database import Base

class Producao(Base):
    __tablename__ = "producao"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(String)

class Processamento(Base):
    __tablename__ = "processamento"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(String)

class Comercializacao(Base):
    __tablename__ = "comercializacao"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(String)

class Importacao(Base):
    __tablename__ = "importacao"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(String)

class Exportacao(Base):
    __tablename__ = "exportacao"
    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String, index=True)
    quantidade = Column(String)
