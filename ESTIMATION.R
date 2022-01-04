ESTIMATES <- function(s,n){
# Simple demand parameter estimation function  -  keep it simple
# Randomness in estimates is unavoidable
# s =  vector of past sales in time order
# n = number of elements in s to be utilized in estimation
v <- mean(tail(s,n)) # Mean of last n sales elements  -  for input into optimal OUTL calculation
v <- c(v,sd(tail(s,n))) # Append standard deviation of last n sales elements  -  for input into optimal OUTL calculation
v <- c(v,v[2]^2/v[1]) # Append conservative estimate of average transaction quantity  -  for checking  -  should be
# around 1 for pure Poisson demand
v <- c(v,v[1]/v[3]) # Append conservative estimate of order arrival rate  -  for checking
v}

x <- read.csv(file="c://RETAIL/DEMANDS.csv",header=TRUE)
attach(x)

ESTIMATES(pois_dmds_low,156)

ESTIMATES(cpois_dmds_low,156)

ESTIMATES(pois_dmds_high,156)

ESTIMATES(cpois_dmds_high,156)

ESTIMATES(pois_dmds_high,52)

ESTIMATES(cpois_dmds_high,52)







