def solution(s):
    try:
        int(s)
        return len(s) == 4 or len(s) == 6
           
    except:
        return False
