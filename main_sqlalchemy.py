
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os

# prepare db name with absolute path 
BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(BASE_DIR,'cats.db')

#allows to create db and tables
Base=declarative_base()

#trully create db, with echo as printing sql queries
engine=create_engine(connection_string,echo=True)

#create session so we vcan access db and tables from anywhere
Session=sessionmaker()

""""
class Fact
    id int
    fact_content str
    date_created datetime
"""

""""
class Image
    id int
    img_name str
    date_created datetime
"""

class Fact(Base):
    __tablename__='facts'
    id=Column(Integer(),primary_key=True)
    fact_content=Column(String,nullable=False,unique=True)
    date_created=Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return f"<Fact number={self.id} is={self.fact_content}>"

class Image(Base):
    __tablename__='images'
    id=Column(Integer(),primary_key=True)
    img_name=Column(String,nullable=False,unique=True)
    date_created=Column(DateTime(),default=datetime.utcnow)

# new_user=User(id=1,username="JOnathan",email="jona@jona.com")
# print(new_user)