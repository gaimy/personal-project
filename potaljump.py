def potaljump(h0, hw, g, count):
    vs = (2*g*h0)**.5
    hs = .0
    i=0
    while i<count :
        m = vs
        vs = hs
        hs = m

        jumptime = 0
        jumptime += vs/g

        hm = (vs**2)/(2*g) + hw
        vs = (2*g*hm)**.5

        jumptime += vs/g
        print("활공 거리(m) = ",round(jumptime*hs,2))
        print("최대 높이(m) = ",round(hm,2))
        print("수평속도(m/s) = ",round(hs,2))
        print("수직속도(m/s) = ",round(vs,2),"\n")

        i+=1

potaljump(10,10,10,10)
