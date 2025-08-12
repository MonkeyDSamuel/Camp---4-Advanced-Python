class Interest:
    def __init__(self, principal : float, time : float, acc_type : str):
        self.__principal = principal
        self.__time = time
        self.__type = acc_type
        #set the interest rate based on account type
        if acc_type.lower() == "saving":
            self.__rate = 11.0
        elif acc_type.lower() == "fixed":
            self.__rate = 4.0
        else:
            raise ValueError("Invalid account type")

    @property
    def get_principal(self):
        return self.__principal
    
    # @get_principal.setter
    # def set_principal(self, amount):
    #     if not isinstance(amount,float):
    #         raise ValueError("The amount must be of float type")
    #     elif not amount:
    #         raise ValueError("The amount must be present")
    #     else:
    #         self.__principal = amount
    
    @property
    def get_time(self):
        return self.__time
    
    # @get_time.setter
    # def set_time(self, time):
    #     if not isinstance(time, float):
    #         raise ValueError("The time entered must of float type")
    #     elif not time:
    #         raise ValueError("The time must be entered")
    #     else:
    #         self.__time = time
    
    @property
    def get_rate(self):
        return self.__rate
    
    # @get_rate.setter
    # def set_rate(self, rate):
    #     if not isinstance(rate, float):
    #         raise ValueError("The rate must be of float type")
    #     elif not rate:
    #         raise ValueError("The rate must be entered")
    #     else:
    #         self.__rate = rate

    @property
    def get_type(self):
        return self.__type


    def __str__(self):
        return f"""
                Account type: {self.__type}
                Principal Amount: {self.__principal}
                Interest rate: {self.__rate}
                Duration: {self.__time}
                """