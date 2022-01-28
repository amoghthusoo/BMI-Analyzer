from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from ui_home import screens


Window.size = (365, 650)


class HomeScreen(Screen):
    pass

class DeveloperScreen(Screen):
    pass

class InfoScreen(Screen):
    pass

class HelpScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name = 'home'))
sm.add_widget(InfoScreen(name = 'info'))

class BMI_Calc(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.app = Builder.load_string(screens)
        return self.app 

    
    def callback_calculate(self, _name, weight, height):
        
        self._name = _name
        self.weight = weight
        self.height = height

        self.close_button = MDFlatButton(text = 'OK', on_release = self.callback_dialog_close)
        self.dialog_window = MDDialog(size_hint = (0.9, 1), buttons = [self.close_button])
        
        if self._name == '' or self.weight == '' or self.height == '':
            self.dialog_window.title = 'INVALID INPUT'
            self.dialog_window.open()
        
        else:
            try:
    
                self.bmi = float(self.weight)/float(self.height)**2
                self.dialog_window.title = 'Hi ' + self._name + ', Your BMI is :'
                self.dialog_window.text = '                                                                           ' + str(self.bmi)
                self.dialog_window.open()            
            except:
                self.dialog_window.title = 'INVALID INPUT'
                self.dialog_window.open()
        

    def callback_dialog_close(self, obj):
        self.dialog_window.dismiss()

    def callback_help(self):
        self.root.transition.direction = 'left'
        self.root.current = 'help'

    def callback_return_home(self):
        self.root.transition.direction = 'right'
        self.root.current = 'home'

root = BMI_Calc()
if __name__ == '__main__':
    root.run()
