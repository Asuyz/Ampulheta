import time
import tkinter as tk

def abrir_janela_sair():
   janela = tk.Tk()
   janela.title("Fim Da Tarefa...")
   janela.geometry("300x150")
   

   label = tk.Label(janela, text=""" Finalizando...  """, font=("Arial", 14))
   label.pack(pady=30)

   botao = tk.Button(janela, text="OK", command=janela.destroy)
   botao.pack()

   janela.mainloop()

def abrir_janela_tempo(): 

   janela = tk.Tk()
   janela.title("Contagem finalizada...")
   janela.geometry("300x150")

   label = tk.Label(janela, text=""" O tempo acabou ⏳ ...  """, font=("Arial", 14))
   label.pack(pady=30)

   botao = tk.Button(janela, text="OK", command=janela.destroy)
   botao.pack()

   janela.mainloop()



while True:
    try:
        print('Seja bem-vindo(a) a sua ampulheta. | 1- Continuar | 2- Sair')
        escolha = int(input())
        

        if escolha  == 1:
            print("""
            +====+   
            |(::)|
            | )( |
            |(..)|
            +====+
            """)


            

            print("""Obrigado por ter continuado, para começarmos digite o tempo desejado em minutos | 
            Exemplo: 120 minutos (2 Horas)""")

            tempo = int(input())
            

            i = 0
            while i < tempo:   
                i += 1
                time.sleep(60)  
                print(f"{i} minuto(s) já se passaram.")

            print("⏳ O tempo acabou!")
            abrir_janela_tempo()
            break



        elif escolha == 2:
            print("Saindo da ampulheta...")
            break

        else:
            raise ValueError("Escolha incorreta. Escolha novamente.")

    except ValueError as e:
        print(e)

abrir_janela_sair()