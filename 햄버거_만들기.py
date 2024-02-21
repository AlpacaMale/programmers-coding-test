def solution(ingredient):
    count = 0
    string = ""
    burger = "1231"
    for num in ingredient:
        string += str(num)
        if num == 1 and string[-4:] == burger:
            string = string[:-4]
            count += 1
    return count
