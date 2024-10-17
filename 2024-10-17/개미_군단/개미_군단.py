def solution(hp):
    officer = hp // 5
    sergeant = hp % 5 // 3
    private = hp % 5 % 3
    return officer + sergeant + private
