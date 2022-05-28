#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:02:06 2022

@author: oyxl
"""

import numpy as np
import pandas as pd
import copy

class gmoverid():
    
    # public variable
    
    # private variable
    
    def __init__(self, path, mostype):
        self.path = path
        self.mostype = mostype
        self.name = str.upper(self.mostype)
        
    # def getData(self):
        
        
    def var_split(data):
        x_array = np.zeros([data.shape[0], int(data.shape[1]/2)])
        y_array = copy.copy(x_array)
        
if __name__ == '__main__':
    a = gmoverid('data/', 'nmos')
    print(a.name)