import pydoc

def basics_for():
    r="""
        For Loop
        ----------
        A for loop is a great way to iterate through elements of a data structure.  Lots of use cases exists for implementing a for loop.  
        For Example, perhaps you simply want to print the value of each element.  Or, perhaps you want to call a function if an 
        element meets a certain condition. Some examples are below.       
    

        Example 1: Iterate through a List
        ----------------------------------
        def processlist(numbers):
            for num in numbers:
                print(num)

        mylist = [5,2,8,9]
        processlist(mylist)
    
        output: 5
                2
                8
                9
    


        Example 2: Iterate through dictionary items 
        --------------------------------------------
        def process(names):
            for student in names.items():
                print(student)
 
        students = {'student1':'Jon','student2':'Mike','student3':'Russ'}
        process(students)

        output: ('student1', 'Jon')
                ('student2', 'Mike')
                ('student3', 'Russ')
    


        Example 3: Iterate through dictionary keys
        ------------------------------------------
        def process(names):
           for student in names.keys():
               print(student)
 
        students = {'student1':'Jon','student2':'Mike','student3':'Russ'}
        process(students)

        output: student1
                student2
                student3



        Example 4: Iterate through dictionary values
        --------------------------------------------
        def process(names):
           for student in names.values():
               print(student)
 
        students = {'student1':'Jon','student2':'Mike','student3':'Russ'}
        process(students)

        output: Jon
                Mike
                Russ

    """
    pydoc.pager(r)

def basics_while():
    r="""

        While Loop
        ----------
        A while loop is a great way to iterate through elements of a data structure as long as a condition is true.  
        Lots of use cases exists for implementing a for loop.  For Example, perhaps you simply want to print 
        the value of each element. 
    

        Example 1:  Print list items 
        -----------------------------
        def process(names):
            ctr = 0
  
            while ctr < len(names):
                print(names[ctr])
                ctr+=1
  
        students = ['Brent','Jon','Russ']
        process(students)
          
    """
    pydoc.pager(r)