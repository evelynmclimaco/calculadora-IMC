from tkinter import *
from tkinter import ttk

co0 = '#ffffff'  # branco / white
co1 = '#000000'  # preto / black
co2 = '#e2725b'  # terracota / terracotta
co3 = '#e2725c'  # terracota escuro

janela = Tk()
janela.title('')
janela.geometry('400x290')
janela.configure(bg=co0)


# --------------- dividindo A JANELA em duas partes ------------------

frame_cima = Frame(janela, width=400, height=60, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=400, height=260, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


# ---------------- configurando frame cima ----------------------------

app_nome = Label(frame_cima, text='Calculadora IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 20 bold'), bg=co0, fg=co2)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 '), bg=co3, fg=co1)
app_linha.place(x=0, y=35)


# ----------------- função calcular ----------------

def calcular():

    # altura = float(input('Digite sua altura em cm: '))
    altura = float(e_altura.get())

    # peso = float(input('Digite seu peso em kg: '))
    peso = float(e_peso.get())

    # imc = peso / (altura/100)**2
    imc = peso / altura ** 2

    # print(imc)

    if imc < 18.5:
        # print(
        # f'seu IMC é de {imc}, tá muito maga mulé!, é classificado como magreza')
        l_resultado_texto['text'] = 'Classificado como: Abaixo do peso!'

    elif imc >= 18.5 and imc < 24.9:
        # print(f'seu IMC é de {imc}, tá gostosaaa!, é classificado como normal')
        l_resultado_texto['text'] = 'Classificado como: Peso normal!'

    elif imc >= 25 and imc < 29.9:
        # print(
        # f'seu IMC é de {imc}, vamos começar a fechar a boca, é classificado como Obesidade I!')
        l_resultado_texto['text'] = 'Classificado como: Sobrepeso!'

    elif imc >= 30 and imc < 39.9:
        # print(
        # f'seu IMC é de {imc}, procure uma academia e feche a boca logo!!! é classificado como Obesidade II!')
        l_resultado_texto['text'] = 'Classificado como: Obesidade!'

    elif imc > 40.0:
        # print(
        # f'seu IMC é de {imc}, pode parar de comer que o negocio da feio pra o teu lado. Obesidade grave III')
        l_resultado_texto['text'] = 'Classificado como: Obesidade Mórbida!'

    # print(float(imc))
    l_resultado['text'] = "{:.{}f}".format(imc, 2)


# --------------- configurando frame baixo ----------------------------

l_altura = Label(frame_baixo, text=' Digite sua altura em cm', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 12'), bg=co0, fg=co1)
l_altura.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=6, relief='solid', font=('Ivy 12'), justify='center')
e_altura.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


l_peso = Label(frame_baixo, text='Digite seu peso em kg', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 12'), bg=co0, fg=co1)
l_peso.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=6, relief='solid', font=('Ivy 12'), justify='center')
e_peso.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado = Label(frame_baixo, text='_', width=5, height=1, padx=5, pady=12, relief='flat', anchor='center', font=('Ivy 26 bold'), bg=co3, fg=co0)
l_resultado.place(x=265, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=0, height=0, padx=0, pady=22, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co3)
l_resultado_texto.place(x=93, y=90)


# b_calcular = Button(frame_baixo, command='calcular', text='Calcular:', width=47, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co3, fg=co0)
b_calcular = Button(frame_baixo, command=calcular, text='Calcular:', width=47, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co3, fg=co0)

b_calcular.grid(row=4, column=0, sticky=NSEW, pady=80, padx=5, columnspan=20)


janela.mainloop()