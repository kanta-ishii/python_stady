class Gear:
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel
        
    @property
    def chainring(self):
        return self.__chainring
    @property
    def cog(self):
        return self.__cog
    @property
    def wheel(self):
        return self.__wheel
    def ratio(self):
        return self.chainring / float(self.cog)
    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()


class Wheel:
    def __init__(self, rim, tire):
        self.__rim = rim
        self.__tire = tire
    
    @property
    def rim(self):
        return self.__rim
    @property
    def tire(self):
        return self.__tire
    def diameter(self):
        return self.rim + (self.tire*2)


wheel = Wheel(26, 1.5)
Gear(52, 11, wheel).gear_inches()