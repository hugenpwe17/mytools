# 定义源文件格式与目标文件格式
src_format = '.eps'
des_format = '.png'

# 定义源文件夹路径和目标文件夹路径
src_path = './source/'
des_path = './destination/'

# 获取源文件夹的所有文件名
import os
src_filenamelist = os.listdir(src_path)

# 创建文件名列表
filenamelist = list()

# 提取源文件的文件名列表
for filename in src_filenamelist:
    if(filename.find(src_format) != -1):
        filenamelist.append(filename.replace(src_format, ''))
        
# 图像格式转换
from PIL import Image
for filename in filenamelist:
	img = Image.open(src_path + filename + src_format)
	img.save(des_path + filename + des_format)
    
# 输出转换信息
print('***')
print(src_format, 'translate to', des_format, 'is successed')
