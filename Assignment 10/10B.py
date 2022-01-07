name = input("Enter your Details:\nName: ")
gender = input("Gender: ")
phone = input("Phone: ")
dob = input("Dob: ")


def handling(dob):
    d, m, y = dob.split('/')
    d = int(d)
    m = int(m)
    y = int(y)
    try:
        if(m < 1 or m > 12):
            raise Exception
        if(d < 1 or d > 31):
            raise Exception
        if(y < 1000 or y > 9999):
            raise Exception
        if not ((y % 400 == 0) or (y % 100 != 0) and (y % 4 == 0)):
            if(m == 2 and d > 28):
                raise Exception
        if(m == 4 or m == 6 or m == 9 or m == 11):
            if(d > 30):
                raise Exception
        return True
    except:
        print('An invalid date is entered.')


handling(dob)
