import customtkinter as ctk
from tkinter import messagebox
#funções---------
def calcular():
    c = int(consumo.get())
    d = int(dis.get())
    p = float(preco.get())
    calc = (d/c)*p

    # resultado.configure(text=f'O valor da sua viagem é R${calc:.2f}')
    messagebox.showinfo('Valor Final', f'O valor da viagem é R${calc:.2f}')
#----------------

janela = ctk.CTk()
ctk.set_appearance_mode('dark')
janela.geometry('500x360')
janela.resizable(width=False,height=False)
janela.title('viagem')

ctk.CTkLabel(janela, text='Sistema de viagem 1.0', font=('verdana', 30, 'bold'), text_color='yellow').pack(pady=10)
dis=ctk.CTkEntry(janela, placeholder_text='Digite a distância', width=400, height=40)
dis.pack(pady=10)
consumo=ctk.CTkEntry(janela, placeholder_text='Digite o consumo', width=400, height=40)
consumo.pack(pady=10)
preco=ctk.CTkEntry(janela, placeholder_text='Digite o preço', width=400, height=40)
preco.pack(pady=10)
btn = ctk.CTkButton(janela, text='Calcular', font=('verdana', 15, 'bold'), text_color='white', fg_color='red', width=50, height=30, cursor='hand2', command=calcular, hover_color='darkred', corner_radius=10)
btn.pack(pady=10)
resultado = ctk.CTkLabel(janela, text='', font=('verdana', 20, 'bold'), text_color='yellow')
resultado.pack(pady=10)



janela.mainloop()
