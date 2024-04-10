# O(n) time complexity , O(k) space complexity.. where k is number of teams.

def tournamentWinner(competitions, results):
    final_result = {}
    for i in range(0, len(results)):
        if(results[i] == 0):
            # away team won
            try:
                final_result[competitions[i][1]] += 3
            except KeyError:
                final_result[competitions[i][1]] = 3
        else:
            try:
                final_result[competitions[i][0]] += 3
            except KeyError:
                final_result[competitions[i][0]] = 3
    return max(final_result, key=final_result.get)

