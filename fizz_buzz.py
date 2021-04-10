
def fizz_buzz(number):
    i=1

    for i in range(1,number+1):

        if i%3 ==0 and i%5 ==0:
            print("FIZZBUZZ")
        elif i % 3==0:
            print("FIZZ")
        elif i %5 ==0:
            print("BUZZ")
        else:
            print(i)
number=int(input("enter the limit: "))
fizz_buzz(number)


