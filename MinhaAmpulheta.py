import tkinter as tk
import time





















# Backup da Lógica

#import time

# while True:
#     try:
#         print('Seja bem-vindo(a) a sua ampulheta. | 1- Continuar | 2- Sair')
#         escolha = int(input())

#         if escolha  == 1:
#             print("""
#             +====+   
#             |(::)|
#             | )( |
#             |(..)|
#             +====+
#             """)

#             print("""Obrigado por ter continuado, para começarmos digite o tempo desejado em minutos | 
#             Exemplo: 120 minutos (2 Horas)""")

#             tempo = int(input())
#             segundos = tempo * 60  

#             i = 0
#             while i < tempo:   # em minutos
#                 i += 1
#                 time.sleep(60)  # pausa de 1 minuto
#                 print(f"{i} minuto(s) já se passaram.")

#             print("⏳ O tempo acabou!")

#         elif escolha == 2:
#             print("Saindo da ampulheta...")
#             break

#         else:
#             raise ValueError("Escolha incorreta. Escolha novamente.")

#     except ValueError as e:
#         print(e)

  
#def abrir_janela():
   # janela = tk.Tk()
   # janela.title("Tempo Esgotado")
   # janela.geometry("300x150")

   # label = tk.Label(janela, text="""⏳ O tempo acabou!  """, font=("Arial", 14))
   # label.pack(pady=30)

   # botao = tk.Button(janela, text="OK", command=janela.destroy)
   # botao.pack()

   # janela.mainloop()

# abrir_janela()