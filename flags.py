import re

# 只匹配ascii字符
p = r'''[A-Z]\w+ #匹配第一个单词
\s+\w+\s+   # 空格和第二个单词
\S+         # 匹配汉子
'''

regex = re.compile(p,re.X)

s = '''Welcome to
达内   
'''

l = regex.findall(s)
print(l)