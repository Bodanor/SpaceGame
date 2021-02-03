import socket
import time
import pickle

import Source.Variable

IP = "192.168.0.7"
PORT = 7654

connecte = False
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def SendScore(score, difficulte):

    if connecte:
        nouveau_score = []
        if difficulte == 0:
            nouveau_score = Source.Variable.MEILLEURS_SCORE
            nouveau_score[0] = score
        elif difficulte == 1:
            nouveau_score = Source.Variable.MEILLEURS_SCORE

            nouveau_score[1] = score

        elif difficulte == 2:
            nouveau_score = Source.Variable.MEILLEURS_SCORE

            nouveau_score[2] = score

        score = pickle.dumps(nouveau_score)
        server.send(score)


def GetScore():
    while True:
        try:
            global server
            global connecte
            if not connecte:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect((IP, PORT))
                connecte = True
                server.send(bytes("SpaceGame", "UTF8"))
                if connecte:

                    while True:
                        meilleurs_scores = server.recv(1024)
                        meilleurs_scores = pickle.loads(meilleurs_scores)
                        Source.Variable.MEILLEURS_SCORE = meilleurs_scores

                        time.sleep(0.1)



            else:
                connecte = True
                time.sleep(0.1)


        except Exception as e:
            connecte = False
            time.sleep(0.1)




