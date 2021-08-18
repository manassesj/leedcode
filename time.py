ti, mi, tf, mf = map(int, input().split())


if tf > ti and mf>=mi:    
    h = tf - ti
    m = mf - mi
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))

elif tf > ti and mi>mf:
    h = (tf - 1) - ti
    m = (60 - mi) + mf 
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
    
elif ti>tf and mf>=mi:
    h = (24 - ti) + tf
    m = mf - mi
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))
    
elif ti>=tf and mi>mf:
    h = (23 - ti) + tf
    m = (60 - mi) + mf 
    print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" %(h,m))

elif tf==ti and mf>mi:
    m = mf - mi
    print("O JOGO DUROU 0 HORA(S) E %i MINUTO(S)" %(m))
elif ti==tf and mi==mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")  