# PASSWORD GENERATOR PROGRAM
import random

try:
    numbers = "1234567890"
    capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowletters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%&*_+/?\|=<>"
    
    all_char = numbers + capletters + lowletters + symbols
    length = int(input("ENTER THE NUMBER OF CHARACTERS FOR YOUR PASSWORD: "))

    passward = ''.join(random.sample(all_char, length))
    print("GENERATED PASSWORD: ", passward)
except ValueError:
    print("invalid input")

 