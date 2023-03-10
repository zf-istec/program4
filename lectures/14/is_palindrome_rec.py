#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_palindrome_rec(s):
    # transform to lower case letters only
    def to_chars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    # the rec function
    def ispal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and ispal(s[1:-1])

    return ispal(to_chars(s))


print()
print(is_palindrome_rec("Aba"))
print(is_palindrome_rec("Able was I, ere I saw Elba"))
