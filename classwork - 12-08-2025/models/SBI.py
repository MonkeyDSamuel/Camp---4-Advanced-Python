from models.RBI import RBI

class SBI(RBI):
    mudra_loan = 100000.0   #static/class variable
    
    def get_rate_of_interest(self):     #overriding parent class implementation
        return 8.5
    def display_rate_of_interest(self):
        return ("SBI rate of intrest is: ", self.get_rate_of_interest(), super().get_rate_of_interest())