# ***** DAILY CHALLENGE #1 - Easy *****

# Create a program that will ask the users name, age, and Reddit username. have it tell them the information back,
# In the format:
#
# your name is (blank), you are (blank) years old, and your username is (blank)
#
# for extra credit, have the program log this information in a file to be accessed later.

# ---------------------------------------------------------------------------------------------------------------------


def information(n, a, user):
    result = "Your name is %s, you are %s years old, and your username is %s" % (n, a, user)
    my_file.write(str(result) + "\n")
    return result

my_file = open("Challenge_1_easy_save", "r+")
name = input("Name: ")
age = input("Age: ")
username = input("Username: ")

output = information(name, age, username)
my_file.close()
print(output)
