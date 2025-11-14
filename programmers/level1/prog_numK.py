arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(arr, commands):
    temp = []
    answer = []
    for i, j, k in commands:
        temp = arr[i - 1:j]
        temp.sort()
        answer.append(temp[k - 1])
    # print(answer)
    return answer

solution(arr,commands)