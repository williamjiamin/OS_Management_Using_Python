# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import shutil
import os

os.chdir('/Users/william/PycharmProjects/OS_Management_Using_Python')
os.makedirs('new_folder')
shutil.copy('test.txt', 'new_folder/test_copy.txt')
