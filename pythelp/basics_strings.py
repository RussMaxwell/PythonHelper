def basics():
    crstr = """
    
        ###############
        Create a string
        ###############

        ##Create a string##
        
        Option 1: bird1 = 'cardinal'
        Option 2: bird2 = "bluejay"

        Note: Create a multi-line string by encapsulating in """   """


  
        #####################################
        ##Access characters within a string##
        #####################################

        Using Example:  bird1 = 'cardinal'

        ##Access and print the d in cardinal##
        print(bird1[3])    

        output: d


        ##Print each char in a string##
        for b in bird1:
            print(b)
        
        output: c
                a
                r
                d
                i
                n
                a
                l
    
 

        ################
        Combine a string
        ################

        example strings:
        bird1 = 'eagle'
        bird2 = 'falcon'

        ##Combine two strings##
        birds = bird1 + bird2
    


       ##################################
       Slice existing string and merge 
       with a new string
       ##################################

       Example: birds = "eagles, bluejays"
       whichbird = "I like " + birds[8:]
       print(whichbird)

       output: I like bluejays     
    

       #######################################
       Use __add__() to add chars to existing 
       list assign the result to a new string
       #######################################
       
       Example: birds = "Orioles "
       oriole = birds.__add__("are the best!")
       print(oriole)

       output: Orioles are the best!
   


       ####################################
       #Find one or more chars in a string#
       ####################################

       bird = 'cardinal'
       res = bird.__contains__('card')

       print(res)

       output: True


       #################################
       #Return index location of a char#
       #################################

       bird = 'cardinal'
       loc = bird.find('n')
       print(loc)

       output: 5


    
       ######################################
       convert different datatypes to strings
       ######################################

       ##Convert list to string##
       hellolst = ['h','i',' ','m','o','m']
       mom = str.join('',hellolst)
       print(mom)

       output: hi mom
      

       ##Convert tuple to string##
       hellotup = ('hi', ' mom')
       mom = str.join('',hellotup)
       print(mom)

       output: hi mom
    
    """
    print(crstr)

