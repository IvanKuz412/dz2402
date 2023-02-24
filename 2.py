class Solution:
    def tree(self, n, c='*'):
        c1 = c
        while n != 0:
            print(' ' * (n - 1) + c1 + ' ' * (n - 1))
            n = n - 1
            c1 = c1 + c + c
b = Solution()
b.tree(10, '*')