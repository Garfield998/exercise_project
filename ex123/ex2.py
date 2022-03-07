from os.path import exists

txt = open('ex2_sample.txt','a+',encoding="utf-8")
# line1 = input("在此文件中追加内容：")
# txt.write(line1)
txt.seek(0,0)
print(txt.read())
txt.close()

print(exists('ex2_sample.txt'))