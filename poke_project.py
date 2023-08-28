#creating a class for expenses
class expenses:
    global rest_money
    #we create a attributes with the expenses we have
    def __init__(self,rent,metro,food,saving,electricity,internet,gas):
        self.rent = rent
        self.metro = metro
        self.food = food
        self.saving = saving
        self.electricity = electricity
        self.internet = internet
        self.gas = gas
    #we create a variable called rest_money where we substractthe money we have called "salary" with expenses we have.
    def distribution(self,salary):
        rest_money = (salary - abs(self.rent -self.metro- self.food- self.saving - self.electricity - self.internet- self.gas ))
        print("my salary is: ",salary)
        print("my net income is: ", rest_money)
    #in this method we are printing the money we have after expenses called "rest_money"
    def saving(self):
        print("mmy money i have for saving is: ", rest_money)
    #we create a child class
    #new attributes "death", "sickness"
class emergency(expenses):
     def __init__(self,rent,metro,food,saving,electricity,internet,gas,death,sickness):
         self.death = death
         self.sickness = sickness
         expenses.__init__(self,rent,metro,food,saving,electricity,internet,gas)
    #method ro print and addition in "death" and "sickness" attribute.
     def extra_expenses(self):
         print("this is my savigs for health problems: ",self.death + self.sickness)

money_1 = expenses(22,56,7,8,98,432,12)
money_1.distribution(1234)
money_2 = emergency(22,56,7,8,98,432,12,20,50)
money_2.extra_expenses()
