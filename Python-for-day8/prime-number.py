def prime_checker(number):
    prime = True
    for divided_num in range(2,number):
        if number % divided_num == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
n = int(input("Please enter a number: \n")) 
prime_checker(number=n)
