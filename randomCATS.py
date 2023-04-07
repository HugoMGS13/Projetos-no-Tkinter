from tkinter import *
import random
janela = Tk()
janela.title("Random cats")
janela.geometry("210x270")
janela.resizable(False,False)
janela.configure(background="#00BFFF")
def f1():
    lista=[gato,spider,gatin,gato2]
    x = random.choice(lista)
    if x == spider:
        lose["text"]="Você perdeu (Não achou o gatinho)"
        fot["image"]=x
    else:
        fot["image"]=x
        lose["text"]="Gatinhooooooo"
def f2():
    fot["image"]=""
    lose["text"]=""
but = Button(janela,text="Busque um gatinho",command=f1)
but.grid(column=0,row=0)
gato = PhotoImage(file="imagens/gatinhow.png")
gato = gato.subsample(8,8)
spider = PhotoImage(file="imagens/spider.png")
spider = spider.subsample(3,3)
gatin = PhotoImage(file="imagens/gigi.png")
gatin = gatin.subsample(2,2)
gato2 = PhotoImage(file="imagens/gato2.png")
gato2 = gato2.subsample(2,2)
fot = Label(janela, image="",bg="#00BFFF")
fot.grid(column=0,row=4)
lose = Label(janela, text="", bg ="#00BFFF")
lose.grid(column=0,row=5)
reini = Button(janela, text="Reiniciar",command=f2)
reini.grid(column=0,row=6)
janela.mainloop()
