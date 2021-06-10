def para(paragraph,banned):
    for c in "?!,;.'":
        paragraph = paragraph.replace(c,' ')
    
    banned = set(banned)
    dic = {}
    #print(paragraph)
    for word in paragraph.lower().split():
        if word in banned:
            continue
        dic[word] = dic.get(word,0)+1

    return max(dic, key=dic.get)


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(para(paragraph,banned))