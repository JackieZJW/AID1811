import re

pattern = r"(\w+):(\d+)"
s = "张:2018,李:2019"

# #直接用re调用
# l=re.findall(pattern,s)
# print(l)

#compile 对象调用
regex = re.compile(pattern,)
l = regex.findall(s,pos=0,endpos=8)
print(l)

#split用法
l = re.split(r'\s+','Hello   world   nihao  Kitty')
print(l)

#sub用法
s = re.sub(r'\s+','##','hello world    nihao Kitty',2)
print(s)

#subn用法
s = re.subn(r'\s+','##','hello world    nihao Kitty',2)
print(s)
