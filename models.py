from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///testdb.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    job = Column(String)

    def repr(self):
        return "<Person(name = '%s', job = '%s')>" % (self.name, self.job)



Base.metadata.create_all(engine)

Messi = Person(name='Messi', job='Football player')
Mutu = Person(name='Mutu', job='Football player')
Marica = Person(name='Marica', job='Football player')
Torje = Person(name='Torje', job='Football player')
Hagi = Person(name='Hagi', job='Football player')
Goian = Person(name='Goian', job='Football player')

session.add_all([Messi, Mutu, Marica, Torje, Hagi, Goian])
session.commit()

with open('players', 'r') as f:
    for line in f:
        t = Person(name=line.strip(), job='Footbal player')
        session.add(t)

session.commit()
