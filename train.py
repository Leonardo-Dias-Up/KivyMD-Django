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

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        
        MDLabel:
            text: 'Mudar senha'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()
    
    MDFloatLayout:
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Codigo enviado por email'
        
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Nova senha:'
        
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha:'
        
        ButtonFocus:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Recadastrar!'
            focus_color: app.theme_cls.accent_color
            unfocus_color: app.theme_cls.primary_color

<ClickableTextFieldRound_Password>:
    size_hint_y: None
    height: text_field_password.height

    MDTextField:
        id: text_field_password
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"
        on_text_validate:
            root.inputtextfn()
            root.text_validate()

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
    height: text_field.height
            
    MDTextField:
        id: text_field
        hint_text: root.hint_text
        #helper_text: "user@gmail.com"
        icon_left: "email"
        on_text_validate:
            root.inputtextfn()
            root.text_validate()

       
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
            #root.ids.userinput.dispatch('on_text_validate')
        on_release: root.old()
'''

class ClickableTextFieldRound_Password(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
print(ClickableTextFieldRound_Password.text)
class ClickableTextFieldRound_Email(MDRelativeLayout):
    text = StringProperty()
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
    
    def get_pass(self):
        text_field_password = self.navigation_bar.get_screen('text_field_password').ids.text_field_password.text
        print(text_field_password)

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
                    on_release=self.show_data,
                )
        screen.add_widget(button)
        return screen
    
    def show_data(self, obj):
        print(self.navigation_bar.text)
        
MyApp().run()

