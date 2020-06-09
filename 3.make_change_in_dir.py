# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os

os.chdir('/Users/william/Desktop')

# 创建
# 方法一： 不太推荐，不一定能成功（如果TestDir不存在的情况下，不一定能实现）
# os.mkdir('TestDir/SubDir')

# 方法二：推荐，一次成功
# os.makedirs('TestDir/SubDir_2')
# print(os.listdir())

# 关于删除，必须慎重

# 方法一：推荐，更加保险。直接删除目标Dir
os.rmdir('TestDir/TestDir2/TestDir3')
# print(os.listdir())
# 方法二：不推荐，危险！ 把中间所有空的Dir全部删除

# os.removedirs('TestDir/TestDir2/TestDir3')
print(os.listdir())
