"""
https://leetcode.com/problems/maximum-subarray
"""


from typing import List


def maxSubArray(nums: List[int]) -> int:

    # 0) Brute-force: Calculating sum of all the possible sub-arrays. TC = O(n^2); SC = O(1)

    """
    largest_sum = float('-inf')  # because nums consists of integers
    for i in range(len(nums)):
        current_sum = 0  # restart the sub-array formation from next element
        for j in range(i, len(nums)):
            current_sum += nums[j]  # increase the size of current sub-array by one element
            if current_sum > largest_sum:
                largest_sum = current_sum
    return largest_sum
    """

    # 1) https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane%27s_algorithm: TC = O(n); SC = O(1)

    # The thought follows a simple rule:
    # If the sum of a sub-array is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
    # If the sum is negative, it has no use to the next element, so we break.
    # It is a game of sum, not the elements.

    # 1.0) THIS VERSION OF THE ALGORITHM WILL RETURN 0 IF THE INPUT CONTAINS ALL NEGATIVE ELEMENTS (WRONG ANSWER):

    """
    current_sum = largest_sum = 0
    for num in nums:
        if current_sum+num > 0:
            current_sum += num
            if current_sum > largest_sum:
                largest_sum = current_sum
        else:
            current_sum = 0  # reset, because we didn't consider num (because it was making the sum go negative), so the array is no more contiguous
    return largest_sum
    """
    # (Same Algo:)
    """
    current_sum = largest_sum = 0
    for num in nums:
        current_sum = max(current_sum+num, 0)
        largest_sum = max(largest_sum, current_sum)
    return largest_sum
    """

    # 1.1) An extension to "1.0)", handling "the input contains all negative elements" case explicitly (ACCEPTED):

    largest_element = max(nums)
    if largest_element < 0:
        return largest_element  # e.g. nums = [-1, -4, -3]; max_subarray = [-1] => ans = -1 = largest_element
    # And then same code as "1.0)".

    # 1.2) Correct but modifies the array (which can be avoided):

    """
    for i in range(len(nums)-1):
        if nums[i] > 0:
            nums[i+1] += nums[i]
    return max(nums)
    """

    # 1.3) Perfect:

    current_sum, largest_sum = 0, float('-inf')  # so that any (negative) integer will be greater
    for num in nums:
        current_sum += num
        if current_sum > largest_sum:
            largest_sum = current_sum
        if current_sum < 0:
            current_sum = 0  # reset, we don't want to take negative sum ahead!
    return largest_sum
    # (Same Algo:)
    """
    current_sum, largest_sum = 0, float('-inf')  # so that any (negative) integer will be greater
    for num in nums:
        current_sum += num
        largest_sum = max(largest_sum, current_sum)
        current_sum = max(current_sum, 0)
    return largest_sum
    """
