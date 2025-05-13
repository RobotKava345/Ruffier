from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import *
from ruffier import *
from kivy.uix.popup import Popup

BG_COLOR = "#392e8f"
BTN_COLOR = "#f2f2f2"
Window.clearcolor = BG_COLOR
p1, p2, p3 = 0, 0 ,0
age = 7

class InstrucktionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instruction)

        lbl1 = Label(text="Введіть [b] iм'я: [/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)
        lbl2 = Label(text="Введіть [b] вiк: [/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)
        self.name_input = MyTextInput()
        self.age_input = MyTextInput()
        start_button = MyButton(text="[b] Почати [/b]")
        start_button.on_press = self.next

        v_line = BoxLayout(orientation='vertical',
                           size_hint=(0.9, 1),
                           pos_hint={"center_x": 0.5},
                           spacing=10,
                           padding=10)
        v_line.add_widget(instr)
        v_line.add_widget(lbl1)
        v_line.add_widget(self.name_input)
        v_line.add_widget(lbl2)
        v_line.add_widget(self.age_input)
        v_line.add_widget(start_button)

        self.add_widget(v_line)
        
    def next(self):
        if self.name_input.text !='' and self.age_input.text.strip() !='':
            try:
                global age
                self.age = int(self.age_input.text.strip())
                if age >= 7:
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'pulse'
                else:
                    error = Popup(title = 'Вік має бути більше семи!', size_hint = (0.6, 0.3), auto_dismiss=True)
                    error.open()

            except:
                error = Popup(title = 'Вік має бути цілим числом більше семи!', size_hint = (0.6, 0.3), auto_dismiss=True)
                error.open()
        

class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = BG_COLOR
        self.font_size = 20
        self.size_hint = (0.5, None)
        self.pos_hint = {"center_x": 0.5}
        self.height = "30sp"
        self.markup = True


class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.size_hint = (0.5, None)
        self.pos_hint = {"center_x": 0.5}
        self.height = "30sp"


class PulseScreen (Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test1)

        lbl1 = Label(text="Введіть [b] результат: [/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)

        self.result_input = MyTextInput()
        
        start_button = MyButton(text="[b] Почати [/b]")
        start_button.on_press = self.next

        v_line = BoxLayout(orientation='vertical',
                           size_hint=(0.9, 1),
                           pos_hint={"center_x": 0.5},
                           spacing=10,
                           padding=10)
        v_line.add_widget(instr)
        v_line.add_widget(lbl1)
        v_line.add_widget(self.result_input)
       

        v_line.add_widget(start_button)

        

        self.add_widget(v_line)

    def next(self):
            
    
            try:
                global p1 
                p1 = int(self.result_input.text.strip())
                
                self.manager.transition.direction = 'left'
                self.manager.current = 'sits'
                
            except:
                error = Popup(title = 'Пульс має бути цілим числом !', size_hint = (0.6, 0.3), auto_dismiss=True)
                error.open()

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resultLabel = Label(text = "",)
        
    
        v_line = BoxLayout(orientation='vertical',
                           size_hint=(0.9, 1),
                           pos_hint={"center_x": 0.5},
                           spacing=10,
                           padding=10)
        v_line.add_widget(self.resultLabel)
        self.on_enter = self.before

    def before(self):
        result = test(p1, p2, p3, age)
        self.resultLabel.text =f"Індекс Руф'є {result}"

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrucktionScreen(name = 'instr'))
        sm.add_widget(PulseScreen (name = 'pulse'))
        sm.add_widget(ResultScreen(name = 'result'))
        # буде показано FirstScr, тому що він доданий першим. Це можна змінити ось так:
        # sm.current = 'second'
        return sm

app = HeartCheck()
app.run()