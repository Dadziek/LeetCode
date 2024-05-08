class Solution(object):
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)
        for key, element in enumerate(score):
            if element == sorted_score[0]:
                score[key] = "Gold Medal"
            elif element == sorted_score[1]:
                score[key] = "Silver Medal"
            elif element == sorted_score[2]:
                score[key] = "Bronze Medal"
            else:
                score[key] = str(sorted_score.index(element)+1)
        return score
                