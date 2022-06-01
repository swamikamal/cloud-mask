from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

#"C:\Users\kamal\Desktop\whatsapp\maskpng"
adr=r'D:\Program Files\python practice\whatsapp python project\diction.txt'
li = open(adr,"r")
data = li.read()
li.close()
l=''
c=0
for i in data:
    
    q=len(l)
    if q%3 ==0:
        l=l+" "
    else:
        l=l+i
    
    if q%4 ==0:
        l=l+" "
    else:
        l=l+i    

    if q%5 ==0:
        l=l+" "
    else:
        l=l+i
    if q%10 ==0:
        l=l+" "
    else:
        l=l+i
print(l)
our_mask = np.array(Image.open(r"D:\Program Files\python practice\whatsapp python project\maskpng\pp.png"))

cloud = WordCloud(background_color="white", mask = our_mask).generate(l)

plt.imshow(cloud)
plt.axis('off')
plt.show()
