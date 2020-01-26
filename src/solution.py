from abc import ABC, abstractmethod

class Vehicle(ABC):
    '''Abstract class'''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getTirePressure(self, tire):
        pass

    @abstractmethod
    def setTirePressure(self, tire, pressure):
        pass

class Car(Vehicle):
    '''First non abstract class which can be instantiated'''
    def __init__(self, name, color):
        super(Car, self).__init__(name)
        self.color = color
        self.tirePressures = {'fr':0, 'fl':0, 'rr':0, 'rl':0}

    def getTirePressure(self, tire):
        if tire not in self.tirePressures.keys():
            raise Exception('Tire value can only be fr, fl, rr or rl')
        return self.tirePressures[tire]

    def setTirePressure(self, tire, pressure):
        if tire not in self.tirePressures.keys():
            raise Exception('Tire value can only be fr, fl, rr or rl')

        if not isinstance(pressure, float):
            raise Exception('Pressure must be a float value')

        if (pressure<0.0) or (pressure>36.0):
            raise Exception('Pressure can be between 0.0 and 36.0')

        self.tirePressures[tire]=pressure
        print('{0} car pressure has been set to {1}.'.format(self.name, self.tirePressures[tire]))
        return True

