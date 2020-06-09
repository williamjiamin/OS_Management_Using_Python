# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os

from datetime import datetime

os.chdir('/Users/william/Desktop/')


# 一般来说是对大量数据文件（一般是日志）做相应数据获取与处理
last_modification_time= os.stat('Test_renamed.txt').st_mtime
print(datetime.fromtimestamp(last_modification_time))