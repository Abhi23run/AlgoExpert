def groupAnagrams(words):
    # Write your code here.
    simplified_words=[''.join(sorted(i)) for i in words]
    final_df={}
    for i,j in enumerate(simplified_words):
      if j in final_df:
        final_df[j].append(i)
      else:
        final_df[j]=[i]
    final_list=list(final_df.values())

    result = [[words[i] for i in sublist] for sublist in final_list]

    return result
