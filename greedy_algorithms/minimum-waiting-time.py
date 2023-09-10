def minimumWaitingTime(queries):  
    queries.sort()
    if len(queries)<2:
        return 0
    else:
        cur_sum=0
        total_sum=0
        for i in queries[:-1]:
          cur_sum+=i
          total_sum+=cur_sum
        return total_sum
