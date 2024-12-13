import os
import customtkinter as ctk

def logoff():
    os.system('shutdown -l 0')
def des():
    os.system('shutdown -s -t 0')
def re():
    os.system('shutdown -r -t 0')


ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.geometry('300x300')
janela.title('Log-off')

ctk.CTkLabel(janela, text='Bomba Patch', font=('verdana', 20, 'bold')).pack(pady=10)
bt1 = ctk.CTkButton(janela, fg_color='red', text='Desligar',hover_color='darkred' , command=des,width=200, height=40, cursor='pirate', font=('verdana', 15, 'bold'), text_color='white', corner_radius=20)
bt1.pack(pady=20)
bt2 = ctk.CTkButton(janela, fg_color='orange', hover_color='darkorange',command=re ,text='Reiniciar', width=200, height=40, cursor='pirate', font=('verdana', 15, 'bold'), text_color='white', corner_radius=20)
bt2.pack(pady=10)
bt3 = ctk.CTkButton(janela, fg_color='green',hover_color='darkgreen', command=logoff , text='Bloquear', width=200, height=40, cursor='pirate', font=('verdana', 15, 'bold'), text_color='white', corner_radius=20)
bt3.pack(pady=10)

janela.mainloop()