def fizzbuzz(num : int):
    if (num % 3) == 0 and (num % 5) == 0:
        print(f"{num} FizzBuzz")
        return
    elif (num % 3) == 0:
        print(f"{num} Fizz")
    elif (num % 5) == 0:
        print(f"{num} Buzz")
    else:
        print(num)


for num in range(1,101):
    fizzbuzz(num)






