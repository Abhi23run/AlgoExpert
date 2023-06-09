def runLengthEncoding(string):
    # Write your code here.
    #code_abhinav
    n=len(string)
    prev_char=string[0]
    new_string=''
    count=1
    if len(string)==1:
        new_string=new_string+'1'+string[0]
    else:
        for i in range(1,n):
            current_char=string[i]
            if ((current_char==prev_char)):
                count+=1     
            else:
                if count<=9:
                    new_string=new_string+str(count)+prev_char
                else:
                    new_string=new_string+('9'+prev_char)*(count//9)
                    new_string=new_string+str(count%9)+prev_char
                count=1
            prev_char=current_char
        if(new_string==''):
    #         new_string=new_string+str(count)+prev_char
            if count<=9:
                new_string=new_string+str(count)+prev_char
            else:
                new_string=new_string+('9'+prev_char)*(count//9)
                new_string=new_string+str(count%9)+prev_char
        if(new_string[-1]!=current_char):
            if count<=9:
                new_string=new_string+str(count)+prev_char
            else:
                new_string=new_string+('9'+prev_char)*(count//9)
                new_string=new_string+str(count%9)+prev_char
        
    return new_string

