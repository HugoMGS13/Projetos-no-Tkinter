from tkinter import *
from tkinter import ttk
import random
janela = Tk()
janela.title("Adivinhe as cores")
janela.geometry("400x400")
janela.resizable(False,False)
#Listas de cores
listapalavras = ["VERMELHO","AZUL","AMARELO","VERDE","ROXO","PRETO"]
listadecores = ["#FF0000","#00BFFF",'#FFFF00',"#008000","#A020F0","#000000"]
#Função comum dos botões
#if
def if1():
    txtveri['text']="ACERTOU"
    valor_atual = result['value']
    if valor_atual < 100:
        novo_valor = valor_atual + 21
        result['value']=novo_valor
    elif valor_atual >= 100:
        txtveri['text']="VOCÊ GANHOU"
    f02()
#else
def else1():
    txtveri['text']="ERROUU"
    result['value']=0
    f02()
#Função do botão de início
def f02():
    bt1.destroy()
    cor = random.choice(listadecores)
    palavra = random.choice(listapalavras)
    txtjogo['text']=palavra
    txtjogo['foreground']=cor
def f03():
    txtveri['text']=""
    result['value']=0
    cor = random.choice(listadecores)
    palavra = random.choice(listapalavras)
    txtjogo['text']=palavra
    txtjogo['foreground']=cor
#Função dos botões das cores
def f1():
    if bt01['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
def f2():
    if bt02['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
def f3():
    if bt03['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
def f4():
    if bt04['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
def f5():
    if bt05['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
def f6():
    if bt06['background'] == txtjogo['foreground']:
        if1()
    else:
        else1()
#Texto de ajuda
txtajuda = Label(janela,text="Adivinhe a cor das palavras e tente não se confundir!",font=("Arial",10))
txtajuda.place(x=45,y=10)
txtveri = Label(janela,text="",font=("Arial",30))
txtveri.place(x=70,y=300)
#Botão de começar
bt1 = Button(janela,text="Começar",command=f02)
bt1.place(x=160,y=40)
btrei = Button(janela,text="Reiniciar",command=f03)
btrei.place(x=162,y=60)
#Botões de escolha
bt01 = Button(janela,background="#FF0000",height=2,width=4,command=f1)
bt01.place(x=130,y=200)
bt02 = Button(janela,background="#00BFFF",height=2,width=4,command=f2)
bt02.place(x=180,y=200)
bt03 = Button(janela,background='#FFFF00',height=2,width=4,command=f3)
bt03.place(x=230,y=200)
bt04 = Button(janela,background="#008000",height=2,width=4,command=f4)
bt04.place(x=130,y=260)
bt05 = Button(janela,background="#A020F0",height=2,width=4,command=f5)
bt05.place(x=180,y=260)
bt06 = Button(janela,background='#000000',height=2,width=4,command=f6)
bt06.place(x=230,y=260)
#Textos
txtjogo = Label(janela,text="",font=('impact',50))
txtjogo.place(x=85,y=87)
#Progress Bar
result = ttk.Progressbar(janela,max=100)
result.place(x=150,y=360)

janela.mainloop()