## Optimized Solution O(n^2)


def longest_index(string,i):
    n=len(string)
    if ((i<0) or (i>=n)):
        return ''
    pivot=string[i]
    flag=1
    final_substring=string[i]
    l,r=i-1,i+1
    if (l>=0):
        if ((string[l]==pivot) & (flag==1)):
            final_substring=max(string[l:i+1],final_substring,key=len)
            l-=1
            flag=0
        if((l>=0) & (r<n)):  
            if string[l]!=string[r]:
                pass
            while(string[l]==string[r]):
                final_substring=max(string[l:r+1],final_substring,key=len)
                l-=1
                r+=1

                if ((l<0) or (r>=n)):
                    break

    l,r=i-1,i+1                
    if((l>=0) & (r<n)):  
            if string[l]!=string[r]:
                pass
            while(string[l]==string[r]):
                final_substring=max(string[l:r+1],final_substring,key=len)
                l-=1
                r+=1

                if ((l<0) or (r>=n)):
                    break

    
    
    return final_substring

def longestPalindromicSubstring(string):
    n=len(string)
    ans_string=''
    for i in range(n):
        ans_string=max(ans_string,longest_index(string,i),key=len)
    return ans_string


## Basic Solution O(n^3)

def isPalindrome(string):
    #solution Abhinav basic
    l,r=0,len(string)-1
    while(l<=r):
        if string[l]==string[r]:
            l+=1
            r-=1

        else:
            return False
    return True

def longestPalindromicSubstring(string):
    # Write your code here.
    m,n=len(string),len(string)

    if n==1:
        return string
    while(n>0):
        for k in range(m-n+1):
            l,r=k,k+n
            if isPalindrome(string[l:r]):
                return string[l:r]
        n-=1
    

