def min_window(S: str, T: str) -> str:
    """
    Minimum Window Substring

    :param str S:
    :param str T:
    :return str:
    """
    Tc = Counter(T)
    Sc = Counter()

    best_i = -sys.maxsize
    best_j = sys.maxsize

    i = 0

    for j, char in enumerate(S):
        Sc[char] += 1

        while Sc & Tc == Tc:
            if j - i < best_j - best_i:
                best_i, best_j = i, j

            Sc[S[i]] -= 1
            i += 1

    return S[best_i : best_j + 1] if best_j - best_i < len(S) else ""