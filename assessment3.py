import timeit

pattern_exist = "дослідження"
pattern_not_exist = "fj39f8jsf"


def kmp_search(pattern, text):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1


def rabin_karp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    q = 101  # просте число
    d = 256
    h = pow(d, m-1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                return s
        if s < n - m:
            t = (d*(t - ord(text[s])*h) + ord(text[s+m])) % q
            if t < 0:
                t += q
    return -1


def boyer_moore_search(pattern, text):
    m = len(pattern)
    n = len(text)
    skip = {}
    for k in range(m-1):
        skip[pattern[k]] = m-k-1
    k = m-1
    while k < n:
        j = m-1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i+1
        k += skip.get(text[k], m)
    return -1


with open("doc1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()
with open("doc2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()\


def measure(func, pattern, text):
    return timeit.timeit(lambda: func(pattern, text), number=1)

for filename, text in [("стаття 1", text1), ("стаття 2", text2)]:
    print(f"\nДля {filename}:")
    for pattern, label in [(pattern_exist, "існуючий"), (pattern_not_exist, "вигаданий")]:
        times = []
        for func, name in [(kmp_search, "KMP"), (rabin_karp_search, "Rabin-Karp"), (boyer_moore_search, "Boyer-Moore")]:
            t = measure(func, pattern, text)
            times.append((t, name))
            print(f"  {name} для '{label}': {t:.6f} секунд")
        fastest = min(times)[1]
        print(f"  -> Найшвидший для '{label}': {fastest}")