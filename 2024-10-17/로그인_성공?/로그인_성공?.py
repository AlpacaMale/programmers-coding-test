def solution(id_pw, db):
    _id, passwd = id_pw
    for db_id, db_passwd in db:
        if db_id == _id:
            return "login" if passwd == db_passwd else "wrong pw"
    return "fail"
