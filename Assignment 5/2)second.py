#First, I will get input from the user
input_string = input("Please enter a string: ")

# This function initializes an index to the last character of the string
index = len(input_string) - 1

# I used a while loop to print characters in reverse order
while index >= 0:

    print(input_string[index])


    index -= 1