
while True:
    #Getting the input from the user
    first_word = input("Enter the first word: ")
    if first_word == "done" or first_word == "":
        break
    
    second_word = input("Enter the second word: ")
    if second_word == "done" or second_word == "":
        break

    if first_word < second_word:

        print(first_word, "comes first")
    else:
        print(second_word, "comes first")