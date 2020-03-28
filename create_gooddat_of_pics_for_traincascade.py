from PIL import Image
f = open(r'C:\Users\1\lib\opencv\build\x64\vc14\bin\baza\Good.dat', 'w', encoding='utf-8')

for i in range(1, 1234):
    if i!=263:
        path=r'C:\Users\1\lib\opencv\build\x64\vc14\bin\baza\Good\Good'+str(i)+'.jpg'
        im = Image.open(path)
        (width, height) = im.size
        f.write("Good\Good" +str(i)+".jpg "+ "1 0 0 "+str(width)+" "+str(height)+'\n')
print("stop")
f.close()