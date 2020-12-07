# Spiral Matrix II

h=n-1
        l=0
        a=[[0 for i in range(n)] for j in range(n)]
        #middle number
        box=int((n+1)/2)
        #starting with 1
        c=1
        
        for i in range(box):
        
            for j in range(l,h+1):
                a[i][j]=c
                c+=1
            for j in range(l+1,h+1):
                a[j][h]=c
                c+=1
            for j in range(h-1,l-1,-1):
                a[h][j]=c
                c+=1
            for j in range(h-1,l,-1):
                a[j][l]=c
                c+=1
            l+=1
            h-=1
        return a
