def A(IPf, OPf):
    
    with open(IPf), open(OPf):
        lines = open(IPf).readlines()
        open(OPf, 'w').writelines(lines[::2])

Ip,Op= "/Users/sreekarsbs/Desktop/Lab10/Lab10/input.txt",'/Users/sreekarsbs/Desktop/Lab10/Lab10/output.txt'
A(Ip, Op)









 