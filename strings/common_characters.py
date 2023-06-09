def commonCharacters(strings):
    # Write your code here.
    #abhinav_code
    set_interaction=set(strings[0])
    for i in range(1,len(strings)):
        set_interaction=set_interaction.intersection(set(strings[i]))
    set_interaction=list(set_interaction)
    return set_interaction
    
