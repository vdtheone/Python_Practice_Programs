"""Minimum Window Substring (refactored).

Provides `min_window(s, t)` which returns the smallest substring
of `s` that contains all characters of `t` (including multiplicity).
"""

from collections import Counter, defaultdict
from typing import Tuple


def min_window(s: str, t: str) -> str:
    """Return the minimum window substring of `s` containing all chars of `t`.

    If no such window exists, returns an empty string.
    """
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    left = 0
    right = 0
    formed = 0
    window_counts = defaultdict(int)
    ans: Tuple[float, int, int] = (float("inf"), None, None)

    while right < len(s):
        ch = s[right]
        window_counts[ch] += 1

        if ch in dict_t and window_counts[ch] == dict_t[ch]:
            formed += 1

        while left <= right and formed == required:
            ch = s[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[ch] -= 1
            if ch in dict_t and window_counts[ch] < dict_t[ch]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    # simple verification
    print(min_window("ADOBECODEBANC", "ABC"))