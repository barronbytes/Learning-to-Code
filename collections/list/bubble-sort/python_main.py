def top_scores(scores): # top_scores(scores, n)
    for i in range(0, len(scores)):
        for j in range(0, len(scores)-1-i):
            if scores[j] < scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
        
    return scores # return scores[:n] this would list the top "n" scores
