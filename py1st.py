Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> >>> #!/usr/bin/env python3
... # -*- coding: utf-8 -*- //ситуационные строки, всё и без них работает
...
>>> import math
>>> import numpy
>>> import matplotlib.pyplot as mpp //подключаем библиотеки
>>>
>>>
>>> if __name__=='__main__': //мэйн - обязательный метод для многих языков
...     arguments = numpy.r_[0:200:0.1] //задаём аргументы нашей функции
...     mpp.plot( //тело функции
...         arguments,
...         [math.sin(a) * math.sin(a/20.0) for a in arguments] //создаём функцию
...     )
...     mpp.show() //запускаем визуализированную функцию при помощи библиотеки в отдельном окне
...
[<matplotlib.lines.Line2D object at 0x016A67F0>] //отчёт о запуске окна
