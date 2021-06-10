def knight(n):
    steps = {0:[4,6],1:[6,8],2:[7,9],3:[4,8],4:[0,3,9],5:[],6:[0,1,7],7:[6,2],8:[1,3],9:[4,2]}

    result = [1]*10

    for i in range(n-1):
        temp = [0]*10
        for j in range(10):
            for k in steps[j]:
                temp[j]+= result[k]

        result = temp
    return sum(result)%(10**9+7)


print(knight(3131))