import requests
from db_test import create_facts_table, launch_db, start_engine
# from db_test import pics as pic_table
from datetime import datetime
import base64
import shutil

def get_3_pics(pic_table, engine):
    i: int = 0
    for i in range(0, 3):
        r = requests.get("https://thiscatdoesnotexist.com/", stream=True)
        img_name = "cat" + str(i) + ".jpg"
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


def get_10_facts(facts, engine):
    i: int = 0
    for i in range(0, 10):
        r = requests.get("https://catfact.ninja/fact")
        print(r.json()["fact"])
        f: str = r.json()["fact"]
        ins = facts.insert()
        ins = facts.insert().values(
        fact_content=f,
        created_on=datetime.now(),
        updated_on=datetime.now(),
        )
        print(str(ins), ins.compile().params)
        conn = engine.connect()
        result = conn.execute(ins)
        # session.
        # result = engine.connection.execute(ins)
        # stmt = (
        #     facts.insert(facts).values(fact_content=f)
        # )
        i += 1


if __name__ == "__main__":
    engine = start_engine()
    facts = create_facts_table(engine)
    pics = launch_db(engine)
    # get_10_facts(facts, engine)
    get_3_pics(pics, engine)