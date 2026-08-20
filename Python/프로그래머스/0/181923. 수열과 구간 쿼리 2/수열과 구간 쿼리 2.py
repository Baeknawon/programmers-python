def solution(arr, queries):
    answer = []
    for query in queries:
        candidate = []
        for i in range(query[0], query[1]+1):
            if arr[i] > query[2]:
                candidate.append(arr[i])
        if not candidate:
            answer.append(-1)
        else:
            answer.append(min(candidate))
        
    return answer