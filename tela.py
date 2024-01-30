from tkinter import *
from PIL import ImageTk, Image

janela = Tk()
janela.title("SevenFit")
janela.geometry("800x600")


imagem = Image.open("C:/Users/duosg/Downloads/3dccf36fc2395f71d4543ccd176d11c8.jpg")


imagem_fundo = ImageTk.PhotoImage(imagem)

label_fundo = Label(janela, image=imagem_fundo)

label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

janela_orientacao = Label(janela, text="Bem vindo a SevenFit!")
janela_orientacao.grid(column=0, row=0, padx=300, pady=50)

botao = Button(janela, text="Entrar", background="green", height="2", width="10", font="verdana")
botao.grid(column=0, row=1)



janela.mainloop()


