f= open('c:/Users/Анна/Desktop/Lista_clasei_11C.txt', 'r')
l=list(f)
f.close()
n=0
m=0
f2= open('c:/Users/Анна/Desktop/Franceza_11C.txt','w')
e= open('c:/Users/Анна/Desktop/Engleza_11C.txt','w')
for linie in l :
    campuri= linie.split()
    nota= int(campuri[2])
    n+=1
    m+=n 
    if campuri[3]=='franceza' :
        f2.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        f2.write('\n')
    if campuri[3]=='engleza' :
        e.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        e.write('\n')
print('Media celor', n, 'elevi este', m/float(n))
f2.close()
e.close()
