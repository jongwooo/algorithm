import collections

def solution(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result.keys())[0]
