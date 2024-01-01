# Pętla while w Pythonie jest używana do wielokrotnego wykonywania bloku kodu, 
# dopóki pewien warunek jest spełniony. Warunek ten jest sprawdzany przed każdą 
# iteracją pętli, i jeśli jest on nadal spełniony, to pętla będzie kontynuowana. 
# Jednak gdy warunek przestaje być spełniony, pętla jest przerywana, i kontrola 
# przechodzi do kodu poza pętlą.

# Napisz program, który wydrukuje do konsoli 10 pierwszych liczb pierwszych rozdzielonych przecinkiem
number = 2
def checkNumner (number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

ten_number = []
while len(ten_number) < 10:
    if checkNumner(number):
        ten_number.append(number)
    number += 1

print(ten_number)