from tkinter import *
janela = Tk()
janela.title("Calculadora")
janela.geometry("299x200")
janela.configure(background="#dde")
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
def btresult():
    resp["text"]=x
def limpar():
    nmr1.delete(0,END)
    nmr2.delete(0,END)
    resp["text"]=""
txt1 = Label(janela,text="Digite um número")
txt1.grid(column=0,row=0)
nmr1=Entry(janela) #Cria uma janela interagível, like "input()"
nmr1.grid(column=0,row=1)
txt2 = Label(janela,text="Digite outro número")
txt2.grid(column=2,row=0,padx=0)
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
resp=Label(janela,text="",background='#fff')
resp.grid(column=1,row=3)
dele = Button(janela, text="Limpar",command=limpar)
dele.grid(column=1,row=4)
janela.mainloop()
