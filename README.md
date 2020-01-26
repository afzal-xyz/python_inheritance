## Purpose of the project
This project will provide you a step-by-step guide to create an abstract and non-abstract classes in Python.


## Verify locally
To test this module locally:
* Open up a terminal at the project root
* Run command `pytest -k module1`


## Task 1: Define abc imports
Import ABC and abstractmethod in the first line
```
from abc import ABC, abstractmethod
```

## Task 2: Define Vehicle and Car classess
The Vehicle will be a subclass of ABC and has abstractmethods setTirePressure and getTirePressure.

```
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

    def getTirePressure(self, tire):
        pass

    def setTirePressure(self, tire, pressure):
        pass
```

## Task 3: Implement Car methods logic
We are going to introduce a color and tirePressure attributes. Tires will be identified as
fr=front right, fl=front left, rr=rear right, rl=rear left. Their values be initialized as zero.

```
class Car(Vehicle):
    '''First non abstract class which can be instantiated'''
    def __init__(self, name, color):
        super(Car, self).__init__(name)
        self.color = color
        self.tirePressures = {'fr':0, 'fl':0, 'rr':0, 'rl':0}

    def getTirePressure(self, tire):
        return self.tirePressures[tire]

    def setTirePressure(self, tire, pressure):
        self.tirePressures[tire]=pressure
        print('{0} car pressure has been set to {1}.'.format(self.name, self.tirePressures[tire]))
        return True
```

## Task 5: Check the tire name in the Car class.
Ensure that in the Car class, tires can only be identified as fr, fl, rr or rl
```
    def getTirePressure(self, tire):
        if tire not in self.tirePressures.keys():
            raise Exception('Tire value can only be fr, fl, rr or rl')
        return self.tirePressures[tire]

    def setTirePressure(self, tire, pressure):
        if tire not in self.tirePressures.keys():
            raise Exception('Tire value can only be fr, fl, rr or rl')

        self.tirePressures[tire]=pressure
        print('{0} car pressure has been set to {1}.'.format(self.name, self.tirePressures[tire]))
        return True
```

## Task 6: Check tire pressure value type in the Car class.
Ensure tire pressure can only be a float value in the Car class.
```
    def setTirePressure(self, tire, pressure):
        if tire not in self.tirePressures.keys():
            raise Exception('Tire value can only be fr, fl, rr or rl')

        if not isinstance(pressure, float):
            raise Exception('Pressure must be a float value')

        self.tirePressures[tire]=pressure
        print('{0} car pressure has been set to {1}.'.format(self.name, self.tirePressures[tire]))
        return True
```

## Task 7: Check tire pressure value ranges in the Car class.
Ensure tire pressure is between 0.0 and 36.0

```
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
```
