class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        ncols = len(A[0])
        nrows = len(A)

        arr = []

        for col in range(ncols):
            r = 0
            c = col
            a = []
            for row in range(nrows):
                if c < 0:
                    a.append(0)
                else:
                    a.append(A[r][c])

                r += 1
                c -= 1
            arr.append(a)

        for row in range(1, nrows):
            r = row
            c = ncols - 1
            a = []
            for col in range(ncols):
                # print(r, c)
                if r >= nrows:
                    a.append(0)
                else:
                    a.append(A[r][c])
                r += 1
                c -= 1
            arr.append(a)

        return arr


A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

print(Solution().diagonal(A))
