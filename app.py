import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
    
class TutorialApp(App):
    layout = GridLayout(cols=2, row_force_default=True, row_default_height=40)
    
    ## self.layout.children[0].text <- asta e textul din text input
    ## fa ce vrei sa faci cu el in eveniment1
    
    def eveniment1(self,*args):
        self.layout.children[2].text = self.layout.children[0].text    
        
    def eveniment2(self,*args):
        #self.layout.children[1].text = Ceva ce scoti din baza de date
        pass
        
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
