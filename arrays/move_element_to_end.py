def moveElementToEnd(array, toMove):
    # Write your code here.
    # Not in place (O(N) memory solution)
    final_list=[]
    for item in array:
      if item==toMove:
        pass
      else:
        final_list.append(item)
    n=len(array)
    m=len(final_list)
    final_list+=[toMove]*(n-m)
    return final_list


def moveElementToEnd(array, toMove):
    # Write your code here.
    ## O(1) memory -> in-memory solution
    l,r=0,len(array)-1
    while(l<=r):
      if((array[l]==toMove) & (array[r]!=toMove)):
        array[l],array[r]=array[r],array[l]
        l+=1
        r-=1
      elif((array[l]!=toMove) & (array[r]==toMove)):
        l+=1
      elif((array[l]==toMove) & (array[r]==toMove)):
        r-=1
      else:
        l+=1

    return array
