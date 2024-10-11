def count_divisors(n):
    count = 0
    sqrt_n = int(n**0.5)
    for i in range(1,sqrt_n+1):
        if n%i==0:
            count+=1
            if i != n // i:
                count+=1
    return count


def solution(number, limit, power):
    total_power_needed = []
    for num in range(1, number + 1):
        number_of_divisors = count_divisors(num)
        total_power_needed.append([number_of_divisors, power][limit < number_of_divisors])
    return sum(total_power_needed)