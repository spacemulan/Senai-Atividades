import customtkinter as ctk
import tkinter
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('dark')

#Lista de cores e fontes

co1= '#00FF7F'
cor2 = '#32CD32'
cor3 = '#DC143C'

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 14, 'bold')

#-----------------------

#funções;.

def adicionar_tarefa():
    tarefa = nova_tarefa.get()
    if tarefa: 
        lista_tarefas.insert(0, tarefa)
        nova_tarefa.delete(0, END)
        salvar_tarefas()
    else:
        messagebox.showerror('Erro', 'Digite uma tarefa')   
def remover_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()
    if tarefa_selecionada:
        lista_tarefas.delete(tarefa_selecionada)
        salvar_tarefas()
    else:
        messagebox.showerror('Erro', 'Clique numa tarefa para selecionar.')
def salvar_tarefas():
    with open('tarefas.txt', 'w') as t:
        tarefas = lista_tarefas.get(0,END)
        for x in tarefas:
            t.write(x + '\n')
def carrega_tarefas():
    try:
        with open('tarefas.txt', 'r') as R:
            tarefas = R.readlines()
            for x in tarefas:
                lista_tarefas.insert(0, x.strip())
    except:
        messagebox.showerror('Erro ', 'Não pode carregar tarefa')
#--------------------------


janela = ctk.CTk()
janela.geometry('300x490')
janela.title('App tarefas V1.0')
ctk.CTkLabel(janela, text='APP Tarefas', font=font1, text_color=co1).pack(pady=10)

add_tarefas = ctk.CTkButton(janela, text='Adicionar Tarefa', fg_color='blue', width=100, height=30, command=adicionar_tarefa)
add_tarefas.place(x=20, y=80)
remov_tarefa = ctk.CTkButton(janela, text='Remover Tarefas', fg_color=cor3, width=100, height= 30, command=remover_tarefa)
remov_tarefa.place(x=170, y=80)
nova_tarefa = ctk.CTkEntry(janela, width=250, height=30, placeholder_text='Digite uma nova tarefa')
nova_tarefa.pack(pady=100)
ctk.CTkLabel(janela, text='Tarefas pendentes', font=font2, text_color=cor2).place(x=65, y=210)
lista_tarefas= Listbox(janela, width=40, height=15)
lista_tarefas.place(x=30, y=240)

carrega_tarefas()
janela.mainloop()