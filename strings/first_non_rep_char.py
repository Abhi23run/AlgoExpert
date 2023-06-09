def firstNonRepeatingCharacter(string):
    # Write your code here.
    #abhinav_code
    freq_dict={}
    index_dict={}
    for i,s in enumerate(string[::-1]):
        freq_dict[s]=freq_dict.get(s,0)+1
        index_dict[s]=len(string)-i-1
    fn_list=({k:v for k,v in index_dict.items() if k in {k:v for k,v in freq_dict.items() if v==1}.keys()}.values())
    
    if len(fn_list)==0:
        return -1
    else:
        return min(fn_list)

