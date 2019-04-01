import re
import sys
port = sys.argv[1]

f = open('1.txt','r')
while True:
    data = ''
    for line in f:
        if line != '\n':
            data += line
        else:
            break    
    if not data:
        print("No data")
        break
    #获取每一段首单词
    try:
        PORT = re.match(r'^\S+',data).group()
    except Exception:
        continue
    if PORT == port:
        addr = re.search(r'(?P<addr>\d+\.\d+\.\d+\.\d+\/\d+|Unknown)',data)
        print(addr.group('addr'))
        break  