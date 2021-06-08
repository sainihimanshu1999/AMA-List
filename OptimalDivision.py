'''
This is a basic mathematics question, x1/x2/x3/x4...xn, where ever we put the paranthesis it does not matter because x1 
will always be in numerator and x2 in denominator, so to maximize result, we have to maximize the numerator as 
x1*y/x2, hence, x1/(x2/x3/x4/x5..xn) == x1*x2*x3*x4*x5..xn/x2
'''

def optimalDivision(nums):
    nums = list(map(str,nums))
    if len(nums)<=2:
        return '/'.join(nums)
    return '{}/({})'.format(nums[0],'/'.join(nums[1:]))


nums = [1000,100,10,2]
print(optimalDivision(nums))