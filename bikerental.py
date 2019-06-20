class BikeRent:
    stock = 100
    def __init__(self, inv):
        self.inv = inv
    def bike_on_hourly(self, no_of_bikes, no_of_hours):
        self.no_of_bikes = no_of_bikes
        self.no_of_houres = no_of_hours
        return no_of_bikes*no_of_hours*5
    def bike_on_daily(self, no_of_bikes, no_of_day):
        self.no_of_bikes = no_of_bikes
        self.no_of_day = no_of_day
        return no_of_bikes*no_of_day*20
    def bike_on_weekly(self, no_of_bikes, no_of_week):
        self.no_of_bikes = no_of_bikes
        self.no_of_week = no_of_week
        return no_of_bikes*no_of_week*60
print("The number of bikes available is : 100")
print("Rent bikes on hourly basis $5 per hour.")
print("Rent bikes on daily basis $20 per day.")
print("Rent bikes on weekly basis $60 per week.")
X = int(input("Enter the number of bikes you want"))
OBJ = BikeRent(X)  
if X > 100:
    print("Only 100 bikes are available,Enter a number less than 100") 
else:
    ITEM = input("Enter hourly or daily or weekly ")
    if ITEM == "hourly":
        THR = int(input("Enter the number of hours you want the bike for"))
        C = OBJ.bike_on_hourly(X, THR)
        print("Your Total amount is : Rs", C)
    elif ITEM == "daily":
        TDY = int(input("Enter the number of days you want the bike for")) 
        C = OBJ.bike_on_daily(X, TDY)
        print("Your Total amount is : Rs", C)
    elif ITEM == "weekly":
        TWE = int(input("Enter the number of weeks you want the bike for")) 
        C = OBJ.bike_on_weekly(X, TWE)
        print("Your Total amount is : Rs", C)
    else:
        print("Give a valid response")
    

        
        
        