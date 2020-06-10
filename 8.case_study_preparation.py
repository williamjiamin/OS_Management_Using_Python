# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os

os.chdir('/Users/william/Desktop/TestDir')

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('现在的路径为：', dirpath)
    print('现在的Dir(目前在的文件夹下)：', dirnames)
    print('现在的文件是：', filenames)
    print()
