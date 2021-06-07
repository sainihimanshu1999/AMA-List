'''
I will name this frequency sort
'''

def frequencySort(s) -> str:
    dic = {}
    
    for i in s:
        dic[i] = dic.get(i,0)+1
        
    freq =sorted(dic.items(),key=lambda x:x[1],reverse = True)
    return ''.join(x[0]*x[1] for x in freq)