'''if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result =[[i,j,k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if i+j+k != n]
    print(result)'''



'''Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
5
2 3 6 6 5
O/P 5
///////////////////
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    MAX = max(arr)
    while MAX in arr:
        arr.remove(MAX)
    print(max(arr))

'''
'''
from a list of name and score find the 1st and 2nd lowest and find the respective name alphabatically

def task(names, scores):
    set_scores = set(scores)
    lowest = min(set_scores)
    set_scores.remove(lowest)
    records = {names[i]: scores[i] for i in range(len(names))}
    ans = [n for n,s in records.items() if s == min(set_scores)]
    ans.sort()
    return ans


if __name__ == '__main__':
    names = []
    scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    names.append(name)
    scores.append(score)
result = task(names, scores)
print(*result, sep="\n")

https://youtu.be/Cgl0c4mupAg?si=e1QFg40ssA4Ap_LY
"
'''
'''
find the average score of an array up to 2 decimal no.. 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
total_sum = sum(scores)
average = total_sum / len(scores)

# Print the average rounded to 2 decimal places
print(f"{average:.2f}")
'''




