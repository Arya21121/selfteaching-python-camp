text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text = text.replace('better','worse')
print('将字符串样本 text 里的 better 全部替换成 worse==>',text)

words=text.split()
filtered=[]
for word in words:
    if word.find('ea')<0:
        filtered.append(word)
print('单词中包含 ea 的单词剔除==>',filtered)
print()


swapcased = [i.swapcase() for i in filtered]
print('字母大小写翻转==》',swapcased)
print()

print('所有单词按 a…z 升序排列==>',sorted(swapcased))