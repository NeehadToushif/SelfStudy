''' Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



Problem Constraints
1 <= |A| <= 100000'''


class Solution:
    # @param A : tuple of integers
    # @return an integer

    def trap(self, A):
        _max = A[0]
        pfm = [_max]
        for i in range(1,len(A)):
            if _max<A[i]:
                _max = A[i]
            pfm.append(_max)
        _max = A[-1]
        sfm = [_max]
        for i in range(len(A)-2,-1,-1):
            if _max < A[i]:
                _max = A[i]
            sfm.append(_max)
        sfm = list(reversed(sfm))
        # print(pfm)
        # print(sfm)
        ans = 0
        for i in range(1,len(A)-1):
            support = min(pfm[i],sfm[i])
            ans = ans+(support-A[i])
        return ans
A = [0, 1, 0, 2]
A = [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
print(Solution().trap(A))
