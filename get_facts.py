import requests
from db_test import launch_db, start_engine
from datetime import datetime


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
    facts = launch_db(engine)
    get_10_facts(facts, engine)
