def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number// 2
            print( 'number ' +str(number) +' is even')
        else:
            number = number*3 + 1
            print('number ' +str(number) +' is odd')

collatz(9)
