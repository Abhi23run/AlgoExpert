def isValidSubsequence(array, sequence):
    # Write your code here.
    # coding_abhinav
    n,m=len(array),len(sequence)
    i,j=0,0
    while(i<n and j<m):
        if sequence[j]!=array[i]:
            i+=1
        else:
            i+=1
            j+=1  
    if i<=n and j==m:
        return True
    else:
        return False
    

