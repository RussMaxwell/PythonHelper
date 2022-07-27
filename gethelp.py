import pythelp.basics_functions as function_help
import pythelp.basics_conditionals as conditional_help
import pythelp.basics_lists as list_help
import pythelp.basics_loops as loop_help
import pythelp.basics_strings as string_help
import pythelp.basics_tuples as tuple_help
import pythelp.basics_dictionaries as dictionary_help



def menu():
    res ="""
        ########################
        ####   Python Help  ####
        ########################
        For help on a given topic, enter the number associated and press enter.

        1. Dictionaries 
        2. Strings
        3. Lists
        4. Tuples 
        5. For Loop
        6. While Loop
        7. Conditionals (if..else)
        8. Functions
        9. Dynamic Arguments
        10. Keyword Arguments
        
        Press 0 to Quit
       
    """
    print(res)


def decide(res):
    
    if res == 1:
        dictionary_help.basics()

    elif res == 2:
        string_help.basics()
    
    elif res == 3:
        list_help.basics()

    elif res == 4:
        tuple_help.basics()

    elif res == 5:
        loop_help.basics_for()

    elif res == 6:
        loop_help.basics_while()

    elif res == 7:
        conditional_help.basics()

    elif res == 8:
        function_help.basics()

    elif res == 9:
        function_help.dynamicarguments()

    elif res == 10:
        function_help.keywordarguments()


while True:
    menu()
    user_input = input("Enter Number: ")
    
    try:
        official = int(user_input)

        if official == 0:
            break

        elif official in range(1,11):
            decide(official)
            input("Press any key to go back to Menu")
    
        else:
            print("You entered an invalid number, try again")
            input("Press any key to continue")
            menu()
    

    except ValueError:
        print("You entered an invalid key. Try Again")    
        input("Press any key to continue")    
        