def sortedSquaredArray(array):
    #coding_abhinav
    n=len(array)
    new_array=[0]*n
    i,j,k=0,n-1,n-1
    while(i<=j):
        if abs(array[i])>abs(array[j]):
            new_array[k]=array[i]**2
            i+=1
        else:
            new_array[k]=array[j]**2
            j-=1
        k-=1

    return new_array
    

