   
            

                
from kivymd.app import MDApp

from kivy.core.text import LabelBase

import pyrebase

from kivymd.uix.behaviors import FakeRectangularElevationBehavior

from kivymd.uix.floatlayout import MDFloatLayout

from kivy.lang import Builder

from kivy.core.window import Window

from kivy.uix.screenmanager import Screen, ScreenManager

import webbrowser



firebaseConfig = {
    'apiKey': "AIzaSyDK-986TqJKhsg9gfL1mbqK6g2GQwu8h1g",
    'authDomain': "cadastroesdras.firebaseapp.com",
    'projectId': "cadastroesdras",
    'databaseURL': "https://cadastroesdras-default-rtdb.firebaseio.com/",
    'storageBucket': "cadastroesdras.appspot.com",
    'messagingSenderId': "447236985164",
    'appId': "1:447236985164:web:2ef253837b22ee6253ffe9",
    'measurementId': "G-3XS7QY17WB"
}





firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()



Window.size = (350, 600)



screen_helper = '''

ScreenManager:

    LoginScreen:

    CadastroScreen:   



<LoginScreen>:

    name: "login"

    id: login

    MDFloatLayout:

        MDLabel:

            id: login_message

            text: "Entrar"

            pos_hint: {"center_x": .5, "center_y": .75}

            halign: "center"

            font_name: "Arial"

            font_size: "40sp"

            theme_text_color: "Custom"

            text_color: 0/255, 0/255, 139/255, 1



        MDFloatLayout:

            size_hint: .75, .08

            pos_hint: {"center_x": .5, "center_y": .65}

            canvas:

            TextInput:

                id: email_login

                hint_text: "Email"

                size_hint: 1, None

                pos_hint: {"center_x": .5, "center_y": .5}

                height: self.minimum_height

                multiline: False

                cursor_color: 0/255, 0/255, 0/255, 1

                cursor_width: "2sp"

                foreground_color: 0/255, 0/255, 0/255, 1

                background_color: 255/255, 250/255, 250/255, 1

                padding: 15

                font_name: "Arial"

                font_size: "18sp"



        MDFloatLayout:

            size_hint: .75, .08

            pos_hint: {"center_x": .5, "center_y": .55}

            TextInput:

                id: senha_login

                hint_text: "Senha"

                password: True

                size_hint: 1, None

                pos_hint: {"center_x": .5, "center_y": .5}

                height: self.minimum_height

                multiline: False

                cursor_color: 0/255, 0/255, 0/255, 1

                cursor_width: "2sp"

                foreground_color: 0/255, 0/255, 0/255, 1

                background_color: 255/255, 250/255, 250/255, 1

                padding: 15

                font_name: "Arial"

                font_size: "18sp"



        Button:

            text: "Fazer cadastro"

            font_name: "Arial"

            theme_text_color: "Custom"

            font_size: "15sp"

            size_hint: .5, .08

            pos_hint: {"center_x": .5, "center_y": .35}

            background_color: 0, 0, 0, 0

            canvas.before:

                Color:

                    rgb: (0/255, 0/255, 139/255, 1)

                RoundedRectangle:

                    size: self.size

                    pos: self.pos

            on_release:

                root.manager.current = "cadastro"



        Button:
            text: "ENTRAR"
            font_name: "Arial"
            font_size: "20sp"
            size_hint: .5, .08
            pos_hint: {"center_x": .5, "center_y": .45}
            background_color: 0, 0, 0, 0
            canvas.before:
                Color:
                    rgb: (0/255, 0/255, 139/255, 1)

                RoundedRectangle:
                    size: self.size
                    pos: self.pos

            on_release:
                print("Login realizado", email_login.text, senha_login.text)
                app.my_firebaselogin.Login(email_login.text, senha_login.text, login_message)
                root.manager.transition.direction = "right"





<CadastroScreen>:

    name: "cadastro"

    id: cadastro

    MDFloatLayout:

        MDLabel:

            id: signup_message

            text: "Criar uma nova conta"

            pos_hint: {"center_x": .5, "center_y": .75}

            halign: "center"

            font_name: "Arial"

            font_size: "20sp"

            theme_text_color: "Custom"

            text_color: 0/255, 0/255, 139/255, 1



        MDFloatLayout:

            size_hint: .75, .08

            pos_hint: {"center_x": .5, "center_y": .65}

            canvas:

            TextInput:

                id: email_signup

                hint_text: "Email"

                size_hint: 1, None

                pos_hint: {"center_x": .5, "center_y": .5}

                height: self.minimum_height

                multiline: False

                cursor_color: 0/255, 0/255, 0/255, 1

                cursor_width: "2sp"

                foreground_color: 0/255, 0/255, 0/255, 1

                background_color: 255/255, 250/255, 250/255, 1

                padding: 15

                font_name: "Arial"

                font_size: "18sp"



        MDFloatLayout:

            size_hint: .75, .08

            pos_hint: {"center_x": .5, "center_y": .55}

            canvas:

            TextInput:

                id: username_signup

                hint_text: "Nome de usuário"

                size_hint: 1, None

                pos_hint: {"center_x": .5, "center_y": .5}

                height: self.minimum_height

                multiline: False

                cursor_color: 0/255, 0/255, 0/255, 1

                cursor_width: "2sp"

                foreground_color: 0/255, 0/255, 0/255, 1

                background_color: 255/255, 250/255, 250/255, 1

                padding: 15

                font_name: "Arial"

                font_size: "18sp"



        MDFloatLayout:

            size_hint: .75, .08

            pos_hint: {"center_x": .5, "center_y": .45}

            canvas:

                Color:

                    rgb: (238/255, 238/255, 238/255, 1)

                RoundedRectangle:

                    size: self.size

                    pos: self.pos

                    radius: [25]

            TextInput:

                id: password_signup

                hint_text: "Senha(mín. 6 caracterés)"

                password: True

                size_hint: 1, None

                pos_hint: {"center_x": .5, "center_y": .5}

                height: self.minimum_height

                multiline: False

                cursor_color: 0/255, 0/255, 0/255, 1

                cursor_width: "2sp"

                foreground_color: 0/255, 0/255, 0/255, 1

                background_color: 255/255, 250/255, 250/255, 1

                padding: 15

                font_name: "Arial"

                font_size: "18sp"



        MDTextButton:

            text: "Já tem conta? Faça login!"

            font_name: "Arial"

            theme_text_color: "Custom"

            font_size: "15sp"

            text_color: 0/255, 0/255, 139/255, 1

            pos_hint: {"center_x": .5, "center_y": .38}

            on_release:

                root.manager.transition.direction = "right"

                root.manager.current = "login"



        Button:

            text: "CADASTRAR"

            font_name: "Arial"

            font_size: "20sp"

            size_hint: .5, .08

            pos_hint: {"center_x": .5, "center_y": .30}

            background_color: 0, 0, 0, 0

            canvas.before:

                Color:

                    rgb: (0/255, 0/255, 139/255, 1)

                RoundedRectangle:

                    size: self.size

                    pos: self.pos

            on_release:

                print("Cadastro realizado", email_signup.text, password_signup.text)

                app.my_firebaselogin.sign_up(email_signup.text, username_signup.text, password_signup.text, signup_message)

                root.manager.transition.direction = "right"

                root.manager.current = "login"



<Card@MDCard+FakeRectangularElevationBehavior>:

    size_hint: None, None

    size: "280dp", "180dp"

    pos_hint: {"center_x": .5, "center_y": .5}

    elevation: 5

    orientation: "vertical"

 



'''



