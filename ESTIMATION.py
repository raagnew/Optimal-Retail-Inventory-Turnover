import pandas as pd
x = pd.read_csv("c://RETAIL/DEMANDS.csv")

def ESTIMATES(s,n):
    mn = x[s][-n:].mean()
    sd = x[s][-n:].std()
    atq = sd**2/mn
    aor = mn/atq
    return [[mn],[sd],[atq],[aor]]
    
print()
print("pois_dmds_low_156",str(ESTIMATES("pois_dmds_low",156)))
print()
print("cpois_dmds_low_156",str(ESTIMATES("cpois_dmds_low",156)))
print()
print("pois_dmds_high_156",str(ESTIMATES("pois_dmds_high",156)))
print()    
print("cpois_dmds_high_156",str(ESTIMATES("cpois_dmds_high",156)))
print()
print("pois_dmds_high_52",str(ESTIMATES("pois_dmds_high",52)))
print()
print("cpois_dmds_high_52",str(ESTIMATES("cpois_dmds_high",52)))
