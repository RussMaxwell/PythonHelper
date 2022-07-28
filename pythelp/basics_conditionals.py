import pydoc

def basics():
    r="""
        ## Conditionals - if - elif - else ##
        
        Conditionals allow a program to compare one or more values.  If the result is true, the 
        code defined within the conditional check will execute.  In Python, you use the if, elif, and else statements.
    
    
        Example 1: use if statement to check a string
        -------------------------------------------------
        res = 'test'

        if res == 'test':
            print('the result evalutes to true')

        output: the result is true
    

        
        Example 2: use if else statement to check a string
        ----------------------------------------------------
        res = 'no'

        if res == 'test':
            print('the result evalutes to true')

        else:
            print('the result evaluated to false')
    
        output: the result evaluated to false
    


        Example 3: check if number is greater than 5
        -----------------------------------------------
        res = 8

        if res > 5:
            print('8 is larger than 5')

        output: 8 is larger than 5



        Example 4: use elif to do a second check 
        -----------------------------------------
        res = 4

        if res > 5:
            print('8 is larger than 5')

        elif res == 4:
            print('The result is 4')

        else:
            print('the number is less than 5')


        output: The result is 4
    """
    #print(r)
    pydoc.pager(r)

