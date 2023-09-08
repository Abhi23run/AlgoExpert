def get_closest(arr,x):
  arr=list(sorted(set(arr)))
  l,r=0,len(arr)-1
  while(l<r):
    mid=(l+r)//2
    mid_val=abs(arr[mid]-x)
    left_val=abs(arr[mid-1]-x)
    right_val=abs(arr[mid+1]-x)
    min_val=min(mid_val,left_val,right_val)
    if min_val==mid_val:
      return arr[mid]
    elif min_val==left_val:
      r=mid-1
    else:
      l=mid+1
  mid=(l+r)//2
  return arr[mid]

def smallestDifference(arrayOne, arrayTwo):
  sorted_a,sorted_b=sorted(arrayOne),sorted(arrayTwo)

  min_diff=1e10
  for i in sorted_a:
    ## use the helper function to get the closest number in 2nd array for each element in 1st array
    closest_num=get_closest(sorted_b,i)

    ## compute the diff b/w both elements
    curr_diff=abs(closest_num-i)

    # condition to update minimum difference and corresponding elements
    if curr_diff<min_diff:
      min_diff=curr_diff
      ans=[i,closest_num]
      
  return ans
