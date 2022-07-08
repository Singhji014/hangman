import random
import word_list
import art

print(art.logo)
# word_list = ["aardvark", "baboon", "camel"]
game_word = random.choice(word_list.word_list)


live = 6

display = []
for _ in range(len(game_word)):
    display += "_"

print(display)
end_of_game = False
while not end_of_game:
    guess = input("Enter a letter you thing is part of the word: ").lower()
    # print(guess)
    #To loop through the game word to check if the letter is part of the Word or not

    if guess in display:
        print(f"You have already Guessed {guess}")

    for position in range(len(game_word)):
        if guess == game_word[position]:
            display[position] = guess
    # To keep track of chnaces the player use
    if guess not in game_word:
        live -= 1
        print(art.stages[live]) 
        if live < 0:
            end_of_game = True
            print(f"Sorry you lost. {game_word} is the answer")   

    print(display)
    if "_" not in display:
        end_of_game = True
        print("Congratulations You won")
            




