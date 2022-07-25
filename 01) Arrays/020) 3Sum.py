"""
https://leetcode.com/problems/3sum
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    """"""

    # 0) (TLE) Brute-force (Nested Loops & HashMap): TC = O(n^3); SC = O(n)

    # Core Logic: TC = O(n^3); SC = O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    yield [nums[i], nums[j], nums[k]]
    """
    # But as the solution set must not contain duplicate triplets, see Example 1:
    #     Input: nums = [-1, 0, 1, 2, -1, -4]
    #     Output: [[-1, 0, 1], [-1, -1, 2]]
    #     Explanation:
    #     nums[0] + nums[1] + nums[2] = (-1) + 0 +   1  = 0.
    #     nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    #     nums[1] + nums[2] + nums[4] =   0  + 1 + (-1) = 0.
    #     THE DISTINCT TRIPLETS ARE [-1, 0, 1] AND [-1, -1, 2].
    #     Notice that the order of the output and the order of the triplets does not matter.
    # We will keep track of the triplets already added to the answer set and will not consider any triplet again: TC = O(n^3 * 3*log(3)); SC = O(n)
    """
    # from collections import Counter

    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    # For checking triplet's presence in O(1) time IRRESPECTIVE OF THE ORDER OF THE NUMS IN TRIPLETS:
                    '''
                    triplet_counter = Counter(triplet)  # tracking triplet's nums and their counts
                    # can't use set because it will destroy the triplet itself, consider triplet = [-1, 2, -1]
                    # set(triplet) = {-1, 2} ❌ whereas Counter(triplet) = {-1: 2, 2: 1} ✔
                    if triplet_counter not in triplet_set:  # raise TypeError: unhashable type: Counter
                        # because MUTABLE DATATYPES ARE UNHASHABLE
                        yield triplet
                        triplet_set.add(triplet_counter)
                    '''
                    # It's the problem, instead, we can sort the triplet (time will be O(1) only because len(triplet) is 3),
                    # and since the triplets will be ordered now, we can use tuples (i.e. ordered and immutable):
                    sorted_triplet_tuple = tuple(sorted(triplet))
                    if sorted_triplet_tuple not in triplet_set:
                        yield triplet
                        triplet_set.add(sorted_triplet_tuple)
    """
    # Turns out that we can also just sort the input array and apply the above logic (without needing to sort the triplets): TC = O(n*log(n) + n^3); SC = O(n)
    # https://leetcode.com/problems/3sum/discuss/1363302#:~:text=Brute%20Force%20Solution
    nums = sorted(nums)  # (not modifying the input array but making a new variable (local))
    n = len(nums)
    triplet_set = set()  # for checking triplet's presence in O(1) time
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet_tuple = tuple(triplet)
                    if triplet_tuple not in triplet_set:
                        yield triplet
                        triplet_set.add(triplet_tuple)
    # Why does this work?
    # Because if the input array is sorted, triplets will not form like [-1, 0, 1] & [0, 1, -1],
    # but like [-1, 0, 1] & [-1, 0, 1], i.e. by default sorted (i.e. in order)
