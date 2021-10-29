controle = open('controle.txt','r')

def admin(user):
    adm = 'viniciusfarineli@gmail.com'
    adm1 = 'leandroalrodrigues@gmail.com'
    adm2 = 'vescheifer@gmail.com'

    if user == adm or user == adm1 or user==adm2:
        return  True