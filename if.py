
number_to_guess = 2
user_input = int(input("Adivina el number_to_guess"))

if user_input == number_to_guess:
	print("You win!!")
else:
    print("Nope, te quedan 4 intentos")

user_input = int(input("Adivina el number_to_guess (te quedan 4 intentos): "))

if user_input == number_to_guess:
    print("You win!!")
else:
    print("Nope, te quedan 3 intentos")

user_input = int(input("Adivina el number_to_guess (te quedan 3 intentos): "))

if user_input == number_to_guess:
    print("You win")
else:
    print("Nope, te quedan 2 intentos")

user_input = int(input("Adivina el number_to_guess (te quedan 2 intentos): "))

if user_input == number_to_guess:
    print("You win")
else:
    print("Nope te queda 1 intento")

user_input = int(input("Adivina el number_to_guess (te quedan 1 intentos): "))

if user_input == number_to_guess:
    print("You win")
else:
    print("Nope you lose")


