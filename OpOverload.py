class MyList:
    def __init__(self,value,*args):
        self.values = []
        if len(args) == 0:
            if isinstance(value,list):
                self.values = value
            else:
                self.values += [value]
        else:
            if isinstance(value,list):
                self.values = value
                for i in args:
                    self.values += [i]
            else:
                self.values += [value]
                for i in args:
                    self.values += [i]

    def __eq__(self, number: 'int'):
        ans = []
        for i in self.values:
            if i == number: ans += [i]
        return ans

    def __gt__(self, number: 'int'):
        ans = []
        for i in self.values:
            if i > number: ans += [i]
        return ans

    def __ge__(self, number: 'int'):
        ans = []
        for i in self.values:
            if i >= number: ans += [i]
        return ans

    def __lt__(self, number: 'int'):
        ans = []
        for i in self.values:
            if i < number: ans += [i]
        return ans

    def __le__(self, number: 'int'):
        ans = []
        for i in self.values:
            if i <= number: ans += [i]
        return ans

    def __getitem__(self, input):
        return input

    def __iadd__(self,addition):
        if isinstance(addition,list):
            for i in addition:
                self.values.append(i)
        elif isinstance(addition,MyList):
            for i in addition.values:
                self.values.append(i)
        else:
            self.values += [addition]
        return self.values

    def __str__(self):
        out = '['
        out += str(self.values[0])
        for i in range(1, len(self.values)):
            out += ', '
            out += str(self.values[i])
        out += ']'
        return out

    def __add__(self, number: 'int'): #И куча других арифметических и не только операций
        for i in self.values:
            i += number


a = MyList([1,2,3,4,5,6,7,8,9,10])
print(a[a > 2])
print(a==3)
print(a<=7)
print(a)

b =MyList(1,2,3,4,5,6)
print(b[b>=3])
print(b<5)
print(b==10)
a += b
print(a)
