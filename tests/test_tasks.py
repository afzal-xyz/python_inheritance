# Importing libraries
import pytest
from src import solution
import ast
import inspect

# -------------------------------------------------
# Pytest for Task 1
# Import ABC and abstractmethod from abc for abstraction
@pytest.mark.test_task1
def test_task1():
    assert 'ABC' in dir(solution), 'Have you imported the ABC from abc?'
    assert 'abstractmethod' in dir(solution), 'Have you imported the abstractmethod from abc?'

# -------------------------------------------------
# Pytest for Task 2
# Checking Vehicle as an abstract class and Car as a non-abstract class

@pytest.mark.test_task2
def test_task2():
    with pytest.raises(TypeError):
        assert solution.Vehicle('test'), 'Vehicle class must be defined as an abstract class.'
    assert solution.Car('test','rest'), 'Car class must be defined inherits from Vehicle class'

# -------------------------------------------------
# Pytest for Task 3
# Checking if we can call Car methods
@pytest.mark.test_task3
def test_task3():
    car = solution.Car('mycar','red')
    assert car.setTirePressure('fr',3.0), 'We should be able to set fr (front right) tire pressure with float value.'
    assert car.setTirePressure('fl',4.0), 'We should be able to set fl (front left) tire pressure with float value.'
    assert car.setTirePressure('rr',5.0), 'We should be able to set rr (rear right) tire pressure with float value.'
    assert car.setTirePressure('rl',6.0), 'We should be able to set rl (rear left) tire pressure with float value.'

    assert car.getTirePressure('fr')==3.0, 'It does not see fr (front right) tire pressure was saved.'
    assert car.getTirePressure('fl')==4.0, 'It does not see fl (front left) tire pressure was saved.'
    assert car.getTirePressure('rr')==5.0, 'It does not see rr (rear right) tire pressure was saved.'
    assert car.getTirePressure('rl')==6.0, 'It does not see rl (rear left) tire pressure was saved.'

# -------------------------------------------------
# Pytest for Task 4
# Car tire pressure value can only be float
@pytest.mark.test_task4
def test_task4():
    car = solution.Car('mycar','red')
    with pytest.raises(Exception):
        assert car.setTirePressure('fr','test'), 'Tire pressure value has to be a float value.'

# -------------------------------------------------
# Pytest for Task 5
# Car tire can be identified as fr, fl, rr or rl
@pytest.mark.test_task5
def test_task5():
    car = solution.Car('mycar','red')
    with pytest.raises(Exception):
        assert car.setTirePressure('test',7.0), 'tire can be identified as fr,fl,rr or rl only.'

# -------------------------------------------------
# Pytest for Task 6
# Car tire pressure cannot be negative
@pytest.mark.test_task6
def test_task6():
    car = solution.Car('mycar','red')
    with pytest.raises(Exception):
        assert car.setTirePressure('rr',-1), 'Tire pressure has to be a positive float value.'
        
# -------------------------------------------------
# Pytest for Task 7
# Care tire pressure cannot be over 36
@pytest.mark.test_task7
def test_task7():
    car = solution.Car('mycar','red')  
    with pytest.raises(Exception):
        assert car.setTirePressure('rr',40.0), 'Tire pressure cannot be more than.'