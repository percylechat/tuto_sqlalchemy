from datetime import datetime
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    create_engine,
    # sessionmaker,
)

# let 
# metadata = MetaData()
# facts = Table(
#     "facts",
#     metadata,
#     Column("fact_id", Integer(), primary_key=True),
#     Column("total_facts", Integer(), autoincrement=True),
#     Column("fact_content", String(), nullable=False, unique=True),
#     Column("created_on", DateTime(), default=datetime.now),
#     Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
# )

def start_engine():
    engine = create_engine('sqlite:///facts.db', echo=True)
    return engine

# def create_session(engine):
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session

def launch_db(engine):
    # engine = create_engine('sqlite:///facts.db', echo=True)
    metadata = MetaData()
    facts = Table(
    "facts",
    metadata,
    Column("fact_id", Integer(), primary_key=True, autoincrement=True),
    Column("total_facts", Integer(), autoincrement=True),
    Column("fact_content", String(), nullable=False, unique=True),
    Column("created_on", DateTime(), default=datetime.now),
    Column("updated_on", DateTime(), default=datetime.now, onupdate=datetime.now),
    )
    metadata.create_all(engine)
    return facts
