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
