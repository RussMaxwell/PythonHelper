def basics():
    cr="""
        #######################################
        Create a List and store different types
        #######################################
        
        ##Create a List of strings##
        Example list -> names = ['Russ', 'Jon', 'Mike', 'Dan']

        ##Create a list of strings and numbers##
        names_ages = ['Russ',45,'Jon', 44, 'Mike',48,'Dan',46]
    
        ##List containing strings and lists##
        carcontainsmileage = ['mustang',[42858], 'bronco',[2300], 'suburban',[35888]]
    
        ##list containing dictionaries##
        names_ages_dict = [{'Russ':45,'Jon':44},{'Mike':48, 'Dan':46}]
    
        ##list containing tuples##
        names_ages_tupl = [('Russ',45),('Jon',44),('Mike',48),('Dan',46)]

    
    
        ##############################
        ##Access items within a list##
        ##############################
    
        Example list -> names = ['Russ', 'Jon', 'Mike', 'Dan']
    
        option 1: print(names.__getitem__(2))
        output: 'Mike'

        option2: print(names[2])
        output: 'Mike'
    
        option 3: for n in names:
                      print(n)
    
        output: Russ
                Jon
                Mike
                Dan

   

        ################
        Updating a Lists
        ################
    
        Example list -> names = ['Russ', 'Jon', 'Mike', 'Dan']
    
        ##Append string to end of list##
        names.append('Jeff')
        print(names)
        Output: ['Russ', 'Jon', 'Mike', 'Dan', 'Jeff']
    
        ##Remove the first name from the existing list##
        names.remove(names[0])
        output: ['Jon','Mike','Dan']
    

        #########################################
        Combine multiple lists into a single list
        #########################################
       
        Example list 1 -> names1 = ['Russ', 'Jon']
        Example list 2 -> names2 = ['Mike', 'Dan']
       
        names = names1 + names2
        output: ['Russ', 'Jon', 'Mike', 'Dan']

    

        ####################################
        Convert different datatypes to lists
        ####################################
    
        ##Convert tuple to list##
        mytuple = (1,2,3)
        mylist = list(mytuple)
    
        output: [1, 2, 3]
    
        ##Convert string to list##
        namestr = 'russmax'
        namelst = list(namestr)
    
        output: ['R', 'u', 's', 's', 'm', 'a', 'x']
    
        ##Convert dictionary to list##
        namedict = {'first':'russ','last':'max'}
        names = list(namedict.items())
    
        output: [('first', 'russ'), ('last', 'max')]
    
    """
    print(cr)

