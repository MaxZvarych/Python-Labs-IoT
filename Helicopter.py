class Helicopter:
    __colour= "Green"
    def __init__(self,numberOfPassengers=6,name="Cargobob",maxSpeed=250,numberOfScrews=4,fuelType="biodiesel"):
        self.numberOfPassengers=numberOfPassengers
        self.name=name
        self.maxSpeed=maxSpeed
        self.numberOfScrews=numberOfScrews
        self.fuelType=fuelType
    def __del__(self):
        print("Видалення екземпляра:"+ self.__str__())
        del self.name
        del self.fuelType
        del self.maxSpeed
        del self.numberOfPassengers
        del self.numberOfScrews

    @staticmethod
    def getColour():
        return Helicopter.__colour
    def __str__(self):
        return "Colour=:" + Helicopter.__colour + ", numberOfPassengers:" + str(self.numberOfPassengers) + ", name:" + self.name \
               +", maxSpeed:" + str(self.maxSpeed) +", numberOfScrews:" + str(self.numberOfScrews) +", fuelType:" + self.fuelType

    def __repr__(self):
        return "Helicopter [Colour:" + Helicopter.__colour + ", numberOfPassengers:" + str(self.numberOfPassengers) + ", name:" + self.name \
               + ", maxSpeed:" + str(self.maxSpeed) + ", numberOfScrews:" + str(self.numberOfScrews) + ", fuelType:" + self.fuelType + "]"


def main():
    cargobob= Helicopter(6,"Cargobob-222",300,2)
    cargobob.getColour()
    print(cargobob)
    repr(cargobob)
    maverick=Helicopter(maxSpeed=275,name="Maverick")
    print(maverick)
    bell=Helicopter(name="Bell-205",numberOfPassengers=8)
    print(bell)
main()




