def erato_sieve(x, get_primes = False):
    """エラトステネスの篩

    0からxまでの素数を返す
    計算量: O(n loglog n)

    Args:
        x (int): 素数判定をしたい数の最大値
        get_primes(bool): 素数のみが入ったリストを返すかどうか

    Returns:
        list: get_primesがTrueの時
                素数飲みが入ったリスト
              get_primesがFalseの時
                i番目が素数ならTrue, そうでないならFalse
    """
    primes = []
    prime_list = [True]*(x+1)
    prime_list[0] = False
    prime_list[1] = False
    p = 2
    while p <= x:
        if not prime_list[p]:
            p += 1
            continue
        
        primes.append(p)
        i = p*2
        while i <= x:
            prime_list[i] = False
            i += p
        p += 1

    return primes if get_primes else prime_list