# Beginner Python Homework: Introduction to Basics
def print_hello_world():
    """Task 1: Print 'Hello, World!' to the console."""
    print("Hello World")

def create_and_print_variables():
    """Task 2: Create two variables, `greeting` with any text and `number` with any number, then print both."""
    greeting = "Hello, Python"
    number = 10
    print(greeting, number)

def sum_two_numbers():
    """Task 3: Create two variables with numbers and print their sum."""
    number1 = 5
    number2 = 10
    print(number1 + number2)

def greet_user():
    """Task 4: Use the input() function to ask the user for their name and greet them."""
    string = input("What's your name ?\n")
    print("Nice to meet you,", string,"!")

def create_list():
    """Task 5: Create a list named `fruits` with any three fruits and print the list."""
    fruits = ["Banana", "Orange", "Apple"]
    print(fruits)

def add_fruit_to_list(fruits):
    """Task 6: Add another fruit to the `fruits` list and print the updated list."""
    fruits = ["Banana", "Orange", "Apple"]
    fruits.append("Grape")
    print(fruits)


def print_fruits(fruits):
    """Task 7: Print each fruit in the `fruits` list using a loop."""
    fruits = ["Banana", "Orange", "Apple", "Grape"]
    for i in fruits:
        print(i)

def create_and_print_dictionary():
    """Task 8: Create a dictionary named `person` with keys 'name' and 'age', then print the dictionary."""
    person = {"name": "Roger", "age": 42}
    print(person)

def update_age_in_dictionary(person):
    """Task 9: Update the 'age' in the `person` dictionary to a new value and print the updated dictionary."""
    person = {"name": "Roger", "age": 42}
    print(person)
    person['age'] = 20
    print(person)
def check_number_greater_than_10():
    """Task 10: Check if a number stored in a variable is greater than 10 and print a relevant message."""
    number = 5
    if number > 10:
        print(number, "is greater than 10")
    else:
        print(number, "is smaller than 10")

def main():
    # Call each function to execute the tasks
    print_hello_world()
    create_and_print_variables()
    sum_two_numbers()
    greet_user()
    fruits = create_list()
    add_fruit_to_list(fruits)
    print_fruits(fruits)
    person = create_and_print_dictionary()
    update_age_in_dictionary(person)
    check_number_greater_than_10()

if __name__ == "__main__":
    main()
