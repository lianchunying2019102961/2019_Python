# encoding=utf-8

import random
import string



 #20000�������
a=[random.randint(8000,20000) for _ in range(20000)]
print (a)

#20000���������
b=[random.uniform(8000.0000,20000.0000) for _ in range(20000)]
print (b)

#����ַ���
#new_words = ''.join(random.sample(string.ascii_letters + string.digits, 6))
#print new_words
#����ַ�
#n={''.join(random.choice(new_words)) for I in range(10)}
#print(len(n))

#60000����ַ���
s=string.ascii_letters+string.digits
print(s)
	

n={''.join(random.choices(s,k=8)) for I in range(60000)}

print(n)
	


with open('randomdata.txt') as f:
   
 for i in n:
      
 f.write(i+'\n')