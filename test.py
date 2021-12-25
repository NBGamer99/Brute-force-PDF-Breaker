import os
import time
# import datetime
t1 = time.time()
time.sleep(5)
t2 = time.time()
# # t = time.ctime(t2-t1)
# t = t2 - t1
# # print('time is ', time.strftime(" %H:%M:%S", t))
# # print('time is ', time.ctime(t))
# # print(time.gmtime(t))
# print(time.strftime("%H:%M:%S", time.gmtime(t)))
# print(str(datetime.timedelta(seconds=t2-t1)))
# # print('dsadsa\n', 'dsa')
mypath = (os.path.realpath(os.path.dirname(__file__)))
path = os.path.join(mypath, "PUT YOUR PDF HERE !!")
# print(mypath)
print(__file__)
print(os.path.dirname(__file__))
print(os.path.join(mypath, "PUT YOUR PDF HERE !!"))
# print(path)
# print(path)
# for root, dirs, files in os.w alk(path):
#     pass
# print(root)
# print(dirs)
# # print(files)
# for root, dirs, files in os.walk(path):
#     for name in files:
#         print('name :', os.path.join(root, name))
#     for name in dirs:
#         print('dires :', os.path.join(root, name))
#     print('root', root)
# # l1 = []
# if not l1:
#     print('empty')
# else:
#     print('not empty list')
