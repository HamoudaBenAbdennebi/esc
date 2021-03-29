N= int(input("donner la taille de la matrice"))
size=(N,N)
tab=[]
for i in range(size[0]):
    tab.append([])
    for j in range(size[1]):
        tab[-1].append(0)

x=0
y=0
lh=0 
lb=0
hd=0 
hl=0 
sens='d'
for k in range(size[0]*size[1]):
    if(size[0]-x-hd>1 and sens=='d') :
        tab[x][y]=k
        x+=1
    elif(sens=='b' and y<size[1]-lb) :
        tab[x][y]=k
        y+=1
    elif(sens=='g' and x>=hl):
        tab[x][y]=k
        x-=1
    elif(sens=='h' and y>=lh):
        tab[x][y]=k
        y-=1
    else :
        if(sens=='d'):
            sens='b'
            lh+=1
            tab[x][y]=k
            y+=1
        elif(sens=='b') :
            sens='g'
            hd+=1
            tab[x-1][y-1]=k
            y=size[1]-lb-1
            x=size[0]-hd-2
        elif(sens=='g'):
            sens='h'
            lb+=1
            y=size[1]-lb-1
            x=hl
            tab[x][y]=k
            y-=1
        elif(sens=='h'):
            sens='d'
            hl+=1
            tab[x+1][lh]=k
            x+=2
            y=lh
    
tabpr=''
for i in range(size[1]):
    for x in range(size[0]):
        num=str(tab[x][i])
        if(len(num)<len(str(size[0]*size[1]-1))):
            num=((len(str(size[0]*size[1]-1))-len(num))*' ')+num
        tabpr+=num+' '
    tabpr+='\n'
print (tabpr)
