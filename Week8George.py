class Menu: 
    """ Create a Menu """
    def __init__(self):
        self.selection = selection

    def displayHomeMenu(self):

        if 2 == vehicleCount:
            print("----Press 1 for car ")
            print("----Press 2 for pickup ")
            selection = input("----Press 3 to quit ")
            return selection

        else: 
            print("----Press 1 for car ")
            selection = input("----Press 2 for pickup ")
            return selection


class Vehicle:
    """ Model a vehicle"""

    def __init__(self, make = " ", model = "n/a", color = "n/a ", fuelType = "n/a ", *options):
        """ Initialize vehicle attributes """
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = ['powerwindows', 'powerlocks', 'remotestart', 'backupcamera', 'bluetooth', 'cruisecontrol', 'heatedseats', 'heatedsteeringwheel']
    
    def getMake(self):
        self.make = input("Please enter your make ")
        return self.make
    def getModel(self):
        self.model = input("Please enter your model ")
        return self.model
    def getColor(self):
        self.color = input("Please enter the color ")
        return self.color
    def getFuelType(self):
        self.fuelType = input("Please enter your fuel type ")
        return self.fuelType
    def getOptions(self):
        print("Please select from the following options: ")
        self.options = input(self.options)
        return self.options
   
class Car(Vehicle):

        """Represents a car"""

        def __init__(self, make = "n/a ", model = "n/a", color = "n/a ", fuelType = "n/a "):

            super().__init__(make, model, color, fuelType)

            """ Initialize car attributes"""

            self.engineSize = " "
            self.numDoors = " "

        def getEngineSize(self):
            self.engineSize = input("Please enter your engine size ")
            return self.engineSize
        def getNumDoors(self):
            self.numDoors = input("How many doors do you have ")
            return self.numDoors

class pickup(Vehicle):

        """Represents a pickup"""

        def __init__(self, make = " ", model = " ", color = " ", fuelType = " "):

            super().__init__(make, model, color, fuelType)

            """ Initialize pickup attributes """
            self.cabStyle = " "
            self.bedLength = " "

        def getCabStyle(self):
            self.cabStyle = input("Please enter your cab style ")
        def getBedLength(self):
            self.bedLength = input("Please enter the length of your bed ")


    
            


i = 0
list = []
vehicleCount = 0
carCount = 0
pickupCount = 0
selection = 0

while True:
    vehicleCount = pickupCount + carCount    

                
    m = Menu()

    selection = Menu.displayHomeMenu(m)
    
        
        


    if selection == "1":
            # Processing for item found
        c = Car(Vehicle)

        Vehicle.getMake(c)
        Vehicle.getModel(c)
        Vehicle.getColor(c)
        Vehicle.getFuelType(c)
        Vehicle.getOptions(c)
        Car.getEngineSize(c)
        Car.getNumDoors(c)
        newcar = vars(c)
        list.append(newcar)

        if carCount < 1:

            carCount = carCount + 1
        else:
            pass

            
        
    elif selection == "2":
    # Processing for item not found
        p = pickup(Vehicle)

        Vehicle.getMake(p)
        Vehicle.getModel(p)
        Vehicle.getColor(p)
        Vehicle.getFuelType(p)
        Vehicle.getOptions(p)
        pickup.getCabStyle(p)
        pickup.getBedLength(p)
        newpickup = vars(p)
        list.append(newpickup)

        if pickupCount < 1:
            pickupCount = pickupCount + 1
    else:
        print("You have the following vehicles in your garage: ")
        for i in list:
            print(list)
            break









