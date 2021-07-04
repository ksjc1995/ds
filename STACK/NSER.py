'Next Smaller Element Right'
from typing import List

def nextsmallertoright(arr:List[int])->List[int]:

    l = len(arr)
    output, stack = [-1] * l , []

    for index in range(l):

        while stack and arr[index] < arr[stack[-1]]:
            output[stack[-1]] = arr[index]
            stack.pop()

        stack.append(index)
    
    return output
