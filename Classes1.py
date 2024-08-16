#1-vazifa
class User:
    """Zo'r narsa"""
    def __init__(self,ism,nickname,email):
        
        self.ism = ism
        self.nickname = nickname
        self.email = email

kimdir1 = User('Shuhrat', 'shuhrat11', 'shuhrat11565@gmail.com')
kimdir2 = User('Begzod' ,'Begi.po' ,'begi005@gmail.com')
kimdir3 = User('Rejabboy', 'rejji.chish', 'yondradigoydiradi@gmail.com')

#2-Vazifa
class User:
    """Bir narsa dagan klass"""
    def __init__(self,ism,nickname,email):
        
        self.ism = ism
        self.nickname = nickname
        self.email = email
        
    def get_info(self):
        print(f"Ismi: {self.ism} Nickname: {self.nickname} Elektron pochtasi: {self.email}")


kimdir1 = User('Shuhrat', 'shuhrat11', 'shuhrat11565@gmail.com')
kimdir2 = User('Begzod' ,'Begi.po' ,'begi005@gmail.com')
kimdir3 = User('Rejabboy', 'rejji.chish', 'yondradigoydiradi@gmail.com')

kimdir1.get_info()
