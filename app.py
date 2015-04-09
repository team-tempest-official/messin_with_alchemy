import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from random import randint

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


class TutorialApp(App):
    layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
    
    ## self.layout.children[0].text <- asta e textul din text input
    ## fa ce vrei sa faci cu el in eveniment1
    
    def eveniment1(self,*args):
        print "ev1"
        p = Person(name=self.layout.children[0].text, job="football player")
        session.add(p)
        session.commit()
        self.layout.children[2].text = self.layout.children[0].text    
        
    def eveniment2(self,*args):
        id_ = randint(1, session.query(Person).count())
        p = session.query(Person).get(id_)
        self.layout.children[1].text = p.name
        print "ev2", p.id

    def build(self):
        self.layout.add_widget(Button(text='Add to database', size_hint_x=None, width=100))
        self.layout.add_widget(Button(text='Get'))
        self.layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        self.layout.add_widget(Button(text='World 2'))
        self.layout.add_widget(TextInput())
        self.layout.children[4].bind(on_press=self.eveniment1)
        self.layout.children[3].bind(on_press=self.eveniment2)
        return self.layout
        
if __name__ == "__main__":
    TutorialApp().run()
