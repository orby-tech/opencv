from PIL import Image
f = open(r'C:\Users\1\lib\opencv\build\x64\vc14\bin\Good.dat', 'w', encoding='utf-8')

for i in range(1, 820):
    if i!=10000:
        path=r'C:\Users\1\lib\opencv\build\x64\vc14\bin\Good\Good_'+str(i)+'.jpg'
        im = Image.open(path)
        (width, height) = im.size
        f.write("Good\Good_" +str(i)+".jpg  "+ "1  0 0 "+str(width)+" "+str(height)+'\n')
print("stop")
f.close()