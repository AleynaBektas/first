from abc import ABC, abstractmethod
#Destructor(Yıkıcı veya Yok edici) olarak adlandırılan fonksiyonlar ise,constructor fonksiyonunun yaptıgı işin tersini
# yaparlar,yani gorevi biten nesneyi yok ederler.Bir sınıfın(class) uyesi olan bir degisken(orn:string tipli)
# gorevini noktaladigi durumda ~destructor() fonksiyonu otomatik cagrilarak,uzerinde calistigi nesneyi devre dışı bırakır
class my_errorclass(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
class Park_info():
    def __init__(self,start_index,vehicle):
        self.star_index=start_index
        self.vehicle=vehicle
class Park():
    def __init__(self):
        self.Park_inLis=[]

    def AddVehicle(self,vehicle):
        if(len(self.Park_inLis)==0):
            self.Park_inLis.append(Park_info(0,vehicle))
            print("x")
        else:
            self.start_indis = 0
            while(self.start_indis < len(self.Park_inLis)-1):
                print(self.start_indis)
                Difference= self.Park_inLis[self.start_indis + 1].start_index - self.Park_inLis[self.start_indis].start_index
                if(vehicle.lena()<= Difference):
                    self.Park_inLis.insert(Park_info(self.start_indis+1,vehicle))
                    return (self.start_indis +1)
                self.start_indis += 1
            if(self.start_indis==len(self.Park_inLis)-1 and  self.Park_inLis.count(vehicle)==0):
                self.Park_inLis.append(Park_info(self.start_indis-1,vehicle))
                print("a")
                self.start_indis+=1
                print(self.start_indis)
        return self.Park_inLis
    """def RemoveVehicle(self,vehicle):
        for i in range(len(self.Park_inLis)-1):
            if(self.Park_inLis[i].vehicle == vehicle):
                self.Park_inLis.pop(i)
                return self.Park_inLis"""


class Graj():
    def __init__(self):
        self.wheel_number=0
        self.vehicles=[]
    def AddVehicle(self,vehicle):
        if((self.wheel_number + vehicle.GetWheelSize()) <=80):
            self.vehicles.append(vehicle)
            self.wheel_number += vehicle.GetWheelSize()
            my_park.VehicleParking(vehicle)
            return True
        return False,"there is no enough place"
    def GetVehicle(self,plate_new):

        for i in self.vehicles:
            if(i.GetPlate()== plate_new):
                return i
        raise my_errorclass('this vehicle is not in the parking')

    def Getavailablewheel(self):
        number=0
        for i in self.vehicles:
            number += i.GetWheelSize()
        return 40 - number

    def removeVehicle(self,plate):
        for i in self.vehicles:
            if(i.GetPlate()== plate):
                self.vehicles.remove(i)
                return i
        raise my_errorclass('this vehicle was removed')

class vehicle(ABC):

    @abstractmethod
    def GetName(self):  # vehicle class a ait ortak bir özellik
        pass
    @abstractmethod
    def GetPlate(self):
        pass
    @abstractmethod
    def GetWheelSize(self):
        pass
    @abstractmethod
    def lena(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

class Car(vehicle):# teker sayısı 4,araç uzunluğu 2 br

    def __init__(self,car_name,plate,wheel_number,lenght):
        super().__init__() # vehicle class ın init fonksiyonunu kullanma
        self.car_name = car_name
        self.plate= plate
        self.wheel_number= wheel_number
        self.lenght = lenght
    def GetName(self):
        return self.car_name
    def GetPlate(self):
        return self.plate
    def GetWheelSize(self):
        return self.wheel_number
    def lena(self):
        return self.lenght
    def __str__(self):
        return "car name={} plate={} wheel_number={}".format(self.GetName(),self.GetPlate(),self.GetWheelSize())


class Truck(vehicle):#teker sayısı 18,araç uzunluğu 4 br
    def __init__(self,car_name,plate,wheel_number,lenght):
        super().__init__() # vehicle class ın init fonksiyonunu kullanma
        self.car_name = car_name
        self.plate= plate
        self.wheel_number= wheel_number
        self.lenght = lenght
    def GetName(self):
       return self.car_name
    def GetPlate(self):
        return self.plate
    def GetWheelSize(self):
        return self.wheel_number
    def lena(self):
        return self.lenght
    def __str__(self):
        return "truck name={} plate={} wheel_number={}".format(self.GetName(),self.GetPlate(),self.GetWheelSize())

"""
opel=Car("opel","34SD4072",4,2)
wosvagen=Car("wosvagen","41HN6351",4,2)
pejo =Car("pejo","34AB2461",4,2)
cooper=Car("Cooper","52DG6362",4,2)
volvo=Truck("volvo","41YN151",18,4)
renault= Truck("renault","41YN150",18,4)
ford=Truck("ford","34UJ5656",18,4)
my_graj=Graj()
my_park=Park()
print(my_graj.Getavailablewheel())
print(my_graj.AddVehicle(opel))
print(my_graj.Getavailablewheel())
print(my_graj.AddVehicle(volvo))
print(my_graj.Getavailablewheel())
print(my_graj.AddVehicle(wosvagen))
print(my_graj.Getavailablewheel())
print(my_graj.AddVehicle(pejo))
print(my_graj.AddVehicle(renault))
#try:
print(my_park.VehicleParking(opel))
#except my_errorclass as errr:
    #print(errr)
print(my_park.LeaveThePark(opel))
print(my_park.LeaveThePark(volvo))
print(my_park.VehicleParking(opel))
print(my_park.VehicleParking(cooper))
try:
    print(my_graj.GetVehicle("34SD4071"))
except my_errorclass as err:
    print(err)

try:
    print(my_graj.removeVehicle("34SD4071"))
except my_errorclass as er:
    print(er)"""


opel = Car("opel", "34SD4072", 4, 2)
wosvagen=Car("wosvagen","41HN6351",4,2)
pejo =Car("pejo","34AB2461",4,2)
cooper=Car("Cooper","52DG6362",4,2)
my_park=Park()
my_park.AddVehicle(opel)
my_park.AddVehicle(wosvagen)
my_park.AddVehicle(pejo)
my_park.AddVehicle(cooper)
print(my_park.Park_inLis)




