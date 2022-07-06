# Write your code below this line 👇
def prime_checker(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                print(f"{number} is not prime")
                break
        else:
            print(f"{number} is prime")
    else:
        print(f"{number} is not prime")
# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
