import random

guessesTaken = 0

print("Olá")
print("Qual seu nome?")
yourName = input()
print("Prazer em conhecer "+yourName)

number = random.randint(1,20)
print("Bom, "+yourName+"Eu estou pensando em um número de 1 a 20.")

print("Tente adivinhar:")

while guessesTaken < 6:
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

        if guess < number:
            print("Seu palpite está muito baixo.")

        if guess > number:
            print("Seu palpite está muito alto.")

        if guess == number:
            break
 if guess == number:
        guessesTaken = str(guessesTaken)
        print("Muito bom, " +yourName+"! Você adivinhou em "+guessesTaken+ "palpites!")
if guess != number:
        number = str(number)
        print("Nãooo. O número que pensei foi "+number)