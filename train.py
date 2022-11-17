from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
KV = '''

<ClickableTextFieldRound_Password>:
    size_hint_y: None
    height: text_field_password.height

    MDTextField:
        id: text_field_password
        hint_text: root.hint_text
        text: root.text_field_password
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field_password.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field_password.password = False if text_field_password.password is True else True

<ClickableTextFieldRound_Email>:
    size_hint_y: None
    height: text_field_email.height
            
    MDTextField:
        id: text_field_email
        text: root.text_field_email
        hint_text: root.hint_text
        #helper_text: "user@gmail.com"
        icon_left: "email"
       
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
    MDIcon:
        icon:"language-python"
        pos_hint:{"center_x": 0.5, "center_y": 0.8}
        font_size: '75sp'
        
    ClickableTextFieldRound_Email:
        size_hint_x: None
        width: "300dp"
        hint_text: "Email"
        pos_hint: {"center_x": .5, "center_y": .5}
        
        
    ClickableTextFieldRound_Password:
        size_hint_x: None
        width: "300dp"
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .4}
        
        
    Button:
        id: button_one
        size_hint: None, None
        size: 300, 40
        pos_hint: {'center_x': .5, 'center_y': .3}
        text: 'Login'
        #font_size: 12
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        on_press: 
            root.new()
            on_press : app.get_data()

        on_release: root.old()
'''

class ClickableTextFieldRound_Password(MDRelativeLayout):
    text_field_password = StringProperty()
    hint_text = StringProperty()

class ClickableTextFieldRound_Email(MDRelativeLayout):
    text_field_email = StringProperty()
    hint_text = StringProperty()

class SenhaCard(MDCard):
    ...

class TelaLogin(FloatLayout):
    def ValidaLogin(self):
        print('Valida Login')
    
    def new(self):
            self.ids['button_one'].background_color = [1, 0, 1, 1] 
    
    def old(self):
            self.ids['button_one'].background_color = [0, 0, 0, 0] 

class MyApp(MDApp):
    def build(self):
        screen = Screen()
        
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '800'
        self.theme_cls.theme_style = 'Dark'
        self.navigation_bar = Builder.load_string(KV)

        screen.add_widget(self.navigation_bar)
        
        button = MDIconButton(
                    icon="language-python",
                    pos_hint={"center_x": 0.4, "center_y": 0.8},
                    on_release=self.get_data,
                )
        screen.add_widget(button)
        return screen
    
    def get_data(self):
        try:
            print(type(self.root.text_field_email.ids))
        except AttributeError:
            print(5*'**','Continue Tentando',5*'*')
        print("The data of text field is :: ",self.root.ids)
        print("The data of text field is :: ",self.root.ids)
            
        
MyApp().run()
