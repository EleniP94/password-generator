import random 

print("Welcome to your Password Generator :)")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789"

number = input(
    "Amount of passwords to generate: "
)

# convert to integer incase string throws us a type error 
number = int(number)

length = input("Input your password length: ")
length = int(length)

print("\nhere are your passwords: ")

for pwd in range(number): 
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars) 
    print(passwords)