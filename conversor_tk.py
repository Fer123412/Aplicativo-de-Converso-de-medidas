import tkinter as tk
from tkinter import ttk
#Tela Lei de ohm
def tela_nova():
    lei = tk.Toplevel()
    lei.title('Lei de Ohm')
    lei.geometry('400x350+100+100')
    lei.resizable(False,False)

    #Função para calculo das grandezas
    def mudar(event=None):
        op = opcao.get()
        if op == '':
            resultado_ohm.config(text='Escolha uma Opção!',fg='Red')
            return
        if op == 'Tensão':
            tip_gz.config(text='Resistência')
            tip_gz2.config(text='Corrente')
        elif op == 'Resistência':
            tip_gz.config(text='Tensão')
            tip_gz2.config(text='Corrente')
        elif op == 'Corrente':
            tip_gz.config(text='Tensão')
            tip_gz2.config(text='Resistência')
    #Função dos calculos
    def calculo():
        try:
            v1 = float(Entrada.get())
            v2 = float(Entrada2.get())
        except ValueError:
            resultado_ohm.config(text='ERRO!',padx=10,pady=10,fg='red')
            return
        
        op = opcao.get()

        if op == 'Tensão':
            r = v1 * v2
            resultado_ohm.config(text=f'{r:.2f}V')
        elif op == 'Resistência':
            r = v1 / v2
            resultado_ohm.config(text=f'{r:.2f}Ohm ')
        elif op == 'Corrente':
            r = v1 / v2
            resultado_ohm.config(text=f'{r:.2f}A')

    Quadro_ohm = tk.Frame(
        lei,
        width=400,
        height=500,
        bg='silver',
        bd=3,
        relief='raised'
        )
    Quadro_ohm.pack(fill='both',expand=True)
    Quadro_ohm.pack_propagate(False)

    tk.Label(Quadro_ohm,text='Lei de Ohm',bg='silver',font=('Times New Roman',20,'bold underline italic')).pack(padx=20,pady=20)

    tk.Label(Quadro_ohm,text='Selecione o que deseja:',bg='silver',font=('Calibri',12,'bold')).pack()
    opcao = ttk.Combobox(
        Quadro_ohm,
        values=['Tensão','Resistência','Corrente'],
        state='readonly'
    )
    opcao.pack(pady=5)
    opcao.bind('<<ComboboxSelected>>',mudar)

    tip_gz = tk.Label(Quadro_ohm,text='Valor 1:',font=('Calibri',12),bg='silver')
    tip_gz.pack(anchor='w',padx=90)
    Entrada = tk.Entry(Quadro_ohm)
    Entrada.pack(fill='x',padx=90)

    tip_gz2 = tk.Label(Quadro_ohm,text=f'Valor 2:',font=('Calibri',12),bg='silver')
    tip_gz2.pack(anchor='w',padx=90)
    Entrada2 = tk.Entry(Quadro_ohm)
    Entrada2.pack(fill='x',padx=90)

    resultado_ohm = tk.Label(Quadro_ohm,text='',font=('Calibri',12,'bold'),bg='silver')
    resultado_ohm.pack()

    botao_result = tk.Button(Quadro_ohm,text='Converter',command=calculo)
    botao_result.pack(padx=30,pady=30)


#configuração
pag = tk.Tk()
pag.title('Conversor Tec')
pag.geometry('400x350+100+100')
pag.config(bg='gray')
pag.resizable(False,False)
 

#Barra de menu
menu = tk.Menu(pag)
pag.config(menu=menu)

menu.add_cascade(label='Exit',command=pag.quit)

ohm =  tk.Menu(menu,tearoff=0)
menu.add_cascade(label='Lei de Ohm',command=tela_nova)



#Quadro
quadro = tk.Frame(pag,width=400,height=500,bg='silver',bd=3,relief='raised')
quadro.pack(fill='both',expand=True)
quadro.pack_propagate(False)

#converter as medidas
def converter():
    t = str(input_tip.get())
    d = str(input_td.get())
    try:
        m = float(med.get())
    except ValueError:
        resul.config(text='Digitação invalida!!',fg='Red')
        return
    #multiplicação
    if t == 'km' and d == 'm':
        metros = m * 1000
    elif t == 'cm' and d == 'm':
        metros = m * 0.01
    elif t == 'm' and d == 'mm':
        metros = m * 1000
        
    #divisão
    elif t == 'mm' and d == 'cm':
        metros = m / 10
    elif t == 'cm' and d == 'm':
        metros = m / 0.01
    else:
        resul.config(text='Conversão invalida',fg='Red')
        return
    resul.config(text=f'{metros:.0f}{d}',font=('Calibri',16,'bold'),padx=10,pady=10)


#conteúdo
texto = tk.Label(quadro,text='Convert',font=('Times New Roman',25,'bold italic underline'),bg='silver')
texto.pack(ipady=10,fill='x')

#Entrada do  tipo medida
tk.Label(quadro,text='Tipo de Medida:',font=('Calibri',12),bg='silver').pack(anchor='w', padx=30)
input_tip = tk.Entry(quadro)
input_tip.pack(fill='x',padx=30)

#Entrada da medida que deseja
tk.Label(quadro,text='Tipo de medida deseja:',font=('Calibri',12),bg='silver').pack(anchor='w',padx=30)
input_td = tk.Entry(quadro)
input_td.pack(fill='x',padx=30)

#Entrada da medida
tk.Label(quadro,text='Medida:',font=('Calibri',12),bg='silver').pack(anchor='w',padx=30)
med = tk.Entry(quadro)
med.pack(fill='x',padx=30)

resul = tk.Label(quadro, text='',bg='silver')
resul.pack()

botao = tk.Button(
    quadro,
    text='Converter',
    width=30,
    font=('Segoe UI',10),
    command=converter
    )
botao.pack(padx=20,pady=20)

pag.mainloop()