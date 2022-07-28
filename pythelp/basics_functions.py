import pydoc

def basics():
    r="""
        Rule 1: Functions are declared via the def keyword
        Rule 2: Function names have () appended with a colon at the end
        Rule 3: The body of a function is indented so no curly braces
        Rule 4: Functions optionally can take a number parameters 
        Rule 5: Functions optionally can return data to the caller
   
    
        ###################
        # Function Basics #
        ###################


        #### function that takes no arguments and returns None ####

        def printme():
            print('function text here')
        
        printme()

        output: function text here
    


        
        #### function that takes two arguments and returns None ####

        def addme(num1, num2):
            print(num1 + num2)

        addme(5,2)        

        output: 7


        
        #### function that takes no arguments and returns a string ####

        def nameme():
            return "john"

        print(nameme())

        output: john



        #### function that takes arguments and returns a value ####

        def addIt(num1, num2):
            return num1 + num2

        res = addIt(5, 5)
        print(res)

        output: 10

    """
    pydoc.pager(r)


def dynamicarguments():
    r="""
        
        *args Parameter
        -------------------
        It's possible to have a function taken a dynamic number of arguments.  
        Depending on the developers goal, it could be expected that a function will not know 
        the number of arguments coming in and it could be random on every call.  Fortunately, 
        in Python you can simply use the *args parameter.        
    
    
        Example 1: Add numbers that are passed as parameters

        def addme(*args):
            print(sum(args))
        
        addme(5,10,15,20)

        output: 50
    
    
        Note 1: The args data type in this case is a tuple.  

        Note 2: If you would want to use dynamic # of keyword arguments, you would use **kwargs as the parameter.

    """
    pydoc.pager(r)


def keywordarguments():
    r="""
        
        Arguments you pass to a function can be either keyword or non-keyword. 

        Non-Keyword Arguments 
        ------------------
        Non-Keyword Arguments are known as positional arguments. The order you place an 
        argument will map to a functions parameter based on position.  If I have a 
        function with two parameters and call it with two arguments, the first argument
        will map to the first parameter while the second argument will map to the second parameter.

        
        Keyword Arguments
        ----------------------
        Keyword Arguments are non-positional arguments. When calling a function,
        it's possible to map an argument to a parameter regardless of the position of both. 
        An example of both argument types are below.
    

        ## Non-Keyword Argument Example ##

        def greet(fname, lname):
            print(f"Hello {fname} {lname}!")

        greet("John", "Smith")

        output: Hello John Smith!



        ## Keyword Argument Example ##

        def greet(lname, fname):
            print(f"Hello {fname} {lname}!")

        greet(fname="John", lname="Smith")

        output: Hello John Smith!
    
    """
    pydoc.pager(r)