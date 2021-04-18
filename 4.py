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


