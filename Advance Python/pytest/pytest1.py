#pip install pytest

#Unit Test
def addition(a,b):
    return a + b


#Base test :this function is testing the addition function
#1. function mean 1 test 
def test_addition():
    assert addition(20,20)  == 40
    assert addition(-10,10) == 0
    assert addition(-10,-50) == -60


#Advance testing 
# If we are Using the test  before the funvtion name then 
# That will be treated as a test function 
def test_addition():
    assert addition(0,0) ==0
    assert addition(0,100) == 100
    assert addition(10000,50000) == 60000
    assert addition(3.5,4.5) ==8.0
    assert addition(-8.1,-2.9) == -11.0