import time
import threading
def escalonamento_round_robin(key, burst):
    print ('ROUND ROBIN\n  Processo '+ key + ' com burst time de ' + str(burst) + ' esta execultando o algoritmo Round Robin com quatum de 5\n')
    time.sleep(5)
    tempo_restante = burst - 5
    if(tempo_restante > 0):
        escalonamento_fifo(key, tempo_restante)
    else:
        tempo_restante = 0
        print('\t***PROCESSOS FINALIZADOS COM ROUND ROBIN***\n\t\tProcesso '+ key + ' com burst time de ' + str(burst) + ' foi finalizado com o algoritmo ROUND-ROBIN \n'),


def escalonamento_fifo(key, tempo_restante):
    time.sleep(tempo_restante)
    print('FIFO\n  Processo ' + key + ' será finalizado com o algoritmo FIFO pois não conseguiu finalizar com RR seu burst time é maior que a fatia de tempo que lhe foi reservada tempo restante é de :'
          + str(tempo_restante) + '\n\t***PROCESSOS FINALIZADOS COM FIFO***\nProcesso ' + key + ' restando ' + str(tempo_restante) + ' foi finalizado por meio do escalonamento FIFO\n')

lista =	{"P1": 40.0,"P2": 30.0,"P3": 3.0,"P4": 5.0,"P5": 1.0}

for key, burst in lista.items():
    thread = threading.Thread(target=escalonamento_round_robin, args=(key,burst)).start()