#Способ короче в голову не пришёл(

def str_base(number, base):
        i = 1
        sum = ""
        while number > base**i:
            i += 1
        i -= 1
        while i >= 0:
            a = int(number / base**i)
            number -= a*(base**i)
            if a < 10:
                    sum += str(a)
            else:
                    sum += chr(65 + a - 10)
            i -= 1
        return sum
