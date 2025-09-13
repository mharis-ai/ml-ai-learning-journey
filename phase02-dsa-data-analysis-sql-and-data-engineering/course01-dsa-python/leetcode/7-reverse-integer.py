class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 -1
        int_min = -2**31
        negative = x<0
        x = abs(x)
        result = 0
        while x>=1:
            last_digit = x % 10
            if result > int_max//10 or (result == int_max//10 and last_digit > 7):
                return 0
            result = result * 10 + last_digit
            x//=10
        return -result if negative else result