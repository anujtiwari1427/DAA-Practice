def t_o_h(n,s,a,d):
    if n == 1:
        print("Move 1 disk from ",s,'to',d)
        return
    t_o_h(n-1,s,d,a)
    print("Move disk:",n,"from",s,'to',d)
    t_o_h(n-1,a,s,d)
disks = 3
t_o_h(disks,'A','B','C')