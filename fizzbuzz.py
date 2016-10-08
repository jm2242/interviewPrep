__author__ = 'jonathanmares'


def fizzbuzz(n):

    for x in range (1,n+1):
        if x%5==0 and x%3==0:
            print("FizzBuzz")
        elif x%5==0:
            print("buzz")
        elif x%3==0:
            print("fizz")
        else:
            print(x)

fizzbuzz(15)