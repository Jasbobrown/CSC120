def annoying_fibonacci_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    out = annoying_fibonacci_sequence(n-1)
    out.append(out[-1] + out[-2])
    return out