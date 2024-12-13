import customtkinter as ctk


ctk.set_appearance_mode('white')

janela = ctk.CTk('#c7a6ec')
janela.geometry('500x300')
janela.title('Sistema de acesso')
janela.iconbitmap('padlock.ico')

ctk.CTkLabel(janela, text='Sistema de acesso', font=('arial', 30,'bold'), text_color='white').pack(pady=50)
login = ctk.CTkEntry(janela, text_color='black', placeholder_text='Digite seu usuário', font=('arial', 15, 'italic'), width=300)
login.pack()
senha = ctk.CTkEntry(janela, text_color='black', placeholder_text='Digite sua senha',show='•', font=('arial', 15, 'italic'), width=300)
senha.pack(pady=10)
botao = ctk.CTkButton(janela, text='Enviar', cursor='hand2', fg_color='purple', text_color='white', width=150, height=30, font=('arial', 15, 'bold'))
botao.pack(pady=10)
janela.mainloop()