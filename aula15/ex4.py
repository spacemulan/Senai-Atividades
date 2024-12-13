import customtkinter as ctk

janela = ctk.CTk()
def subtracao():
    n1 = int(num1.get())
    n2 = int(num2.get())
    subs = n1-n2
    resultado.configure(text=f'O resultado é {subs}')
def adicao():
    n1 = int(num1.get())
    n2 = int(num2.get())
    ad = n1+n2
    resultado.configure(text=f'O resultado é {ad}')
def multiplicacao():
    n1 = int(num1.get())
    n2 = int(num2.get())
    mt = n1*n2
    resultado.configure(text=f'O resultado é {mt}')
def divisao():
    n1 = int(num1.get())
    n2 = int(num2.get())
    dv = n1/n2
    resultado.configure(text=f'O resultado é {dv:.2f}')

ctk.set_appearance_mode('dark')
janela.geometry('500x500')

num1= ctk.CTkEntry(janela, width=300, height=40,placeholder_text='Digite um numero')
num1.pack(pady=30)
num2= ctk.CTkEntry(janela, width=300, height=40,placeholder_text='Digite outro numero')
num2.pack(pady=10)

sub = ctk.CTkButton(janela, cursor='hand2', width=130, height=40, text='Subtração', fg_color='red', hover_color='darkred', font=('verdana', 15, 'bold'), command=subtracao)
sub.pack(pady=10)
add = ctk.CTkButton(janela, cursor='hand2', width=130, height=40, text='Adição', fg_color='green', hover_color='darkgreen', font=('verdana', 15, 'bold'), command=adicao)
add.pack(pady=10)
div = ctk.CTkButton(janela, cursor='hand2', width=130, height=40, text='Divisão', fg_color='blue', hover_color='darkblue', font=('verdana', 15, 'bold'), command=divisao)
div.pack(pady=10)
multi = ctk.CTkButton(janela, cursor='hand2', width=130, height=40, text='Multiplicação', fg_color='orange', hover_color='darkorange', font=('verdana', 15, 'bold'), command=multiplicacao)
multi.pack(pady=10)
resultado = ctk.CTkLabel(janela, font=('verdana', 15, 'bold'), text_color='white', text='')
resultado.pack(pady=10)
janela.mainloop()