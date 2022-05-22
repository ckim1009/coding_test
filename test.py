
from re import I


def solution(id_list, report, k):
    ab = [set([]) for _ in id_list]
    abuse = [0 for _ in id_list]
    
    for x,y in list(map(lambda x : x.split(),report)):
        ab[id_list.index(x)].add(y)
   
    for s in ab:
        if s:
            temp = list(map(lambda x: id_list.index(x) ,s))
            for i in temp:
                abuse[i]+=1

    answer = [0 for _ in id_list]

    for index,id in enumerate(id_list):
        if abuse[index] >= k:
            for i,j in list(map(lambda x : x.split(),report)):
                if j==id:
                    answer[id_list.index(i)]+=1
    
    return answer

def solution2(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


m = [1, 15, 4, 6, 7]

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

arr = [[i+j*5 for i in range(5)] for j in range(5)]
print(arr)
print(*arr)
print(list(zip(*arr)))
#print(solution(id_list, report, k))

