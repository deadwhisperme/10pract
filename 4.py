enru=open('en-ru.txt','r')
input=open('input.txt','r')
output=open('output.txt','w')
s=enru.read()
x=''
qwe={'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'}
slovar={}
s=s.replace('\t-\t',' ')
while len(s)>0:
    slovar[s[:s.index(' ')]]=s[s.index(' '):s.index('\n')]
    s=s[s.index('\n')+1:]
print(slovar)
s=input.read()
s=s.lower()
while len(s)>0:
    a=s[0]
    if a not in qwe:
        if  x in slovar:
            print(slovar[x],a, file=output, sep='',end='')
        else:
            print(x,a, file=output, sep='',end='')
        x=''    
    else:
        x+=a
    s=s[1:]
