import pydoc

def basics():
    r="""
        Rule 1: Dictionaries are mutable (they can be changed after creation)
        Rule 2: Each item in a dictionary is a key value pair
        Rule 3: create Dictionaries using {key:value}
        Rule 4: A dictionary can contain different data types
        Rule 5: Dictionary cannot have duplicate keys but can have duplicate values
    
    
        #####################
        ##Create Dictionary##
        #####################
    
        #Example 1: Create Empty Dictionary
        cars = dict()
        
        #Example 2: Create Dictionary containing same data types#
        cars = {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger'}

        #Example 2: Dictionary containing various datatypes#
        randominfo = {'cars':['Chevy','Ford','Dodge'], 'owner':'russmax', 'age':40}
    
    
    
        ######################################
        # Access keys/values in a dictionary #
        ######################################
        
        Example:  cars = {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger'}

        #access dictionary item key to get it's value#
        print(cars['Ford'])

        output: Mustang
        
     
    
        ###############################
        # Add to existing dictionary #
        ###############################

        Example:  cars = {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger'}

        #add new key/value pair to existing dictionary

        cars['Nissan'] = 'GTR'
        print(cars)

        output: {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger','Nissan':'GTR'}
    
    

        ##################################################
        # Merge a dictionary into an existing dictionary #
        ##################################################

        Example:  cars = {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger'}

        Example new dictionary:  newcars = {'Toyota':'Supra', 'Acura':'NSX'}

        cars.update(newcars)
        print(cars)

        output: {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger','Toyota':'Supra','Acura':'NSX'}
    


        ##################################################
        # Merging two dictionaries into a new dictionary #
        ##################################################

        cars = {'Chevy':'Camaro','Ford':'Mustang','Dodge':'Charger'}
        newcars = {'Toyota':'Supra', 'Acura':'NSX'}

        allcars = {**cars, **newcars}

        Note:  Example uses the unpacking operator
    


        #############################################
        # Convert different datatypes to dictionary #
        #############################################

        ## Convert list to dictionary ##
        
        studentList = ['Student1', 'Russ', 'Student2', 'Jon', 'Student3', 'Mike']
        studentDict = { studentList[i]: studentList[i + 1] for i in range(0, len(studentList), 2)}
        print(studentDict)

        output: {'Student1': 'Russ', 'Student2': 'Jon', 'Student3': 'Mike'}

    
        ## Convert list of tuples to dictionary ##
        
        studentList2 = [('Student1', 'Russ'), ('Student2', 'Jon'), ('Student3', 'Mike')]
        studentDict2 = {studentList2[i][0]: studentList2[i][1] for i in range(0, len(studentList2), 1)}
        print(studentDict2)

        output: {'Student1': 'Russ', 'Student2': 'Jon', 'Student3': 'Mike'}


        ## Convert tuple to a dictionary ##
        
        names_and_ages_tup = (('Russ', 45), ('Jon', 46), ('Mike', 49))
        names_and_ages_dict = dict(names_and_ages_tup)
        
        print(names_and_ages_dict)

        output: {'Russ': 45, 'Jon': 46, 'Mike': 49}

    """
    pydoc.pager(r)


