import getpass

def svc_login(user, passwd):
    print('user:{},passwd:{}'.format(user, passwd))
    return True

user = getpass.getuser()
passwd = getpass.getpass()


if svc_login(user, passwd):
    print('Yay!')
else:
    print('Boo!')
