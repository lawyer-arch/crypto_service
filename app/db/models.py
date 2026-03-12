from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, BigInteger

Base = declarative_base()


class Prices(Base):

    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    timestamp = Column(BigInteger, index=True)