import string
import re
# password = "Rohit.tupe21"
password = "rohitT3u"
#
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
import re

flag = 0
while True:
    if (len(password) < 8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")
