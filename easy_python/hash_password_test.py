import hashlib

solt = "mmf" #加盐
List = []
def get_password(password):
    md5 = hashlib.md5()
    md5.update((password+solt).encode('ascii'))
    List.append(md5.hexdigest())

def last(mes):
    if mes == 1:
        print("right")
    else:
        print('error')

def password_test(password):
    md5 = hashlib.md5()
    md5.update((password+solt).encode('ascii'))
    for i in List:
        if i == md5.hexdigest():
            return last(1)
    return last(0)

password1 = "a123456"
password2 = "123456"
get_password(password1)
password_test(password1)
password_test(password2)

