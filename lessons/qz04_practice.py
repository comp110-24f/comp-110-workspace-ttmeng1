"""Recursion practice for Quiz 04"""

from __future__ import annotations


# 1
def factorial(num: int) -> int:
    """Returns factorial of input number."""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# 2
def sum_of_natural_numbers(num: int) -> int:
    """Returns sum of first n natural numbers."""
    if num == 0:
        return 0
    else:
        return num + sum_of_natural_numbers(num - 1)


# 3
def sum_of_digits(num: str) -> int:
    """Sums digits of a number"""
    if len(num) == 1:
        return int(num)
    else:
        return int(num[0]) + sum_of_digits(num[1:])


# 4
def power(num: int, exp: int) -> int:
    """Returns power of number"""
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * power(num, exp - 1)


# 5
def gcd(num1: int, num2: int) -> int:
    """Returns gcd of 2 numbers (uses Euclidean algorithm)"""
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)


# 7
def fibonacci(num: int) -> int:
    """Computes n-th number in Fibonacci sequence."""
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


# 8
def factorial_list(nums: list[int]) -> list[int]:
    """Returns a list with factorial of each element in list."""
    result: list[int] = []
    for num in nums:
        result.append(factorial(num))
    return result


# Challenge 1
def fibonacci_sequence(up_to: int, fib_list: list[int]) -> list[int]:
    """Generates Fibonacci sequence as list until it exceeds up_to."""
    if len(fib_list) < 2:
        fib_list = [0, 1]
    next: int = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
    if next > up_to:
        return fib_list
    fib_list.append(next)
    return fibonacci_sequence(up_to, fib_list)


# Challenge 2
def binary_search(arr: list[int], target: int, low: int, high: int) -> int:
    """Finds if target exists in sorted list of intervals."""
    if high >= low:
        mid: int = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    return -1


# ------------------Recursive Structures-----------------------


# 1
class Node:
    def __init__(self, value: list[int], next: Node | None):
        self.value = value  # A list of integers
        # Either another Node or None
        if next is None:
            self.next = None
        else:
            self.next = next


# 1a
def sum_node_values(node: Node | None) -> int:
    if node is None:
        return 0
    else:
        current: int = 0
        for num in node.value:
            current += num
        return current + sum_node_values(node.next)


# 1b
def increment_node_values(node: Node | None) -> None:
    if node is None:
        return None
    else:
        for num in node.value:
            num += 1
        increment_node_values(node.next)
