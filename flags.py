import re


#re.I   忽略大小写
# s = 'Hello world'
# pattern = r'hello'
# regex = re.compile(pattern,flags=re.I)

#re.A   使用ascii字符
# s = 'Hello 你好'
# pattern = r'\w+'
# regex = re.compile(pattern,flags=re.A)

#re.S  使 . 匹配\n
# s = '''Hello world 
# nihao China'''
# pattern = r'.+'
# regex = re.compile(pattern,flags=re.S)

#re.M匹配每行开头结尾
# s = '''Hello world
# nihao China
# '''
# pattern = r'^Hello'
# regex = re.compile(pattern,flags=re.M)

#re.X给正则表达式加注释
s = '''abcdefghi'''
pattern = r'''(ab)    #第一行分组
\w+                   #任意字符串
(?P<dog>ef)           #dog组
'''
regex = re.compile(pattern,flags=re.X)
l = regex.findall(s)
print(l)