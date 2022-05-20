'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below

number = int(input("Enter a number: "))
number1 = int(input("Enter another number: "))

if number < 0 and number1 > 0 or number1 < 0 and number > 0:
  print("opposite")
elif number > 0 and number1 > 0:
  print("positive")
elif number < 0 and number1 < 0:
  print("negative")
elif number == 0 or number1 == 0:
  print("zero")