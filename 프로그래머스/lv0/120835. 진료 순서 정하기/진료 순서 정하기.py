def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    answer = [sorted_emergency.index(i)+1 for i in emergency]
    return answer