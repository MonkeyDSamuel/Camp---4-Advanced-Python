from models.RBI import RBI

class UBI(RBI):

    
    def get_rate_of_interest(self):     #overriding parent class implementation
        return 9.5
    def display_rate_of_interest(self):
        return ("UBI rate of intrest is: ", self.get_rate_of_interest())