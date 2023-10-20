from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 550)

butns = ['C', 'Esc', '√', '/',
        '7', '8', '9', '*',
        '4', '5', '6', '-',
        '1', '2', '3', '+',
        '00', '0', '.'
        ]

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class MyApp(App):

    def __init__(self):
        super().__init__()



        self.got_but = [Button(text = x, font_size = 30, size = (100, 70), size_hint =(None, None), on_press = self.add_number) for x in butns]

        print(self.got_but)


        self.Button_res = Button(text = '=', font_size = 30, size = (100, 70), size_hint =(None, None), pos = (100, 100))
        self.TextIn = Label(text = '', font_size = 30, size_hint = (1, 0.3))
        self.Result = Label(text = '0', font_size = 30, size_hint = (1, 0.3), halign = 'right')

    def add_number(self, instance):
        a = []
        for i in self.TextIn.text:
            a.append(i)
        try:
            if a[-1] in ['/', '*', '+', '-'] and a[-2] in ['/', '*', '+', '-']:
                del a[-1]
                self.TextIn.text = ''.join(a)
        except:
            pass

        if str(instance.text) =='C':
            self.TextIn.text = ''
            self.Result.text = self.TextIn.text
        elif str(instance.text) == 'Esc':
            try:
                a = []
                for i in self.TextIn.text:
                    a.append(i)
                del a[-1]
                self.TextIn.text = ''.join(a)
            except:
                pass
        elif str(instance.text) == '√':
            try:
                self.Result.text = str(eval(self.TextIn.text) ** 0.5)
            except:
                pass
        else:
            self.TextIn.text += str(instance.text)
            try:

                self.Result.text = str(eval(self.TextIn.text))
            except:
                pass
    
    def build(self):
        bx = BoxLayout(orientation = 'vertical')
        gl = GridLayout(cols = 4)

        bx.add_widget(self.TextIn)
        bx.add_widget(self.Result)



        for i in self.got_but:
            gl.add_widget(i)
        
        gl.add_widget(self.Button_res)

        bx.add_widget(gl)

        return bx


if __name__ == '__main__':
    MyApp().run()

