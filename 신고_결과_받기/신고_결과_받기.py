def solution(id_list, reports, k):
    id_report = {id_: [] for id_ in id_list}
    banned = []

    for report in set(reports):
        reporter, suspect = report.split()
        id_report[reporter].append(suspect)

    for id_ in id_list:
        count = 0
        for suspect in id_report.values():
            if id_ in suspect:
                count += 1
        if count >= k:
            banned.append(id_)

    return [
        sum(suspect_id in banned for suspect_id in suspect_ids)
        for user_id, suspect_ids in id_report.items()
    ]
