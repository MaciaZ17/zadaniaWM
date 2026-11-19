###
# Stack operations: puts numbers on the stack, sums the last two
# and then the remaining elements
#
# Stos (stack) działa jak stos talerzy: ostatni położony jest pierwszym zdjętym (LIFO).
# queue.LifoQueue() to gotowy stos: put() kładzie na wierzch, get() zdejmuje z wierzchu,
# empty() sprawdza, czy stos jest pusty.
import queue                                            # dołączamy moduł queue, w którym jest gotowy stos

stack = queue.LifoQueue()                               # tworzymy pusty stos

stack.put(2)                                            # kładziemy 2 na stos
stack.put(3)                                            # kładziemy 3
stack.put(7)                                            # kładziemy 7
stack.put(4)                                            # kładziemy 4
stack.put(1)                                            # kładziemy 1
stack.put(9)                                            # kładziemy 9
stack.put(8)                                            # kładziemy 8 (jest teraz na samej górze)

first = stack.get()                                     # zdejmujemy element z góry: 8
second = stack.get()                                    # zdejmujemy następny: 9
print('Sum of the last two numbers:', first + second)   # wypisujemy 8 + 9 = 17

total = 0                                               # suma pozostałych elementów, na początku 0
while not stack.empty():                                # powtarzamy, dopóki stos nie jest pusty
    total = total + stack.get()                         # zdejmujemy element z góry i dodajemy do sumy
print('Sum of the remaining elements:', total)          # 1 + 4 + 7 + 3 + 2 = 17
