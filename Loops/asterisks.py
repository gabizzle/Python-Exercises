# Asterisks - Loops

'''
    Create a program that uses a for loop and range() function to display the following pattern in the terminal using a bunch of asterisks *:

    *
    * *
    * * *
    * * * *
    * * * * *
    # ... and so on

    It should look like this but with 25 rows total.
'''


for i in range(25):
    print('* ' * i)