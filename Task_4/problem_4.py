if _name_ == '_main_':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))
    scores.sort()
    print(scores[-2])
