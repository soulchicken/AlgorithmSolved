def solution(numbers, hand):
    l = dict([(1,(0,0)),(4,(0,1)),(7,(0,2))])
    r = dict([(3,(2,0)),(6,(2,1)),(9,(2,2))])
    c = dict([(2,(1,0)),(5,(1,1)),(8,(1,2)),(0,(1,3))])
    right_hand = [0,3]
    left_hand = [2,3]
    answer = ''
    for n in numbers:
        if n in l:
            answer += 'L'
            left_hand = l[n]
        elif n in r:
            answer += 'R'
            right_hand = r[n]
        else:
            i,j = c[n]
            right_distance = abs(right_hand[0] - i) + abs(right_hand[1] - j)
            left_distance = abs(left_hand[0] - i) + abs(left_hand[1] - j)
            if right_distance < left_distance or hand == 'right' and right_distance == left_distance:
                answer += 'R'
                right_hand = c[n]
            else:
                answer += 'L'
                left_hand = c[n]
    return answer
