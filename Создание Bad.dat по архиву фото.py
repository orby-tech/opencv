f = open(r'C:\Users\1\lib\opencv\build\x64\vc14\bin\Bad.dat', 'w', encoding='utf-8')
for i in range(1, 624):
    f.write("Bad\Bad"+str(i)+".jpg"+'\n')
print("stop")
f.close()