def solution(n):
    # 에라토스테네스의 체 알고리즘
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for num in range(2, int(n**0.5) + 1):
        if is_prime[num]:
            # num의 배수들은 소수가 아님
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = False

    primes = [num for num in range(2, n + 1) if is_prime[num]]
    return len(primes)
