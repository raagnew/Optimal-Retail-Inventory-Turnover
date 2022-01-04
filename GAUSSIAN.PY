def GAUSSIAN_SVL(N,R,S,L,T):
    """ Service level for OUTL N, demand rate R, demand standard deviation S, lead time L, and review period T """
    from scipy.stats import norm
    from math import sqrt
    SVL = 0
    if N > 0:
        X1 = R*(L+T)
        X2 = S*sqrt(L+T)
        X3 = R*L
        X4 = S*sqrt(L)
        S1 = (X2**2)*norm.pdf(N,X1,X2) - (N-X1)*norm.sf(N,X1,X2)
        S2 = (X4**2)*norm.pdf(N,X3,X4) - (N-X3)*norm.sf(N,X3,X4)
        SVL = 1-(S1-S2)/(R*T)
    return SVL

def GAUSSIAN_AVI(N,R,S,L,T):
    """ Average inventory for OUTL N, demand rate R, demand standard deviation S, lead time L, and review period T """
    from scipy.stats import norm
    from math import sqrt
    from math import exp
    AVI = 0
    if N > 0:
        X1 = R*(L+T)
        X2 = S*sqrt(L+T)
        X3 = R*L
        X4 = S*sqrt(L)
        W11 = (S**2/R**3)*(1+R*N/S**2)*norm.sf(N,X1,X2) - 2*(X2**2/R**2)*norm.pdf(N,X1,X2)
        W11 = W11 + (1/R**2)*(N-S**2/R)*exp(2*R*N/S**2)*norm.sf(N,-X1,X2)
        W12 = (S**2/R**3)*(1+R*N/S**2)*norm.sf(N,X3,X4) - 2*(X4**2/R**2)*norm.pdf(N,X3,X4)
        W12 = W12 + (1/R**2)*(N-S**2/R)*exp(2*R*N/S**2)*norm.sf(N,-X3,X4)
        AVI = (S**2)*(W11 - W12)
        V01 = (L+T-N/R-.5*S**2/R**2)*norm.sf(N,X1,X2) + (X2**2/R)*norm.pdf(N,X1,X2)
        V01 = V01 + .5*(S**2/R**2)*exp(2*R*N/S**2)*norm.sf(N,-X1,X2)
        V02 = (L-N/R-.5*S**2/R**2)*norm.sf(N,X3,X4) + (X4**2/R)*norm.pdf(N,X3,X4)
        V02 = V02 + .5*(S**2/R**2)*exp(2*R*N/S**2)*norm.sf(N,-X3,X4)
        AVI = AVI - N*(V01 - V02)
        V11 = .5*((L+T)**2-N**2/R**2 - 2*N*S**2/R**3 - 1.5*S**4/R**4)*norm.sf(N,X1,X2)
        V11 = V11 + (.5*X2**2/R**2)*(X1+3*S**2/R+N)*norm.pdf(N,X1,X2)
        V11 = V11 - (.5*S**2/R**3)*(N-1.5*S**2/R)*exp(2*R*N/S**2)*norm.sf(N,-X1,X2)
        V12 = .5*(L**2-N**2/R**2 - 2*N*S**2/R**3 - 1.5*S**4/R**4)*norm.sf(N,X3,X4)
        V12 = V12 + (.5*X4**2/R**2)*(X3+3*S**2/R+N)*norm.pdf(N,X3,X4)
        V12 = V12 - (.5*S**2/R**3)*(N-1.5*S**2/R)*exp(2*R*N/S**2)*norm.sf(N,-X3,X4)
        AVI = AVI + R*(V11 - V12)
        AVI = N - R*(L + T/2) + AVI/T
    return AVI

def GAUSSIAN_OUTL(U,I,P,C,R,S,L,T):
    """ Optimal OUTL for time units per year U, annual inventory carrying cost rate I, unit price P, unit cost C,
    demand rate R, demand standard deviation S, lead time L, and review period T """
    M = I*C/(P - C)
    N = 0
    SVL0 = 0
    AVI0 = 0
    X = 1000000
    while X >= M:
        N = N + 1
        SVL1 = GAUSSIAN_SVL(N,R,S,L,T)
        AVI1 = GAUSSIAN_AVI(N,R,S,L,T)
        if AVI1 > .0000001: X = U*R*(SVL1 - SVL0)/(AVI1 - AVI0)
        else: X = 1000000
        SVL0 = SVL1
        AVI0 = AVI1
    return N - 1

def GAUSSIAN_PROFIT(U,I,P,C,N,R,S,L,T):
    """ Average annual profit for time units per year U, annual inventory
    carrying cost I, unit price P, unit cost C, OUTL N, demand rate R,
    demand standard deviation S, lead time L, review period T """
    return (P-C)*U*R*GAUSSIAN_SVL(N,R,S,L,T) - I*C*GAUSSIAN_AVI(N,R,S,L,T)







