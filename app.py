import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode('dark')

# Iniciando a janela

janela = ctk.CTk() 

janela.geometry('600x450')
janela.title('Doceria da JuJu')
janela.resizable(False,False)

#---------------------------------------------
# Imagem
cookie = Image.open('cookie.png')
ctk_imagem = ctk.CTkImage(dark_image=cookie,size=(100,100))
#---------------------------------------------

# Elementos de texto 

titulo = ctk.CTkLabel(
    janela,text='Sistema de login',
    image=ctk_imagem,compound='top',
    font=('Cascadia Code',25,'bold')
)

subtitulo = ctk.CTkLabel(
    janela,text=('Bem-vindo(a)'),
    font=('Cascadia Code',20,'bold'),
    text_color="#A85633"
)

titulo.pack(pady=20)
subtitulo.pack(pady=10)
#---------------------------------------------

login = ctk.CTkEntry(
    janela,placeholder_text='Seu usuário',
    width=250,height=20,border_color="#5F3B2B",
    font=('Cascadia Code',18,'bold')
)

senha = ctk.CTkEntry(
    janela,placeholder_text='Sua senha',show='*',
    width=250,height=20,border_color="#5F3B2B",
    font=('Cascadia Code',18,'bold')
)

login.pack(pady=20)
senha.pack(pady=10)
#---------------------------------------------
# Botão
cake = Image.open('cake.png')
cake_image = ctk.CTkImage(
    dark_image=cake,light_image=cake,size=(30,30)
)

acesso = ctk.CTkButton(
    janela,text='',
    corner_radius=15,border_width=2,
    cursor='hand2',image=cake_image,
    fg_color="#A45C3D",hover_color="#694333"
)
acesso.pack(pady=30)

janela.mainloop()