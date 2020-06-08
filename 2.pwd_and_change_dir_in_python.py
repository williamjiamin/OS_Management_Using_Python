# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os

print('这个是第一次的默认dir' + os.getcwd())

os.chdir('/Users/william/Desktop/')

print('这个是第二次的改变之后的dir' + os.getcwd())
