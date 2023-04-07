from tkinter import *
import math
janela = Tk()
janela.title("Calculadora")
janela.geometry("420x300")
janela.resizable(False,False)
janela.configure(background="#00BFFF")
def btmais():
    global x
    x = int(nmr1.get())+int(nmr2.get())
def btsub():
    global x
    x = int(nmr1.get())-int(nmr2.get())
def btmulti():
    global x
    x = int(nmr1.get())*int(nmr2.get())
def btdivi():
    global x
    x = int(nmr1.get())/int(nmr2.get())
def btporc():
    global x
    x = (int(nmr1.get())*int(nmr2.get()))/100
def btraiz():
    global x
    x = math.sqrt(int(nmr1.get()))
def btresult():
    resp["text"]=x
def limpar():
    nmr1.delete(0,END)
    nmr2.delete(0,END)
    resp["text"]=""
txt1 = Label(janela,text="Primeiro número",bg="#00BFFF")
txt1.grid(column=0,row=0,pady=0)
nmr1=Entry(janela) #Cria uma janela interagível, like "input()"
nmr1.grid(column=0,row=1)
txt2 = Label(janela,text="Segundo número",bg="#00BFFF")
txt2.grid(column=2,row=0,padx=0,pady=0)
nmr2=Entry(janela) #Cria uma janela interagível, like "input()" ; o Text() é a mesma coisa do Entry() porém com mais linhas
nmr2.grid(column=2,row=1,pady= 10)
btt1 = Button(janela,text="=",command=btresult)
btt1.grid(column=1,row=2)
sinal=Button(janela,text="+", background="#dde",command=btmais)
sinal.grid(column=0,row=2)
sinal2=Button(janela,text="-", background="#dde",command=btsub)
sinal2.grid(column=2,row=2,padx=0)
sinal3=Button(janela,text="x", background="#dde",command=btmulti)
sinal3.grid(column=0,row=3)
sinal4=Button(janela,text="/", background="#dde",command=btdivi)
sinal4.grid(column=2,row=3,padx=0)
sinal5=Button(janela, text="%\n1º-Porcen.\n2º-Número",command=btporc,background="#dde")
sinal5.grid(column=2,row=4)
sinal6=Button(janela, text="√ \nSó 1 Nº",command=btraiz,background="#dde")
sinal6.grid(column=0,row=4)
resp=Label(janela,text="",background='#fff')
resp.grid(column=1,row=3)
dele = Button(janela, text="Limpar",command=limpar)
dele.grid(column=1,row=4)
atencao=Label(janela,text="1º - Digite os números\n2º - Selecione a operação\n3º - Clique para ver o resultado",bg="#00BFFF")
atencao.grid(column=1,row=5)
logo = PhotoImage(file="imagens/calcu.png")
logo = logo.subsample(7,7)
fot = Label(image=logo,bg="#00BFFF")
fot.grid(column=1,row=1,pady=0)
janela.mainloop()
