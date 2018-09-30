#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp
#подключаем библиотеки

if __name__=='__main__': #мэйн
    arguments = numpy.r_[0:200:0.1] #задаём аргументы синусоиды
    mpp.plot( #тело синусоиды
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    mpp.show() #вывод синусоиды в отдельном окне
