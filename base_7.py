# -*- coding: utf-8 -*-
"""
Created on Sun April 2017
@author: jiang
"""
class Car():  #定义类名称

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0


    def descriptive(self):
        """返回整洁的描述性信息"""
        long_name =  str(self.year) + ' '+ self.make +' ' +self.model
        return long_name.title()

    def read_odometer(self):
        """打印车子里程信息"""
        print ("This is has "+ str(self.odometer_reading) + " miles on it.")    

    
    def update_odometers(self,mileage):
        """将里程表度数设置为指定值
           禁止表数回调
        """
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
            print ("You can't back on odometers.")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print("This car  hava a  full tank!")


my_new_car = Car('audi','a4','2017')
print (my_new_car.descriptive())
my_new_car.odometer_reading = 45
my_new_car.read_odometer()
my_new_car.update_odometers(20)
my_new_car.read_odometer()
my_new_car.increment_odometer(15)
my_new_car.read_odometer()


class ElectricCar(Car):
    """电动车的独特之处"""
    
    def __init__(self,make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)
        self.battery_size =  60 


    def fill_gas_tank(self):
        print("This car doesn't hava a tank!")


my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.descriptive())
my_tesla.odometer_reading = 21
my_tesla.read_odometer()
print('This car has a '+ str(my_tesla.battery_size)+ '-KWh battery.')
my_tesla.fill_gas_tank()



