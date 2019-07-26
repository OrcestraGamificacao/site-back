from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def initialize_sql(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
