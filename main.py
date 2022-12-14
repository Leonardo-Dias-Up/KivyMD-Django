''' 

#########################################################

Anotações para identificarmos as classes e os ids
precisamos colocar o id quando chamarmos as classes:

obs: por enquanto estamos usando StringProperty como ids

    ClickableTextFieldRound_Email:
        id: text_field_email

    ClickableTextFieldRound_Password:
        id: text_field_password

#########################################################

Referênciamento de Widget com clickaction

https://kivy.org/doc/stable/guide/lang.html#referencing-widgets

'''

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen


KV = '''
<Login>:
    
    MDIcon:
        icon:"language-python"
        pos_hint:{"center_x": 0.5, "center_y": 0.8}
        font_size: '75sp'
    
    MDTextField:
        id: text_field_email
        text: root.text_field_email
        hint_text: root.hint_text
        #helper_text: "user@gmail.com"
        icon_left: "email"
        size_hint_x: None
        width: "300dp"
        hint_text: "Email"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_text: 
            #root.check_status(button_one, text_field_email)

    
    MDTextField:    
        name : 'text_field_password'
        id: text_field_password
        hint_text: root.hint_text
        text: root.text_field_password
        password: True
        icon_left: "key-variant"
        size_hint_x: None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_text: 
            #root.check_status(button_one, text_field_password)
            
            
    MDIconButton:
        icon: "eye-off"
        theme_text_color: "Hint"
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .4}
        #pos: text_field_password.width - self.width + dp(8), 0
        size_hint_x: None
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field_password.password = False if text_field_password.password is True else True      


    Button:
        name:'button_one'
        id: button_one
        size_hint: None, None
        size: 300, 40
        pos_hint: {'center_x': .5, 'center_y': .3}
        text: 'Login'
        #font_size: 12
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        on_press: 
            root.btn_after()
            root.check_status(button_one, text_field_email, text_field_password)
        on_release: root.btn_pos()
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'MyApp'
            left_action_items: [['menu', lambda x: x]]
            right_action_items: 
                [
                ['home', lambda x: x, 'Home', 'Home'],
                ['dots-vertical', lambda x: x],
                ]
        TelaLogin:
           
<TelaLogin@FloatLayout>:

    Login:

        
'''

class TelaLogin(FloatLayout):
           
    class Login(MDRelativeLayout):
        text_field_email = StringProperty()
        hint_text = StringProperty()
        text_field_password = StringProperty()
        hint_text = StringProperty()
        
        def btn_after(self):
                self.ids['button_one'].background_color = [1, 0, 1, 1] 
        def btn_pos(self):
                self.ids['button_one'].background_color = [0, 0 , 0, 0] 
            
        def check_status(self, btn, text_email, text_password):
                                   
            print('button state is: {state}'.format(state=btn.state))
            print('text input email is: {txt}'.format(txt=text_email.text))
            print('text input password is: {txt}'.format(txt=text_password.text))

class MyApp(MDApp):
    
    def build(self):
        
        screen = Screen()
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '800'
        self.theme_cls.theme_style = 'Dark'
        self.login_inicial = Builder.load_string(KV)
        screen.add_widget(self.login_inicial)
        
        return screen
    
MyApp().run()
