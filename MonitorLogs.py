import random
import datetime

def menu():
    nomeArquivo = "log.txt"
    while True:
        print("Monitor LogPy")
        print("1 - Gerar Logs")
        print("2 - Analisar Logs")
        print("3 - Gerar e Analisar Logs")
        print("4 - Sair")
        
        opcao = input("Escolha uma opcao: ")
        if opcao == "1":
            try:
                quantidade = int(input("Quantidade de logs a serem gerados: "))
                gerarArquivo(quantidade, nomeArquivo)
            except:
                print("Quantidade inválida")
                
        elif opcao == "2":
            analisarLog(nomeArquivo)
        elif opcao == "3":
            try:
                quantidade = int(input("Quantidade de logs a serem gerados: "))
                gerarArquivo(quantidade, nomeArquivo)
                analisarLog(nomeArquivo)
            except:
                print("Quantidade inválida")
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida")
            
def gerarArquivo(quantidade, nomeArquivo):
    with open(nomeArquivo, "w", encoding="utf-8") as file:
        for i in range(quantidade):
            file.write(montarLog(i) + "\n")
        print("Logs gerados")
        
def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIP(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f"[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 512mb - HTTP/1.1 - {agente} - /home"

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22, 8, 0)
    data = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + data).strftime("%d/%m/%Y %H:%M:%S")

def gerarIP(i):
    r = random.randint(1, 6)
    
    if i >= 20 and i <= 30:
        return "200.0.111.345"
    
    if r == 1:
        return "192.168.5.6"
    elif r == 2:
        return "192.168.2.61"
    elif r == 3:
        return "192.168.2.4"
    elif r == 4:
        return "192.168.4.7"
    elif r == 5:
        return "192.168.0.15"
    else:
        return "192.168.101.5"
    
def analisarLog(nomeArquivo):
    pass

menu()