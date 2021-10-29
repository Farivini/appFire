import base64
from config import firebaseConfig,auth,fire
import streamlit as st
from controle import *
from usr import *



def stream ():
        st.title("Verificação E-mail - Firebase")
        menu = ["Criar usuario","Login"]
        slc = st.sidebar.selectbox("Menu", menu)

        if slc == "Criar usuario":
                name = st.sidebar.text_input("Digite seu nome")
                usr = st.sidebar.text_input("Digite seu E-mail")
                passw = st.sidebar.text_input("Digite sua senha",type='password')
                if st.sidebar.button("Criar"):
                        try:
                                # Criamos usuario
                                sts = auth.create_user_with_email_and_password(usr, passw)
                                st.title("Verifique caixa do seu e-mail ,e confirme seu e-mail")
                                st.image("verienviado.png", width=None)
                                auth.send_email_verification(sts['idToken'])
                        except:
                                st.write('Verifique e-mail cadastrado e tente novamente, possivel e-mail ja foi cadastrado')
                                st.image("jaexiste.png",width=None)
        if slc == "Login":
                #st.subheader("Login")
                user = st.sidebar.text_input("Digite seu E-mail")
                pwd = st.sidebar.text_input("Digite sua senha",type='password')

                if st.sidebar.button("Login"):
                        try:
                                veri = auth.sign_in_with_email_and_password(user, pwd)
                                info = veri["idToken"]
                                usuInfo = auth.get_account_info(info)
                                # Verificando se está validado
                                usuarios = usuInfo["users"]
                                email_verif = usuarios[0]['emailVerified']  # Tem que retornar TRUE
                                if email_verif:
                                        st.write('E-mail já autenticado no Banco de dados, Login feito com sucesso')
                                        # Registrando acesso em um arquivo txt chamando a função control
                                        control(user)
                                        st.image('verificado.png',width=None)
                                        adm = admin(user)
                                        if adm is True:
                                                st.download_button(label='Controle de acesso',data=controle)
                                if not email_verif:
                                        st.write('E-mail não verificado, por favor olhe sua caixa de e-mail')
                                        st.image('negado.png', width=None)
                        except:
                                st.write('E-mail não cadastrado , favor cadastrar .')
                                st.image('cadastre.png',width=None)


if __name__ == '__main__':
    stream()