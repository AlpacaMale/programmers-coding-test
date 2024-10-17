def solution(emergency):
    emergency_rated_order = {
        rate: index + 1
        for index, rate in enumerate(sorted(emergency, key=lambda x: -x))
    }
    return [emergency_rated_order[rate] for rate in emergency]
