from tkinter import *
import webbrowser

def space_pressed(event):
    event.widget.tk_focusNext().focus()
    return "break"

def on_enter(event):
    hacer_operacion()

ventana = Tk()
ventana.wm_attributes("-topmost", True)
ventana.title("CALCULADORA RETIROS")
ventana.configure(background="Skyblue4")

e_resultado = Entry(ventana, font=("Calibri 20"))
e_resultado.grid(row=0, column=1, columnspan=4, padx=5, pady=5)
e_resultado.bind("<Return>", on_enter)

e_deposito = Entry(ventana, font=("Calibri 20"))
e_deposito.grid(row=2, column=1, columnspan=4, padx=5, pady=5)
e_deposito.bind("<Return>", on_enter)

e_retiro = Entry(ventana, font=("Calibri 20"))
e_retiro.grid(row=3, column=1, columnspan=4, padx=5, pady=5)
e_retiro.bind("<Return>", on_enter)

e_bet = Entry(ventana, font=("Calibri 20"))
e_bet.grid(row=4, column=1, columnspan=4, padx=5, pady=5)
e_bet.bind("<Return>", on_enter)

e_win = Entry(ventana, font=("Calibri 20"))
e_win.grid(row=5, column=1, columnspan=4, padx=5, pady=5)
e_win.bind("<Return>", on_enter)

e_bono = Entry(ventana, font=("Calibri 20"))
e_bono.grid(row=6, column=1, columnspan=4, padx=5, pady=5)
e_bono.bind("<Return>", on_enter)

e_balance = Entry(ventana, font=("Calibri 20"))
e_balance.grid(row=7, column=1, columnspan=4, padx=5, pady=5)
e_balance.bind("<Return>", on_enter)

e_cb = Entry(ventana, font=("Calibri 20"))
e_cb.grid(row=8, column=1, columnspan=4, padx=5, pady=5)
e_cb.bind("<Return>", on_enter)

# Agregamos el evento para la tecla espacio
ventana.bind("<space>", space_pressed)

# Resto del código...

#aca agregamos la fuente y que son ventanas de entrada de texto

#funciones
def callback():
    webbrowser.open_new("https://datastudio.google.com/reporting/04d9329a-7612-43b6-b39a-e99f1c1f4c88/page/p_kxidinenxc")
def llamajira():
    webbrowser.open_new("https://stratechcorp.atlassian.net/jira/software/projects/RISK/boards/27")
def llama_jira_desarrollo():
    webbrowser.open_new("https://stratechcorp.atlassian.net/servicedesk/customer/portal/4/group/16/create/61")
def llama_bet():
    webbrowser.open_new("https://datastudio.google.com/reporting/d804b2c5-4058-4e4c-aac2-be3cd8112d8a/page/mtu5C")
def llama_seon():
    webbrowser.open_new("https://admin.seon.io/manual/")
def llama_truora():
    webbrowser.open_new("https://docs.accounts.truora.com/#tag--Hooks")
def llama_sofwiss():
    webbrowser.open_new("https://jira.softswiss.net/servicedesk/customer/portal/2/group/9")
#agregamos links en estas lineas
def clear():
    e_bono.delete(0,END)
    e_win.delete(0,END)
    e_bet.delete(0,END)
    e_balance.delete(0,END)
    e_cb.delete(0,END)
    e_deposito.delete(0,END)
    e_retiro.delete(0,END)
    e_resultado.delete(0,END)
#borramos lineas con esta funcion
def suma():
    cb=e_cb.get()
    re_cb=eval(cb)
    e_cb.delete(0,END)
    e_cb.insert(0,re_cb)
#resuelve el cb
def hacer_operacion():
    win=e_win.get()
    re_win=eval(win)
    bet=e_bet.get()
    re_bet=eval(bet)
    bono=e_bono.get()
    if len(bono) <= 1:
        re_bono=0
    else:
         re_bono=eval(bono)
    retiro=e_retiro.get()
    re_retiro=eval(retiro)
    deposito=e_deposito.get()
    re_deposito=eval(deposito)
    balance=e_balance.get()
    if len(balance) <= 1:
        re_balance=0
    else:
        re_balance=eval(balance)
    cb=e_cb.get()
    if len(cb) <= 1:
        re_cb=0
    else:
        re_cb=eval(cb)




#en estas lineas corregi el error de cubo en blanco en caso de no existir alguno de los parametros
    resultado=re_win-re_bet+re_bono-re_retiro+re_deposito+re_balance+re_cb
    e_resultado.delete(0,END)
    e_resultado.insert(0,resultado)
#en estas lineas agrege el algoritmo de suma resta

botonwin=Label(ventana, text="WIN",width=5,height=2 ,fg='green',activebackground='green',activeforeground='white')
botonbet=Label(ventana, text="BET",width=5,height=2,fg='red',activebackground='red',activeforeground='white')
#en estas lineas 61-62 le agregue color para diferenciar mas simple por que quiero y por que puedo
botonbono=Label(ventana, text="BONO",width=5,height=2)
botonretiro=Label(ventana, text="RETIRO",width=5,height=2)
botondeposito=Label(ventana, text="DEPOSITO",width=8,height=2)
botonresultado=Button(ventana, text="RESULTADO",width=9,height=2, command=lambda:hacer_operacion())
botonborrar=Button(ventana, text="BORRAR",width=9,height=2, command=clear)
botoncb=Button(ventana, text="CB",width=5,height=2,command=lambda:suma())
botonbalance=Label(ventana, text="BALANCEMANUAL",width=14,height=2)
your_variable_name = Button(text="DATASTUDIO", command=callback)
your_variable_name.grid(column=2, row=10)
jira = Button(text="JIRA_RIESGO", command=llamajira)
jira.grid(column=2, row=11)
jira_desa = Button(text="JIRA_DESARROLLO", command=llama_jira_desarrollo)
jira_desa.grid(column=2, row=12)
databet = Button(text="DATA_BY_BET", command=llama_bet)
databet.grid(column=2, row=13)
seon = Button(text="SEON", command=llama_seon)
seon.grid(column=2, row=14)
truora = Button(text="TRUORA", command=llama_truora)
truora.grid(column=2, row=15)
sofwiss = Button(text="SOFTSWISS", command=llama_sofwiss)
sofwiss.grid(column=2, row=16)
#agregar botones

botonwin.grid(row=5,column=0,padx=5,pady=5)
botonbet.grid(row=4,column=0,padx=5,pady=5)
botonbono.grid(row=6,column=0,padx=5,pady=5)
botonretiro.grid(row=3,column=0,padx=5,pady=5)
botondeposito.grid(row=2,column=0,padx=5,pady=5)
botonresultado.grid(row=0,column=0,padx=5,pady=5)
botoncb.grid(row=8,column=0,padx=5,pady=5)
botonbalance.grid(row=7,column=0,padx=5,pady=5)
botonborrar.grid(row=9,column=0,padx=5,pady=5)

ventana.mainloop()
#indicamos que no se cierre