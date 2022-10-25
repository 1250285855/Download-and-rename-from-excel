# 作者: Savo_Shen

import os

import wget
import pandas

# 需要读取的Excel文件名
xlsx_name = 'test.xlsx'

# 保存图片的文件夹名
imgs_dir = 'test_imgs/'

# 读取Excel文件默认sheet 1的数据
# usecols: 从0开始，读取第1列到第3列的数据
names   = pandas.read_excel(xlsx_name, usecols=[1])
IDs     = pandas.read_excel(xlsx_name, usecols=[2])
urls    = pandas.read_excel(xlsx_name, usecols=[3])

file_name='test'

for _ in range(len(names)):

    # 出现特殊情况，需要手动中断
    # if names.values[_][0] == 'xxx':
    #     continue
    
    # 从Excel中读取的其他信息组成图片的文件名
    name = file_name + names.values[_][0] + '_' + str(IDs.values[_][0])

    # 从图片链接中提取文件类型作为后缀
    img_type = urls.values[_][0].split("type=")[1]

    # 判断文件是否存在
    if os.path.exists(imgs_dir + name + "." + img_type):
        continue

    # 下载图片并保存到目录
    wget.download(urls.values[_][0], imgs_dir + name + "." + img_type)

print('success')