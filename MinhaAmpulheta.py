import tkinter as tk
import time























# Backup da Lógica

#while True:
#    try:
#        print('Seja bem-vindo(a) a sua ampulheta. | 1- Continuar | 2- Sair')
#        escolha= int(input())
#        
#        if escolha == 1:
#            print("""
#            +====+   
#            |(::)|
#            | )( |
#            |(..)|
#            +====+
#            """)
#            print("""Obrigado por ter continuado, para comerçarmos digite o tempo desejado em minutos | 
#            Exemplo: 120 minutos ( 2Horas )""")
#            tempo=int(input())

#            segundos = tempo * 60
#            i = 0
#            while i < tempo:
#                i = i + 1
#                time.sleep(60)
#                print(i)
#                print ('Deseja continuar? | 1 - Sim | 2 - Não')
#                continuar = int(input())
#                try:
#                    if continuar == 1:
#                        True
#                    else:
#                         False
#                except:
#                    ValueError('Escolha incorreta. Escolha novamente.')
#    except:
#        escolha == 2
#        False
#    finally:
#        ValueError('Escolha incorreta. Escolha novamente.')
#        True
    

  
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