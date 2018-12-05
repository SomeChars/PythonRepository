import math

class Quaternion:
    def __init__(self,free_coefficient,*args):
        self.free_coefficient = free_coefficient
        if args:
            self.i_coefficient = args[0]
            self.j_coefficient = args[1]
            self.k_coefficient = args[2]
        else:
            self.i_coefficient = 0
            self.j_coefficient = 0
            self.k_coefficient = 0

    def __str__(self):
        return str(self.free_coefficient)+" + "+str(self.i_coefficient)+"*i + "+str(self.j_coefficient)+"*j + "+str(self.k_coefficient)+"*k"

    def __eq__(self,other):
        return self.free_coefficient == other.free_coefficient and self.i_coefficient == other.i_coefficient and self.j_coefficient == other.j_coefficient and self.k_coefficient == other.k_coefficient

    def __add__(self,other):
        sum_0 = self.free_coefficient+other.free_coefficient
        sum_1 = self.i_coefficient+other.i_coefficient
        sum_2 = self.j_coefficient+other.j_coefficient
        sum_3 = self.k_coefficient+other.k_coefficient
        return Quaternion(sum_0,sum_1,sum_2,sum_3)

    def __sub__(self,other):
        sub_0 = self.free_coefficient-other.free_coefficient
        sub_1 = self.i_coefficient-other.i_coefficient
        sub_2 = self.j_coefficient-other.j_coefficient
        sub_3 = self.k_coefficient-other.k_coefficient
        return Quaternion(sub_0,sub_1,sub_2,sub_3)

    def __mul__(self,other):
        mul_0 = self.free_coefficient*other.free_coefficient - self.i_coefficient*other.i_coefficient - self.j_coefficient*other.j_coefficient - self.k_coefficient*other.k_coefficient
        mul_1 = self.free_coefficient*other.i_coefficient + self.i_coefficient*other.free_coefficient + self.j_coefficient*other.k_coefficient - self.k_coefficient*other.j_coefficient
        mul_2 = self.free_coefficient*other.j_coefficient + self.j_coefficient*other.free_coefficient + self.k_coefficient*other.i_coefficient - self.i_coefficient*other.k_coefficient
        mul_3 = self.free_coefficient*other.k_coefficient + self.k_coefficient*other.free_coefficient + self.i_coefficient*other.j_coefficient - self.j_coefficient*other.i_coefficient
        return Quaternion(mul_0,mul_1,mul_2,mul_3)

    def __abs__(self):
        return math.sqrt(self.free_coefficient**2 + self.i_coefficient**2 + self.j_coefficient**2 + self.k_coefficient**2)

 

q1 = Quaternion(1,2,3,4)
print(q1)
q2 = Quaternion(1,2,1,2)
print(q1+q2)
print(q1*q2)
q3 = Quaternion(4,0,3,0)
print(abs(q3))
q4 = Quaternion(2)
print(q4)
