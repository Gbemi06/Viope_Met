Guess_word = "Giraffe"
your_guess = ""
Guess_count = 0

while your_guess != Guess_word:
    your_guess = input("Enter word: ")
    Guess_count += 1

print("you win")
print(Guess_count)
