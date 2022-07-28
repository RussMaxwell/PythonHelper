import pydoc

def basics():
    r="""
        Rule 1: Tuples are immutable (they cannot be changed after creation)
        Rule 2: Tuples are faster than lists
        Rule 3: create tuples by wrapping values in ()
        Rule 4: A tuple can contain different data types
        Rule 5: can add duplicate values to a single tuple
    

        ##############
        Create a tuple
        ##############

        ##Create tuple of strings##
        names = ('Russ', 'Jon', 'Mike')
        print(names)
        
        output: ('Russ', 'Jon', Mike')    
    
        
        ##Create tuple with mixture of datatypes##
        names_and_ages = ('Russ', 45, 'Jon', 46, 'Mike', 49)

        #Create tuple with one value#
        name = ('Russ',)
        
        
        ########################
        Access values in a Tuple
        ########################

        Example Tuple:  names_and_ages = ('Russ', 45, 'Jon', 46, 'Mike', 49)

        #print the first element#
        print(names_and_ages[0])

        output: Russ


        #iterate thru tuple and print each value#
        for n in names_and_ages:
            print(n)

        output: Russ
                45
                Jon
                46
                Mike
                49

        
        ##get length of Tuple##        
        print(len(names_and_ages))

        output: 6

        
        ##get index location of a desired tuple value##
        print(names_and_ages.index('Mike'))

        output: 4

    
        ############################
        Convert datatypes to a Tuple
        ############################
        
        ##Convert string to tuple##
        randomstr = "Russ"
        newtuple1 = tuple(randomstr)

        ##Convert list to tuple##
        randomlist = [29,'contoso',12,'toys']
        newtuple2 = tuple(randomlist)    


        ##Convert set to tuple##
        randomset = {5,6,7,8}
        newtuple3 = tuple(randomset)
        
        Important Note: Dictionary conversion to a tuple is not a common scenario.  
                        If needed, convert a dictionary to a list of tuples.  
                        Please see list conversions section for more details.

    """
    pydoc.pager(r)

    