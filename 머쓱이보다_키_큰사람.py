def solution(array, height):
    return sum(friend_height > height for friend_height in array)
