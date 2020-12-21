"""
h0 = 떨어질 때 높이
hw = 벽 포탈의 높이
g = 중력가속도
count = 도약 횟수
"""
def potaljump(h0,hw,g,count):
    
    vs = (2*g*h0)**0.5 #수직 속력
    hs = 0.0        #수평 속력

    i = 0
    while i<count :
        
        m = vs
        vs = hs
        hs = m
        #수평 속력, 수직 속력을 서로 바꾼다
        
        jumptime = 0
        jumptime += vs/g
        #수직속력을 중력가속도로 나눠 시간 구하기(vs>0)

        hm = (vs**2))/(2*g) + hw
        #최고점 높이 등가속도운동 변위공식
        vs = (2*g*hm)**0.5
        #최고점 높이 기준으로 수직속력 다시 구하기
        
        jumptime += vs/g
        #수직속력을 중력가속도로 나눠 시간 구하기(0>vs)
        print("활공 거리(m) = ",round(jumptime*hs,2))
        print("수평 속도(m/s) = ",round(hs, 2))
        print("수직 속도(m/s) = ",round(vs, 2)), "\n")

        i+=1
