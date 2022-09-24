
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        lst = [ 'dog', 'cat', 'horse', 'gerbil', 'hamster', 'ferret']
        if species.lower() in lst:
            
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        if self.name_str:
            result_str = "Species of: {:s}, named {:s}".format(self.species_str, self.name_str)
        else: 
            result_str = "Species of: {:s}, unnamed".format(self.species_str)
            
        return result_str
    
        

##
## Class Dog -- not complete
##

class Dog( Pet ):
    def __init__(self, name='', chases='Cats'):
        self.chase = chases.title()
        Pet.__init__(self, 'dog', name)
        
    
    def __str__( self ):
        strn=Pet.__str__(self)
        strn=strn+', chases {}'.format(self.chase)
        
        return strn 
    

##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    def __init__(self, name='', hates='Dogs'):
        self.hate=hates.title()
        Pet.__init__(self, 'cat', name)
    def __str__(self):
        strn=Pet.__str__(self)
        strn=strn+', hates {}'.format(self.hate)
        return strn
        

