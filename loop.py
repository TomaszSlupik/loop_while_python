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

print('---')


# Napisz program, który przy użyciu pętli while oblicza silnię z danej liczby całkowitej

def countStrong (num):
    yourNum = []
    number = 0
    while number < num:
        number += 1
        yourNum.append(number)

    multipliedNumbers = 1 
    
    for finalStrong in yourNum:
        multipliedNumbers  *= finalStrong
    print (f"The factorial is: {multipliedNumbers}")

countStrong(5)

print('---')

# Napisz program który wyświetla kolejne elementy ciągu Fibonacciego aż do momentu przekroczenia zadanej wartości np.100
yourLimit = 100

def fibonacci(limit):
    fibonacciList = [0, 1]
    while True:
        nextFibonacci = fibonacciList[-1] + fibonacciList[-2]
        if nextFibonacci >= limit:
            break
        fibonacciList.append(nextFibonacci)
    
    for num in fibonacciList:
        print(num)

fibonacci(yourLimit)


