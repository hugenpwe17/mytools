#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 01:18:36 2022

@author: oyxl
"""

# 定义源文件格式与目标文件格式
src_format = '.svg'
des_format = '.pdf'

# 定义源文件夹路径和目标文件夹路径
src_path = './source/'
des_path = './destination/'

# 获取源文件夹的所有文件名
import os
src_filenamelist = os.listdir(src_path)

# 创建文件名列表
filenamelist = list()

# 提取源文件的文件名列表S
for filename in src_filenamelist:
    if(filename.find(src_format) != -1):
        filenamelist.append(filename.replace(src_format, ''))
        
# 图像格式转换
import cairosvg
for filename in filenamelist:
	res = cairosvg.svg2pdf(url=(src_path + filename + src_format),write_to=des_path + filename + des_format)
    