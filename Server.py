import socket
import threading
import time
import pickle

IP = "192.168.0.7"
PORT = 7654

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))

lo = threading.Lock()
scores = []

def ReceveurClient(conn, lo):
    while True:
        try:
            global scores
            best_score_client = conn.recv(1024)
            best_score_client = pickle.loads(best_score_client)
            with open('scoreboard.txt', 'w+') as fichier:
                print(len(scores))
                new_best_score = []

                with lo:
                    for index,score_client in enumerate(best_score_client):
                        if score_client > scores[index]:
                                new_best_score.append(str(score_client) + '\n')
                        else:
                            new_best_score.append(str(scores[index]) + '\n')

                    fichier.writelines(new_best_score)




        except BrokenPipeError:
            pass

        except ConnectionResetError:
            pass

def EnvoyeurClient(conn):
        try:
            global scores
            packet_type = conn.recv(1024)
            packet_type = packet_type.decode("UTF8")

            if packet_type == "SpaceGame":
                receveur_client_thread = threading.Thread(target=ReceveurClient, args=(connexion,lo))
                receveur_client_thread.start()
                while True:
                    score_client = pickle.dumps(scores)
                    conn.send(score_client)
                    time.sleep(0.1)


            else:
                pass

            time.sleep(1)


        except BrokenPipeError:
            pass

        except ConnectionResetError:
            pass


def update_bestscore(lo):

    #Garde en mémoire le meilleur score

    while True:
        with open('scoreboard.txt', 'r+') as fichier: #Ouverture du fichier Scoreboard et lecture de celui-ci

            with lo:

                global scores
                meilleurs_scores = fichier.readlines()
                for index,score in enumerate(meilleurs_scores):
                    meilleurs_scores[index] = int(score)

                scores.clear()

                for score in meilleurs_scores:
                    scores.append(score)


update_score_thread = threading.Thread(target=update_bestscore, args=(lo,))
update_score_thread.start()

print("Demarrage du serveur !")

while True:

    server.listen()
    connexion , addresse = server.accept()
    print("Nouvelle connexion de {} sur le port {}".format(addresse[0], addresse[1]))
    envoyeur_client_thread = threading.Thread(target=EnvoyeurClient, args=(connexion,))
    envoyeur_client_thread.start()