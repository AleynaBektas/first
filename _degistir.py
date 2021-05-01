from abc import ABC, abstractmethod
#Destructor(Yıkıcı veya Yok edici) olarak adlandırılan fonksiyonlar ise,constructor fonksiyonunun yaptıgı işin tersini
# yaparlar,yani gorevi biten nesneyi yok ederler.Bir sınıfın(class) uyesi olan bir degisken(orn:string tipli)
# gorevini noktaladigi durumda ~destructor() fonksiyonu otomatik cagrilarak,uzerinde calistigi nesneyi devre dışı bırakır
class my_errorclass(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Graj():
    def __init__(self):
        self.wheel_number=0
        self.vehicles=[]
    def AddVehicle(self,vehicle):
        if((self.wheel_number + vehicle.GetWheelSize()) <=80):
            self.vehicles.append(vehicle)
            self.wheel_number += vehicle.GetWheelSize()
            print(my_park.VehicleParking(vehicle))
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

class Park(Graj):
    def __init__(self):
        self.park=[]
        self.park_vehicle=[]
        self.i=0
        self.b=0
        self.a=0
        self.k=0
    def VehicleParking(self,vehicle):
        if(self.park_vehicle.count(vehicle)==0):
            if (self.park.count('-')>= 2):
                if(vehicle.lena()==2):
                    for i in self.park:
                        if(i=='-'):
                            self.c = self.park.index(i)
                            if ((self.park[self.c + 1])=='-'):
                                self.c=self.park.index(i)
                                self.park.pop(self.c)
                                self.park.insert(self.c,'+')
                                self.park.pop(self.c+1)
                                self.park.insert(self.c+1, '+')
                elif(vehicle.lena()==4):
                    for i in self.park:
                        if(i=='-'):
                            self.c = self.park.index(i)
                            if ((self.park[self.c + 1:self.c+5]) == '-'):
                                self.d = self.park.index(i)
                                self.park.pop(self.d)
                                self.park.insert(self.d, '+')
                                self.park.pop(self.d + 1)
                                self.park.insert(self.d + 1, '+')
                                self.park.pop(self.d + 2)
                                self.park.insert(self.d + 2, '+')
                                self.park.pop(self.d + 3)
                                self.park.insert(self.d + 3, '+')
                return self.park

            else:
                self.park_vehicle.append(vehicle)
                for i in range(vehicle.lena()):
                    self.park.insert(self.i,'+')
                    self.i+=1
                return ((self.i) - vehicle.lena()),self.park
        else:
            print("this vehicle is already inside")
            self.k=1
            if(self.k==1):
                for i in self.park_vehicle:
                    if(i!=vehicle):
                        if(i.GetWheelSize()==4):
                            self.b+=2
                        elif(i.GetWheelSize()==18):
                            self.b+=4
                    if(i==vehicle):
                        j=self.b
                        break
                j=self.b
                self.b=0
            return j,self.park
            #raise my_errorclass("this vehicle is already inside")

    def LeaveThePark(self,vehicle):
        a=my_park.VehicleParking(vehicle)[0]
        for i in range(vehicle.lena()):
            self.park.pop(a+i)
            self.park.insert((a+i),'-')
        
        return a,self.park


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
#print(my_park.VehicleParking(opel))
#except my_errorclass as errr:
    #print(errr)
print(my_park.LeaveThePark(volvo))
print(my_park.LeaveThePark(wosvagen))
print(my_park.LeaveThePark(pejo))
print(my_park.VehicleParking(pejo))
#print(my_park.VehicleParking(cooper))
try:
    print(my_graj.GetVehicle("34SD4071"))
except my_errorclass as err:
    print(err)

try:
    print(my_graj.removeVehicle("34SD4071"))
except my_errorclass as er:
    print(er)





