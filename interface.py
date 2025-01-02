import tkinter as tk
from defs import *
window = tk.Tk()
window.title("Banco IFPE")
window.geometry('1080x720')



label_menu = tk.Label(window, text='''
                         Menu:
                      1. Cadastro
                      2. Login
                      3. Saque
                      4. Status da Conta
                      5. Ajuda
                      6. Sair
                      ''',
                     font=("Arial", 12))
label_menu.pack(pady=8)

label_texto_introdutorio = tk.Label(window, text='Digite a opção: ', font=('Arial', 11))
label_texto_introdutorio.pack(pady=10)

entrad = tk.Entry(window, font=('Arial', 14), width=5)
entrad.pack(pady=10)



window.mainloop()