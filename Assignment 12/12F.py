import datetime


class Time:
    def is_valid_time(self, time):
        h, m, s = time.split(':')
        try:
            datetime.time(int(h), int(m), int(s))
            return True
        except:
            return False

    def is_valid_date(self, date):
        d, m, y = date.split('/')
        try:
            datetime.datetime(int(y), int(m), int(d))
            return True
        except:
            return False

    def duration(self, start_time, end_time, date):
        h, m, s = start_time.split(':')
        st = datetime.time(int(h), int(m), int(s))
        h, m, s = end_time.split(':')
        et = datetime.time(int(h), int(m), int(s))
        print(et-st)
        d, m, y = date.split('/')
        d = datetime.datetime(int(y), int(m), int(d))
        t1 = datetime.datetime.combine(d, st)
        t2 = datetime.datetime.combine(d, et)
        try:
            t = t2 - t1
            if str(t)[0] == -1:
                raise Exception
            return t
        except:
            return False


exam = Time()
while True:
    date = input("Enter Date: ")
    if not exam.is_valid_date(date):
        print("Invalid Date entered!\nTry Again\n")
        continue
    start_time = input("Start Time: ")
    if not exam.is_valid_time(start_time):
        print("Invalid starting time entered!\nTry Again\n")
        continue
    end_time = input("End Time: ")
    if not exam.is_valid_time(end_time):
        print("Invalid ending time entered!\nTry Again\n")
        continue
    if(exam.duration(start_time, end_time, date) == False):
        print("Invalid duration of Exam!")
    else:
        print("Duration of Exam:", exam.duration(start_time, end_time, date))
    break
