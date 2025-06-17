members = []

N = int(input('<UNK> <UNK> <UNK>'))
 num = 1
 for _ in range(N//3):
    members.append(list(range(num,num+3)))
    num += 3

    print(members)