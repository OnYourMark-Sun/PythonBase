""""
\d   :表示数字
\d{3}  : 三个数字
\w   ：表示数字或者字母
\d\w\d  :0q2   454

A|B  : A或者B
(P|p)ython  : Python  或  python
^\d  : ^表示开头， 以数字开头
$\d  : $表示结尾   以数字结尾
\s   : 匹配一个空格
*   : 任意个字符
?   :0或者1个
+   ： 至少1个字符

匹配 '010-123456' 的正则： \d{3}\-\d{5}    \- :是将- 转义
[0-9a-zA-Z\_] :可以匹配一个数字一个字母或者下划线
[0-9a-zA-z\_]+ :可以匹配至少有一个数字字母下划线组成的字符串
[a-zA-Z\_][0-9a-zA-Z\_]*  :这个是由字母数字下划线开头  后边是数字字母下划线组成的字符串
[a-zA-Z\_][0-9a-zA-Z\_]{0,19} :限制了变量的长度 前边是一个  后边不超过19个
"""

'''print("正则表达式")

import re
string = '0106456'
if re.match(r'^\d{3}',string):
    print('OK匹配')
else:
    print('没有匹配--')

string2 = '12 3  23 2 232 2 '
print(re.split(r'\s+',string2))


#分组 ()

timet = '20:58:18'
re = re.match(r'^(0[0-9]|1[0-9]|2[0-3])\:([0-5][0-9])\:([0-5][0-9])$',timet)
if re:
    print('符合时间算法')
    print(re.group(),'-',re.group(1),'-',re.group(2),'-',re.group(3))
    print(re.groups())
else:
    print('看看哪儿错了吧')



#防止重复编译
import re
re_telephone = re.compile(r'^\d{3-4}-\d{3,8}$')
renum = re_telephone.match('010-12358456')
print(renum.groups())
print(re_telephone.match('0375-158877466').groups())'''

#判断网址
import re
url = 'www.baiddsf233u.com'
url2 = 'http://www.baiddsf233u.com'

if re.match(r'^(http://www|www).(\w+).(com)',url):
    print('是一个网址')

else:print('不是一个网址')


email = ['1175337619@qq.com','15120006188@139.com7','15120006188@gmail.com']

def determineMailbox(r):
    if re.match('^(\d+)(@qq.com)$',r):
        print(r,"是一个qq邮箱")
    else:
        if re.match('^(\d{11})(@139.com)$',r):
            print(r,"这是一个139的邮箱")
        else:
            if re.match('^(\d{11})(@gmail.com )$',r):
                print(r,"这是一个gooleEmail邮箱")
            else:
                print(r,"这不是一个邮箱啊")

for t in email:
    determineMailbox(t)