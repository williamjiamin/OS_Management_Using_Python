# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
# 需要用到的技术
# 1.路径读取os
# 2.文件读取的写入
# 3.筛选功能实现
# 4.需要注意的问题：编码问题
# 5.shutil的综合应用

import os
import shutil

os.chdir('/Users/william/Desktop/File_to_be_org')
os.makedirs('new_dir')

for root, dirs, files in os.walk('/Users/william/Desktop/File_to_be_org', topdown=False):
    for file_name in files:
        file_name_split = file_name.split('.')
        # print(file_name_split)

        # 可以通过判断来进行筛选，特定选取操作
        try:
            # 找到所有你需要的特定类型文件
            # 通过if进行筛选
            if file_name_split[-1] == 'md':
                # 原来路径与新路径创建
                md_file_path_read = os.path.join(root, '.'.join(file_name_split))
                md_file_path_write = os.path.join(root, 'new_dir', '.'.join(file_name_split))
                # print(os.getcwd())
                # print(md_file_path)
                shutil.copy(file_name, 'new_dir/{}'.format(file_name))

                with open(md_file_path_write, 'r', encoding='utf-8') as rf:
                    contents = rf.readlines()
                contents.insert(0, '---\n' + 'title: {}\n'.format(file_name_split[0], file_name_split[1]) + '---\n')

                with open(md_file_path_write, 'w', encoding='utf-8') as wf:
                    contents = "".join(contents)
                    wf.write(contents)
        # 如果没有的情况下，打印找不到错误
        except FileNotFoundError as e:
            print(e)
