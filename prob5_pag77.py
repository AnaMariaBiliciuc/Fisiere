with open('c:/Users/Анна/Desktop/sir.txt', 'w') as f:
    f.write(str(input('Introduceti sirul de caractere: ')))
with open('c:/Users/Анна/Desktop/sir.txt', 'r') as f:   
    a=f.read()
with open('c:/Users/Анна/Desktop/vocale.txt', 'w') as f: 
    for i in range(0,len(a)) :
        if a[i] in ('a','A','e','E','o','O','u','U','i','I') :
            f.write(a[i])
