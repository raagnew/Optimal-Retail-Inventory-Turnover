def POISSON_SVL(N,R,L,T):
    """ One-at-a-time independent, random demands """
    """ Service level for OUTL N, demand rate R, lead time L, review period T """
    from scipy.stats import poisson
    S = 0
    if N > 0:
        for K in range(1,N+1):
            P1 = poisson.cdf(K-1,R*L)
            P2 = poisson.cdf(K-1,R*(L+T))
            S = S + P1 - P2
    return S/(R*T)
            
def POISSON_AVI(N,R,L,T):
    """ One-at-a-time independent, random demands """
    """ Average inventory for OUTL N, demand rate R, lead time L, review period T """
    AVI = 0
    if N > 0:
        for K in range(1,N+1): AVI = AVI + POISSON_SVL(K,R,L,T)
    return AVI
    
def POISSON_OUTL(U,I,P,C,R,L,T):
    """ One-at-a-time independent, random demands """
    """ Optimal OUTL for time units per year U, annual inventory carrying cost I,
    unit price P, unit cost C, demand rate R, lead time L, review period T """
    M = I*C/(P - C) # Marginal Turnover Minimum
    N = 0
    SVL0 = 0
    X = 1000000
    while X >= M:
        N = N + 1
        SVL1 = POISSON_SVL(N,R,L,T)
        if SVL1 > .000001: X = U*R*(SVL1 - SVL0)/SVL1
        else: X = 1000000
        SVL0 = SVL1
    return N-1

def POISSON_PROFIT(U,I,P,C,N,R,L,T):
    """ One-at-a-time independent, random demands """
    """ Average annual profit for time units per year U, annual inventory
    carrying cost I, unit price P, unit cost C, OUTL N, demand rate R,
    lead time L, review period T """
    return (P-C)*U*R*POISSON_SVL(N,R,L,T) - I*C*POISSON_AVI(N,R,L,T)

def POISSON_SVL_CMP(N,R,S,L,T):
    """ Random transaction quantities at Poisson random time points demands """
    """ Service level for OUTL N, demand rate R, demand standard deviation s, lead time L, review period T """
    ATQ = S**2/R
    return POISSON_SVL(round(N/ATQ,0),R/ATQ,L,T)

def POISSON_AVI_CMP(N,R,S,L,T):
    """ Random transaction quantities at Poisson random time points demands """
    """ Service level for OUTL N, demand rate R, demand standard deviation S, lead time L, review period T """
    ATQ = S**2/R
    return ATQ*POISSON_AVI(round(N/ATQ,0),R/ATQ,L,T)

def POISSON_OUTL_CMP(U,I,P,C,R,S,L,T):
    """ Random transaction quantities at Poisson random time points demands """
    """ Optimal OUTL for time units per year U, annual inventory carrying cost I,
    unit price P, unit cost C, demand rate R, demand standard deviation S, lead time L, review period T """
    ATQ = S**2/R
    return round(ATQ*POISSON_OUTL(U,I,P,C,R/ATQ,L,T))

def POISSON_PROFIT_CMP(U,I,P,C,N,R,S,L,T):
    """ One-at-a-time independent, random demands """
    """ Average annual profit for time units per year U, annual inventory
    carrying cost I, unit price P, unit cost C, OUTL N, demand rate R, demand standard deviation S,
    lead time L, review period T """
    return (P-C)*U*R*POISSON_SVL_CMP(N,R,S,L,T) - I*C*POISSON_AVI_CMP(N,R,S,L,T)


