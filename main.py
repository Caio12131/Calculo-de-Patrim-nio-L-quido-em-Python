import tkinter
from tkinter import*
from tkinter import ttk, Tk, messagebox

from PIL import Image, ImageTk

cor0 = "#2e2d2b" # preto
cor1 = "#feffff" # branco
cor2 = "#4fa882" # verde
cor3 = "#38576b" # valor
cor4 = "#403d3d" # letra
cor5 = "#e06636" # profit
cor6 = "#038cfc" # azul
cor7 = "#3fbfb9" # verde
cor8 = "#263238" # + verde
cor9 = "#e9edf5" # + verde
cor10 = "#6e8faf" # 
cor11 = "#f2f4f2" # 

janela = Tk()
janela.title("")
janela.geometry('380x550')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")


# Frames
frameCima = Frame(janela, width=380, height=50, bg= cor1)
frameCima.grid(row=0, column=0, columnspan=2)

frameResultado = Frame(janela, width=380, height=50, bg= cor3)
frameResultado.grid(row=1, column=0, pady=10)

frameBaixo = Frame(janela, width=380, height=450, bg= cor1)
frameBaixo.grid(row=2, column=0, pady=10)


# Dividindo Frame Baixo

frameAtivos = Frame(frameBaixo, width=180, height=370, bg=cor9)
frameAtivos.grid(row=0, column=0, padx= 5)

framePassivo = Frame(frameBaixo, width=180, height=370, bg=cor9)
framePassivo.grid(row=0, column=1)    


app_image = Image.open('icon.jpg')
app_image = app_image.resize((42,42))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(frameCima, image=app_image, width=900, compound=LEFT, padx=5, anchor=NW, bg=cor1, fg=cor4)
app_logo.place(x=5, y=0)

app = Label(frameCima, text="Calculadora de Patrimônio Líquido", width=900, compound=LEFT, padx=5, pady=8, anchor=NW, font=("ivy, 12"), bg=cor1, fg=cor4)
app.place(x=50, y=5)

app_linha = Label(frameCima, width=380, anchor=NW, font=("Verdana 1"), bg=cor3, fg=cor1)
app_linha.place(x=0, y=47)



def patrimonio_liquido():
    try:

        ativo1 = float(valor_casa.get())
        ativo2 = float(valor_imoveis.get())
        ativo3 = float(valor_investimentos.get())
        ativo4 = float(valor_veiculos.get())
        ativo5 = float(valor_outros.get())


        passivo1 = float(valor_hipoteca.get())
        passivo2 = float(valor_emprestimo_carro.get())
        passivo3 = float(valor_emprestimo_estudantil.get())
        passivo4 = float(valor_outras.get())

        if ativo1 == "" or ativo2 == "" or ativo3 == "" or ativo4 == "" or ativo5 == "" or passivo1 == '' or passivo2 == "" or passivo3 == "" or passivo4 == "":
       
            return
        else:
            total_ativos = float(ativo1) + float(ativo2) + float(ativo3) + float(ativo4) + float(ativo5) 

            total_passivos = float(passivo1) + float(passivo2) + float(passivo3)  + float(passivo4) 

            patrimonio_liquido = total_ativos - total_passivos
            l_resultado['text'] = 'R${:,.2f}'.format(patrimonio_liquido)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos em todos os campos.")

### Entrada de Ativos

l_nome = Label(frameAtivos, text="Insira Ativos", padx= 10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=cor2, fg=cor1)
l_nome.place(x=0, y=0)

#Valores

l_nome = Label(frameAtivos, text="Valor Casa", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=40)
valor_casa = Entry(frameAtivos, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_casa.place(x=10, y=65)

#Imoveis
l_nome = Label(frameAtivos, text="Imoveis", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=105)
valor_imoveis = Entry(frameAtivos, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_imoveis.place(x=10, y=125)

#Veiculos
l_nome = Label(frameAtivos, text="Veiculos", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=165)
valor_veiculos = Entry(frameAtivos, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_veiculos.place(x=10, y=185)

#Investimentos
l_nome = Label(frameAtivos, text="Investimentos", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=225)
valor_investimentos = Entry(frameAtivos, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_investimentos.place(x=10, y=245)

#Outros Ativos
l_nome = Label(frameAtivos, text="Outros Ativos", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=285)
valor_outros = Entry(frameAtivos, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_outros.place(x=10, y=305)


### Entrando Passivos 

l_nome = Label(framePassivo, text="Insira Passivos", padx= 10, width=35, height=1, anchor=NW, font=('Verdana 11'), bg=cor5, fg=cor1)
l_nome.place(x=0, y=0)

#Hipoteca

l_nome = Label(framePassivo, text="Hipoteca", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=40)
valor_hipoteca = Entry(framePassivo, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_hipoteca.place(x=10, y=65)

#Emprestimo de Carro
l_nome = Label(framePassivo, text="Empréstimo de carro", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=105)
valor_emprestimo_carro = Entry(framePassivo, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_emprestimo_carro.place(x=10, y=125)

#Emprestimo Estudantil
l_nome = Label(framePassivo, text="Emprestimo Estudantil", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=165)
valor_emprestimo_estudantil = Entry(framePassivo, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_emprestimo_estudantil.place(x=10, y=185)

#Outras Dívidas
l_nome = Label(framePassivo, text="Outras Dívidas", anchor=E, font=('Verdana 9'), bg=cor9, fg=cor0)
l_nome.place(x=10, y=225)
valor_outras = Entry(framePassivo, width=10, font=("Ivy 12"), justify="center", relief='solid')
valor_outras.place(x=10, y=245)

### Resultado

l_resultado = Label(frameResultado, text="R${:,.2f}".format(00), padx=10, width=15, anchor=NE, font=('Verdana 25 bold'), bg=cor3, fg=cor1)
l_resultado.place(x=0, y=7)  

botao_calcular = Button(framePassivo,command=patrimonio_liquido, text="Calcular".upper(), padx=8, width=20, height=2, anchor=CENTER, font=('Ivy 9 bold'), bg=cor1, fg=cor0)
botao_calcular.place(x=10, y=310)  


janela.mainloop()
