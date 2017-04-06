#SIMULEAC Ioana-Veronica

# -*- coding: cp1252 -*-
import socket, sys
HOST = socket.gethostname()
PORT = 6666
counter =0
"""
compteur de connexions actives
1) creation du socket :
"""
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""2) liaison du socket a une adresse precise :"""

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket a l'adresse choisie a echoue.")
    sys.exit

while 1:
    """3) Attente de la requete de connexion d'un client :"""
    
    print("Serveur pret, en attente de requetes ...")
    mySocket.listen(5)
    
    """4) Etablissement de la connexion :"""
    connexion, adresse = mySocket.accept()
    counter +=1
    print("Client connecte, adresse IP %s, port %s" % (adresse[0], adresse[1]))

    """5) Dialogue avec le client :"""
    msgServeur ="Vous etes connecte au serveur Ioana. Envoyez vos messages."
    connexion.send(msgServeur)
    msgClient = connexion.recv(1024)
    
    while 1:
        print("C>", msgClient)
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)
        
    """6) Fermeture de la connexion :"""
    
    connexion.send("fin")
    print("Connexion interrompue.")
    connexion.close()
    ch = input("<R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
        break
