# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os

# print(type(os.environ.get('HOME')))

some_random_path = '/lexueoude.com/LoveShareFintech/williamjiamin/lexueoude.txt'

some_certain_path = '/Users/william/Desktop/DontKnowDirOrFile_dir'

# 做各类处理
# print(os.path.basename(some_random_path))
# print(os.path.dirname(some_random_path))
# print(os.path.split(some_random_path))
print(os.path.splitext(some_random_path))


# 做各类判断
# print(os.path.exists(some_random_path))
# print(os.path.isdir(some_certain_path))
# print(os.path.isfile(some_certain_path))
