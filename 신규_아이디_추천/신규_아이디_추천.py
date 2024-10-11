def solution(new_id):
    new_id_phase1 = new_id.lower()
    new_id_phase2 = "".join(
        char
        for char in new_id_phase1
        if char.isalpha() or char.isdigit() or char in ["-", "_", "."]
    )
    new_id_phase3 = ""
    flag = False
    for char in new_id_phase2:
        if char == "." and not flag:
            flag = True
            new_id_phase3 += char
        elif char != "." and flag:
            flag = False
            new_id_phase3 += char
        elif not flag:
            new_id_phase3 += char
    new_id_phase4 = new_id_phase3.strip(".")
    new_id_phase5 = new_id_phase4 or "a"
    new_id_phase6 = new_id_phase5[:15].rstrip(".")
    new_id_phase7 = new_id_phase6
    if len(new_id_phase6) <= 2:
        for _ in range(3 - len(new_id_phase6)):
            new_id_phase7 += new_id_phase6[-1]
    return new_id_phase7
