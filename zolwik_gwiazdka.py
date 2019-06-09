# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:17:40 2019

@author: Sebastian
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()