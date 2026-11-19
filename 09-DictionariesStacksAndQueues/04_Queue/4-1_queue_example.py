###
# A simple example of creating and using a queue
#
# Kolejka (queue) działa jak kolejka w sklepie: kto pierwszy przyszedł, ten pierwszy wychodzi (FIFO).
# queue.Queue(): put() dodaje na koniec kolejki, get() zabiera z początku.
import queue                               # dołączamy moduł queue

q = queue.Queue()                          # tworzymy pustą kolejkę

q.put('Anna')                              # Anna staje w kolejce pierwsza
q.put('Tomasz')                            # Tomasz staje za nią
q.put('Kasia')                             # Kasia staje na końcu

print('People in the queue:', q.qsize())   # qsize() podaje liczbę elementów w kolejce (3)
while not q.empty():                       # powtarzamy, dopóki kolejka nie jest pusta
    print('Served:', q.get())              # get() zabiera osobę z początku: Anna, potem Tomasz, potem Kasia
