# James Bond – Functions

'''
    James Bond is a classic movie character that fights bad guys and introduces himself in an iconic way: “Bond, James Bond.”

    Write a greetings() function that takes in two parameters:

    first_name
    last_name
    Print out the phrase with the last name, followed by a comma, and then the full name.

    Next, call the function using your own name, like:

    greetings('Richard', 'Hendricks')

    The output should look like:

    Hendricks, Richard Hendricks

    Note: This function doesn't have a return statement.
'''

def greetings():
    first_name = 'Bella'
    last_name = 'the Brit'

    print(last_name + ', ' + first_name)

greetings()