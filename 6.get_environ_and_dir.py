# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import os

print(type(os.environ.get('HOME')))

# 路径问题：不推荐的写法——字符串连接,因为非常容易犯掉'/'等错误

# our_path = os.environ.get('HOME') + 'Desktop/Test'

# 推荐：通过os系统的专门的路径模块解决
our_path = os.path.join(os.environ.get('HOME'), 'Desktop', 'Test.txt')

print(our_path)
