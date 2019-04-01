import re

try:
    f = open('1.txt','rb')
    data = f.read()
except:
    print('Error')
finally:
    f.close()
# print(data)
# BigWrite = r'\b[A-Z]\S+\b'
# BW = re.findall(BigWrite,data.decode())
# MP = r'-?\d+[./]?\d*%?'
# M = re.findall(MP,data.decode())
# print(BW)
# print(M)
DP = r'[1-2]\d{3}[.]\d{1,2}[.]\d{1,2}'
D = re.findall(DP,data.decode())
for i in D:
    l = re.sub(r'[.]','-',i)
    print(l)

regex = re.compile(DP)
for i in regex.finditer(data.decode()):
    s = i.group()
    print('s',s)
    l = re.sub(r'\.','-',s)
    print(l)