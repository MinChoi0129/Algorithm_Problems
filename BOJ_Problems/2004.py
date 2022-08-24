#참고 사이트 : https://codedrive.tistory.com/175
def NumCount(user):
    
    power = 1
    two_count = 0
    while(user//(2**power) > 0): 
        two_count += user//(2**power)
        power += 1
    
    power = 1  
    five_count = 0
    while(user//(5**power) > 0): 
        five_count += user//(5**power)
        power += 1
        
    return two_count, five_count
    

n, m = map(int, input().split())

n_2, n_5 = NumCount(n)
m_2, m_5 = NumCount(m)
n_sub_m_2, n_sub_m_5 = NumCount(n - m)

tot_2 = n_2-m_2 - n_sub_m_2
tot_5 = n_5-m_5 - n_sub_m_5

print(min(tot_2, tot_5))