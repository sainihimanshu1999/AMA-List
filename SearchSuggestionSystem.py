'''
usin two pointer solution for this question, this solution is pretty intutive
'''

def suggestions(products,word):
    products.sort()
    start,end = 0,len(products)-1
    result = []

    for i,c in enumerate(word):
        while start<=end and (len(products[start])<=i or products[start][i]!=c):
            start +=1

        while start<=end and (len(products[end])<=i or products[end][i]!=c):
            end-=1
        
        result.append(products[start:min(start+3,end+1)])

    return result

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
print(suggestions(products,searchWord))