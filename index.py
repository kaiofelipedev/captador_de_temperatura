from tkinter import *
from tkinter import ttk
import automacao as auto

janela = Tk()
janela.title("Clima São Paulo")
janela.geometry("480x500+400+100")
janela.configure(background="#736F36", highlightthickness=10,
                  highlightcolor="#592202")

# Título

lb_titulo = Label(janela, text="Clima São Paulo",bg="#736F36", fg="#F2EAE4",
                  font=("verdana", 14, "bold"))
lb_titulo.place(relx=.3, relwidth=.4, relheight=.1)

# Treeview

tabela = ttk.Treeview(janela, columns=("Umidade do ar", "Data", "Hora"))
tabela.column("#0", anchor=CENTER, width=15)
tabela.heading("#0", text="Temperatura")
tabela.column("Umidade do ar", anchor=CENTER, width=5)
tabela.heading("Umidade do ar", text="Umidade")
tabela.column("Data", anchor=CENTER, width=10)
tabela.heading("Data", text="Data")
tabela.column("Hora", anchor=CENTER, width=10)
tabela.heading("Hora", text="Hora")
tabela.place(relx=.25, rely=.1, relwidth=.74, relheight=.85)

# Botão

bt_pesquisa = Button(janela, text="Pesquisar", font=("verdana", 12, "bold"), fg="#F2EAE4",
                     bg="#734E38", border=6, relief="groove", command=auto.Navegador)
bt_pesquisa.place(rely=.3, relwidth=.25, relheight=.1)

janela.mainloop()