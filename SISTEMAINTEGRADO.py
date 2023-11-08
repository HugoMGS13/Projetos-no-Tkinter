import webbrowser
from tkinter import *

janela = Tk()
janela.title('SISTEMA INTEGRADO')
janela.geometry('600x400')
janela.resizable(False, False)

def OpenURL():
    webbrowser.open('https://www.bb.com.br/site/')

botão = Button(janela, text = 'BANCO', command=OpenURL )
botão.place(x=274,y=100)
but = Button(janela, text='SISTEMA')
but.place(x=270, y=150)
janela.mainloop()

'''
#Sistema do SESI
import re
import webbrowser
print('Bem vindo ao SINSESI')
regex = r'[1-5]{1}'
regex_senha = r'\w{8}'
try:
  vontade = input('Digite o número do Sistema que você quer entrar!\n1 - Sistema Bancário\n2 - Sistema Financeiro\n3 - Sistema de geração de boletos\n4 - Sistema de Patrimônio\n5 - Sistema de Almoxarifado\n')
  check = re.fullmatch(regex, vontade)
  if check:
    if vontade == '1':
      senha = input('Digite a senha do seu banco:\n')
      checksenha = re.fullmatch(regex_senha, senha)
      loop = 0
      while checksenha == None:
        print('Tente novamente')
        senha = input('Digite a senha do seu banco:\n')
        checksenha = re.fullmatch(regex_senha, senha)
      if checksenha != None:
        print('Bem vindo ao site.')
        webbrowser.open('https://www.bb.com.br/site/')
  else:
    print('ERRO')
except:
  print('ERRO exc')
'''
