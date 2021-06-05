'''
Basic class of shuffling an array
'''
import random
class shuffle:

    def __init__(self,nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        return sorted(self.nums,keys=lambda x:random.random())