from sqlalchemy import MetaData, Table
from sqlalchemy import Column, BigInteger


metadata = MetaData()

users = Table("users", metadata,
              Column("id", BigInteger, primary_key=True),
              )
