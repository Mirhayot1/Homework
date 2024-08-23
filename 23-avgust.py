class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __num_shaxs = 0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        Shaxs.__num_shaxs += 1
        
    @classmethod
    def get_num_shaxs(cls):
        return cls.__num_shaxs
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport},  {self.tyil}-yilda tug`ilgan"
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        
class Mirhayot():
    """Mirhayot nomli klass"""
    def __init__(self):
        self.__hususiyat = 'Salom'
    def get_hususiyat(self):
        return self.__hususiyat

obj = Mirhayot()
print(obj.get_hususiyat())   
        
    
inson = Shaxs("Hasan","Alimov","FB001122",1995)
inson = Shaxs("Muhammadali","Saidmamemedov","IR484348",2012)
inson = Shaxs("Elon","Musk","FA843846",2001)
inson = Shaxs("Cristiano","Ranoldo","CR1884384",1985)
print(f"{inson.get_info()}. {inson.get_age(2024)} yoshda.")

talaba = Talaba("Valijon","Aliyev","FA112299",2000)
print(talaba.get_info())
print(Shaxs.get_num_shaxs())
