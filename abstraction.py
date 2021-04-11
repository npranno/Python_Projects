

from abc import ABC, abstractmethod #imports ABC and abstractmethod from abc module

class shoes(ABC):
    #defines amount of the purchase of said shoes
    def payAmount(self, amount):
        print("Your shoes cost: ",amount)
    #@abstractmethod tells user to pass in an argument, but the data isn't defined yet
    @abstractmethod
    def payment(self,amount):
        pass #passes this function for something to be called later

class giftCard(shoes): #child class of shoes, defining that the payment is a gift card
    def payment(self, amount): #payment is defined separately within this class
        print("Your gift card balance is not enough to purchase this item costing {}.".format(amount))

obj = giftCard()
obj.payAmount("$60") #calls pay amount in parent class, and response
obj.payment("$60") #calls payment in child class, and response
