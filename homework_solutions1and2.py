'''
Take 5 values from the user and write a program that prints the values you get on the screen.
Print the type of values you received in this program on the screen.
When using print functions, do not forget to use f-string and format usage in your program.
'''

value_array = []
for i in range(0,5):
    came_value = int(input("Enter a number : "))
    value_array.append(came_value)
    
print(f"Array : {value_array} ")

for i in value_array:
    print(f"Array_value = {i} type is {type(i)}")


"""
User Identification Program
The user will be defined. Get the data of this user by input method. Obtain information from user
as follow:
-First Name
-Last Name
-Age
-Date of birth (just year)

Pass the user's information to the list and displays the screen using the for loop. Print all user
information on the screen.

If he is under 18, print "You can't go out because it's too dangerous." on the screen.

If he is over 18, print "You can go out to the street." on the screen.
"""

user_information = []
question_strings = ["First_Name : ","Last_Name : ","Age : ","Date of birth : "]

for i in range(0,len(question_strings)):
    info = input(question_strings[i])
    user_information.append(info)
print(user_information)

if int(user_information[2]) < 18:
    print(f"You are {user_information[2]} years old. You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")
