import requests
# from db_test import create_facts_table, launch_db, start_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import base64
import shutil
from main_sqlalchemy import Fact, Image,engine,Base, Session

def get_3_pics(pic_table, engine):
    i: int = 0
    for i in range(0, 3):
        Session = sessionmaker(bind = engine)
        session = Session()
        session.add(pic_table)
        nbr_row = session.query(pic_table).count()
        r = requests.get("https://thiscatdoesnotexist.com/", stream=True)
        img_name : str = "cat" + str(i + nbr_row) + ".jpg"
        with open(img_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        ins = pic_table.insert()
        ins = pic_table.insert().values(
        picture=img_name,
        created_on=datetime.now(),
        updated_on=datetime.now(),
        )
        conn = engine.connect()
        result = conn.execute(ins)
        i += 1


def get_10_facts(engine):
    i: int = 0
    local_session=Session(bind=engine)
    for i in range(0, 10):
        r = requests.get("https://catfact.ninja/fact")
        print(r.json()["fact"])
        f: str = r.json()["fact"]
        new_fact = Fact(fact_content=f)
        local_session.add(new_fact)
        local_session.commit()
        # ins = facts.insert()
        # ins = facts.insert().values(
        # fact_content=f,
        # created_on=datetime.now(),
        # updated_on=datetime.now(),
        # )
        # print(str(ins), ins.compile().params)
        # conn = engine.connect()
        # result = conn.execute(ins)
        i += 1


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # engine = start_engine()
    # facts = create_facts_table(engine)
    # pics = launch_db(engine)
    get_10_facts(engine)
    get_3_pics(pics, engine)