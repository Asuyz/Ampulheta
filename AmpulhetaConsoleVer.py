import time
import os
import tkinter as tk

# Janelas
def abrir_janela_sair():
   janela = tk.Tk()
   janela.title("Fim Da Tarefa...")
   janela.geometry("300x150")
   

   label = tk.Label(janela, text=""" Finalizando...  """, font=("Arial", 14))
   label.pack(pady=30)


def abrir_janela_tempo(): 

   janela = tk.Tk()
   janela.title("Contagem finalizada...")
   janela.geometry("300x150")

   label = tk.Label(janela, text=""" O tempo acabou ⏳ ...  """, font=("Arial", 14))
   label.pack(pady=30)

   botao = tk.Button(janela, text="OK", command=janela.destroy)
   botao.pack()

   janela.mainloop()

# Cores ANSI para o terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


#Limpeza de Tela
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def alerta_final():
    for _ in range(3):
        print(f"{YELLOW}⏰ O tempo acabou!{RESET}")
        
        
        if os.name == 'posix':  # Linux ou macOS
            print("\a", end="", flush=True)
        else:  # Windows
            os.system('echo \a')
        
        time.sleep(1)
        limpar_tela()
        time.sleep(0.5)
    print(f"{GREEN}✅ Tempo finalizado!{RESET}\n")


def ampulheta():
    ampulheta_ativa = True

    while ampulheta_ativa:
        limpar_tela()
        print(f"{CYAN}=== MENU PRINCIPAL ==={RESET}")
        print("Deseja rodar a ampulheta?")
        print(f"{YELLOW}1 - Sim{RESET}")
        print(f"{YELLOW}2 - Não{RESET}\n")

        try:
            escolha_menu = int(input("Escolha: "))

            if escolha_menu == 1:
                print(f"\n{GREEN}Entrando na ampulheta...{RESET}")
                time.sleep(1)

                def ampulheta_controle():
                    nonlocal ampulheta_ativa
                    ampulheta_controle_ativa = True

                    while ampulheta_controle_ativa:
                        limpar_tela()
                        print(f"{CYAN}=== MENU DA AMPULHETA ==={RESET}")
                        print(f"{YELLOW}1 - Vamos contar{RESET}")
                        print(f"{YELLOW}2 - Encerrar{RESET}\n")

                        try:
                            escolha_ampulheta = int(input("Escolha: "))

                            if escolha_ampulheta == 1:
                                limpar_tela()
                                print(f"{CYAN}=== DEFINIR TEMPO ==={RESET}")

                                print("Digite seu tempo em minutos.")
                                print(f"{YELLOW}Exemplos:{RESET}")

                                print(" - 1 hora = 60 minutos")
                                print(" - 2 horas = 120 minutos\n")

                                try:
                                    tempo = int(input("Tempo em minutos: "))
                                    limpar_tela()
                                    print(f"{GREEN}⏳ Cronômetro iniciado por {tempo} minuto(s)!{RESET}\n")

                                    for i in range(1, tempo + 1):
                                        time.sleep(60) 
                                        print(f"{i} minuto(s) já se passaram...")

                                    print(f"\n{YELLOW}⏰ O tempo acabou!{RESET}\n")
                                    abrir_janela_tempo()
                                    alerta_final()
                                    print("Deseja correr um novo tempo?")
                                    print(f"{YELLOW}1 - Sim{RESET}")
                                    print(f"{YELLOW}2 - Sair{RESET}\n")

                                    try:
                                        escolha_nova = int(input("Escolha: "))
                                        if escolha_nova == 1:
                                            continue
                                        elif escolha_nova == 2:
                                            print(f"{YELLOW}Saindo... até logo! 👋{RESET}")
                                            ampulheta_ativa = False
                                            ampulheta_controle_ativa = False
                                            time.sleep(1)

                                        else:
                                            print(f"{RED}Valor inválido, digite novamente.{RESET}")
                                            time.sleep(1)
                                    except ValueError:
                                        print(f"{RED}Entrada inválida! Digite apenas números.{RESET}")
                                        time.sleep(1)

                                except ValueError:
                                    print(f"{RED}Entrada inválida! Digite apenas números.{RESET}")
                                    time.sleep(1)

                            elif escolha_ampulheta == 2:
                                print(f"{YELLOW}Encerrando ampulheta...{RESET}")
                                ampulheta_ativa = False
                                ampulheta_controle_ativa = False
                                time.sleep(1)

                            else:
                                print(f"{RED}Valor inválido! Escolha 1 ou 2.{RESET}")
                                time.sleep(1)

                        except ValueError:
                            print(f"{RED}Entrada inválida! Digite apenas números.{RESET}")
                            time.sleep(1)

                ampulheta_controle()

            elif escolha_menu == 2:
                print(f"{YELLOW}Saindo... até logo! 👋{RESET}")
                ampulheta_ativa = False
                time.sleep(1)

            else:
                print(f"{RED}Valor inválido! Escolha 1 ou 2.{RESET}")
                time.sleep(1)

        except ValueError:
            print(f"{RED}Entrada inválida! Digite apenas números.{RESET}")
            time.sleep(1)


ampulheta()