def tournamentWinner(competitions, results):
    # Write your code here.
    # coding_abhinav
    score_dict={}
    for i, match in enumerate(competitions):
        winner=match[abs(1-results[i])]
        loser=match[abs(1-abs(1-results[i]))]
        score_dict[winner]=score_dict.get(winner,0)+3
        score_dict[loser]=score_dict.get(loser,0)
    max_score=max(score_dict.values())
    
    return [i for i,j in score_dict.items() if j==max_score][0]

