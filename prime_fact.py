def prime_fact(x):
    """素因数分解

    素数判定も可能
    計算量: O(n**(1/2))

    Args:
        x (int): 素因数分解する整数

    Returns:
        dict: {素因数:指数, 素因数:指数, ...}    
    """
    prime_dict = {}
    p = 2
    while p**2 <= x:
        if x % p == 0:
            prime_dict.setdefault(p, 0)
            prime_dict[p] += 1
            x //= p
        else:
            p = 3 if p == 2 else p + 2
    if x != 1:
        prime_dict.setdefault(x, 0)
        prime_dict[x] += 1
    return prime_dict