# print your name 

print("Hello, my name is neha!!")

# ask name and print

name = input("What is your name: ")

print("Nice to meet you,", name)

# sum of two numbers

a = 10
b = 30

sum = a + b

print("This sum is:", sum)

#simple calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("addition: " , a + b)
print("substraction: " , a + b)
print("multiplication: " , a + b)
print("division: " , a + b)

#sandwich make

bread = input("choose your bread (white/brown)")
filling = input("Choose your filling (chese / jam / potato / banana)")

print("Here you silly sandwich: ")
print("[" + bread + "bread" + filling + "rainbow silly sandwich" + "]")
print("🧽🌦🌈🌂🔥⛄❄⚡⛱☔🌠🌙🌑🌊🍕🍔🍟🌭🥐🧀🍒🍉🌵🍭🍇🥝🍽🎨🧵💎")


# rock paper sissors game

import random

choices = ["rock" , "paper" , "scissors"]
computer = random.choice(choices)
player = input("choose rock , paper , scissor")

if player == computer:
    print("😑😋😎😁 It's a tie")

elif (player == "rock" and computer == "scissors"):
    (player == "paper" and computer == "rock") 
    (player == "scissors" and computer == "paper")
    print("😎😎You Win")

else:
    print("🤪😱 computer wins")