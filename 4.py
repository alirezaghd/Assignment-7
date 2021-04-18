class fraction:
    def __init__(self,s1,m1,s2,m2):
        self.sorat1 = s1
        self.makhrag1 = m1
        self.sorat2 = s2
        self.makhrag2 = m2


    def mul(self):
        s = self.sorat1 * self.sorat2
        m = self.makhrag1 * self.makhrag2
        return (str(s) + '/' + str(m))

    def sum(self):
        s = (self.sorat1 * self.makhrag2) + (self.sorat2 * self.makhrag1)
        m = self.makhrag1 * self.makhrag2
        return (str(s) + '/' + str(m))

    def sub(self):
        s = (self.sorat1 * self.makhrag2)-(self.sorat2 * self.makhrag1)
        m = self.makhrag1 * self.makhrag2
        return (str(s) + '/' + str(m))

    def div(self):
        s = (self.sorat1 * self.makhrag2)/(self.makhrag1*self.sorat2)
        return s


result = fraction(2,3,4,5)


print('(', result.sorat1, '/', result.makhrag1, ')*(', result.sorat2, '/', result.makhrag2, ')=', result.mul())

print('(', result.sorat1, '/', result.makhrag1, ')+(', result.sorat2, '/', result.makhrag2, ')=', result.sum())

print('(', result.sorat1, '/', result.makhrag1, ')-(', result.sorat2, '/', result.makhrag2, ')=', result.sub())

print('(', result.sorat1, '/', result.makhrag1, ')/(', result.sorat2, '/', result.makhrag2, ')=', result.div())


class time():
    def __init__(self,h1,m1,s1,h2,m2,s2):

        self.hour = h1
        self.minute = m1
        self.second = s1
        self.hour1 = h2
        self.minute2 = m2
        self.second2 = s2

    def sum_time(self):
        print("your first time",self.hour,":",self.minute,":",self.second)
        print("your second time",self.hour1,":",self.minute2,":",self.second2)
        h = self.hour + self.hour1
        m = self.minute + self.minute2 
        s = self.second + self.second2

        if m >= 60:
            m -= 60
            h += 1

        if s >= 60:
            s -= 60
            m += 1
        
        return str(h)+':'+str(m)+':'+str(s)

    def sub_time(self):
        print("your first time",self.hour,":",self.minute,":",self.second)
        print("your second time",self.hour1,":",self.minute2,":",self.second2)
        h = self.hour - self.hour1
        m = self.minute - self.minute2 
        s = self.second - self.second2

        return str(h)+':'+str(m)+':'+str(s)

    def second_to_time(self):
        times= self.second
        hour= int(times / 3600)
        times = times % 3600
        minute = int(times / 60)
        second = int(times % 60)
        return str(hour)+':'+str(minute)+':'+str(second)

    def time_to_secend(self):
        hour = self.hour
        minute = self.minute
        second = self.second
        h = hour * 3600
        m = minute * 60
        result = h + m + second
        return result

result = time(2,10,15,5,21,30)
print('sum of two time:',result.sum_time())
print('Subtraction of two time:',result.sub_time())
print('is time: ', result.second_to_time())
print('Seconds: ', result.time_to_secend())
