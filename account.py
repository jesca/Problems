class Account:
        def __init__(self, name_input, pin_input):
                self.name = name_input
                self.pin= pin_input
                self.value = 0.0

        def deposit(self, amount):
                self.value += amount
                print "Thanks! You have successfully deposited: $", amount

        def withdraw(self, amount):
                self.check_pin()
                if self.value < amount:
                        print "Insufficient funds"
                else:
                        self.value = self.value - amount
                        print "Thank you! You hve successfully withdrew $", amount
                        return amount

        def check_pin(self):
                input = raw_input("Please enter your pin: ")
                # fill in the rest 

        def getValue(self):
                return self.value
