import itertools as its
# 迭代器

words = "1234567890"
r = its.product(words,repeat=5)

#for i in r:
#    print(i)

# 保存在文件中生成密码本
dic = open("pass.txt","a")
for i in r:
    #123456
    dic.write("".join(i))
    # 换行
    dic.write("".join("\n"))
dic.close()