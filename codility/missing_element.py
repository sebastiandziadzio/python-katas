"""
Find the missing element in a given permutation.
"""

def solution(A):
    expected = set(range(1, len(A)+2))
    actual = set(A)
    return next(iter(expected-actual))