class LoginScreen(Screen):



    def limpar_campos_login(self):

        self.ids.email_login.text = ""

        self.ids.senha_login.text = ""

        self.ids.login_message.text = "Login"

        self.ids.login_message.font_size = "40sp"



class CadastroScreen(Screen):

    pass





sm = ScreenManager()

sm.add_widget(LoginScreen(name="login"))

sm.add_widget(CadastroScreen(name="cadastro"))





class TesteApp(MDApp):

    def build(self):

        self.my_firebaselogin = MyFirebaseLogin()

        return Builder.load_string(screen_helper)



    def on_start(self):

        self.title = "Login"

        self.root.current = "login"



class MyFirebaseLogin:

    def Login(self, email, password, login_message):

        try:

            auth.sign_in_with_email_and_password(email, password)

            print("Login bem-sucedido")

            login_message.text = "Login realizado"

            login_message.text_color = (0/255, 0/255, 139/255, 1)

            login_message.font_size = "30sp"

        except:

            print("Login falhou")

            login_message.text = "Dados inválidos"

            login_message.text_color = (1, 0, 0, 1)  # Vermelho

            login_message.font_size = "30sp"



    def sign_up(self, email, username, password, login_message):

        try:

            auth.create_user_with_email_and_password(email, password)

            print("Cadastro bem-sucedido")

            login_message.text = "Login"

            login_message.text_color = (162/255, 201/255, 86/255, 1)

            login_message.font_size = "40sp"



        except:

            print("Cadastro falhou")



if __name__ == '__main__':

    TesteApp().run()
