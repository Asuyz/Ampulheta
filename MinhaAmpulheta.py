import tkinter as tk
import time


print("""


+====+    
|(::)|
| )( |
|(..)|
+====+
""")
time.sleep(1)
print("""


+====+    
|(::)|
| )( |
|(..)|
+====+
""")
time.sleep(1)
print("""


+====+    
|(::)|
| )( |
|(..)|
+====+
""")
time.sleep(1)

print("SEJA BEM VINDO A SUA AMPULHETA EM PYTHON!!!| Digite o tempo que gostaria em minutos: | (Exemplo: 120 minutos)")

tempo=int(input())

segundos = tempo *60

i = 0

while i < tempo:
    i = i+1
    time.sleep(60)
    print (i)
  
def abrir_janela():
    janela = tk.Tk()
    janela.title("Tempo Esgotado")
    janela.geometry("300x150")

    label = tk.Label(janela, text="""⏳ O tempo acabou!  """, font=("Arial", 14))
    label.pack(pady=30)

    botao = tk.Button(janela, text="OK", command=janela.destroy)
    botao.pack()

    janela.mainloop()

abrir_janela()