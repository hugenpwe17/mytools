#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 19:49:11 2022

@author: oyxl
"""

import numpy as np

def yfindx(v, xn, vn):
    [vn_unique, idx] = np.unique(vn, return_index=True)
    xn_unique = xn[idx]
    x_iwant = np.interp(v, vn_unique, xn_unique)
    return x_iwant