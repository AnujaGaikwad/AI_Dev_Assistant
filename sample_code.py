# sample_code.py
# A sample file with intentional bugs + undocumented code
# Use this to demo the AI Dev Assistant

class Calculator:
    def divide(self, a, b):
        return a / b  # Bug: no zero-division guard

    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)  # Bug: no guard for negative numbers

    def find_max(self, numbers):
        max_val = numbers[0]  # Bug: crashes on empty list
        for n in numbers:
            if n > max_val:
                max_val = n
        return max_val

def reverse_string(s):
    return s[::-1]

def count_words(text):
    words = text.split(" ")
    return len(words)  # Bug: doesn't handle multiple spaces

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]  # Bug: doesn't strip punctuation/spaces

if __name__ == "__main__":
    calc = Calculator()
    print(calc.divide(10, 2))
    print(calc.factorial(5))
    print(reverse_string("hello"))
    print(count_words("  hello   world  "))
    print(is_palindrome("A man a plan a canal Panama"))
