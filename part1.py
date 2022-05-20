'''
______
PART 1
______
The code below prompts the user to enter two numbers, and then prints out the smaller of the numbers entered. Modify so that it prompts the user to enter THREE numbers, and then prints the smallest of the three numbers entered in a sentence.

(Hint: You'll need to be careful for the cases when the user enters the same number twice or all three times.)

An example of what should appear on the console when the code is run:

Enter a number: 11
Enter another number: 2
Enter another number: 5

The smallest number is 2
'''

number = int(input("Enter a number: "))

number1 = int(input("Enter another number: "))

number2 = int(input("Enter another number: "))

smallest = number

if number < number2 and number < number1:
  smallest = number
elif number1 < number and number1 < number2:
  smallest = number1
elif number2 < number and number2 < number1:
  smallest = number2
elif number == number2 and number < number1:
  smallest = number = number2
  print("The first and last numbers are equal")
elif number1 == number2 and number1 < number:
  smallest = number1 = number2
  print("The second and last numbers are equal")
elif number == number1 and number < number2:
  smallest = number = number
  print("The first and second numbers are equal")
print("The smallest number is ", smallest)
if number == number2 == number1:
  print("All 3 numbers are equal")