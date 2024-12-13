import customtkinter as ctk

def escola():
    uni1 = float(unidade1.get())
    uni2 = float(unidade2.get())
    uni3 = float(unidade3.get())
    calc = (uni1+uni2+uni3)/3
    if(calc>=5):
       mensagem = 'você foi aprovado'
       cor = 'green'
    else:
        mensagem = 'você foi para a recuperação'
        cor = 'red'
    resultado.configure(text=f'A sua média foi {calc:.2f} , \n {mensagem}',text_color=cor)

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('500x350')

janela.title('Sistema escolar')

ctk.CTkLabel(janela, text='Sistema escolar 2024', font=('verdana', 20, 'bold')).pack(pady=10)
unidade1 = ctk.CTkEntry(janela, width= 300, placeholder_text='Digite a nota da 1º unidade', height=30, corner_radius=10)
unidade1.pack(pady=10)
unidade2 = ctk.CTkEntry(janela, width= 300, height=30, placeholder_text='Digite a nota da 2º unidade', corner_radius=10)
unidade2.pack(pady=10)
unidade3 = ctk.CTkEntry(janela, width= 300, height=30, placeholder_text='Digite a nota da 3º unidade', corner_radius=10)
unidade3.pack(pady=10)
btn = ctk.CTkButton(janela, width=100, height=30, fg_color='green', text='Calcular', cursor = 'hand2', command=escola)
btn.pack(pady=10)
resultado = ctk.CTkLabel(janela, font=('verdana', 18, 'italic') , text='')
resultado.pack(pady=10)

janela.mainloop()
