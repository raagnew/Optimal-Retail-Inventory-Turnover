# Simulated demand vectors for lower demand items
set.seed(17) # Set random number seed for reproducible results
# Pure Poisson demand 
pois_dmds_low <- rpois(156,4) # 3 years of randomly-generated Poisson weekly demands: mean = 4, variance = 4, std deviation = sqrt(4) = 2
# Compound Poisson demand  -  particular compounding distribution is of course arbitrary and for demonstration only
n <- rpois(156,2)
cpois_dmds_low <- NULL
for (i in 1:156){
cpois_dmds_low <- c(cpois_dmds_low,sum(sample.int(4,n[i],replace=TRUE,prob=c(.4,.3,.2,.1))))} # 3 years of randomly-generated Compound Poisson weekly demands: mean = 4, variance = 10, std deviation = sqrt(10) = 3.1622777

# Simulated demand vectors for higher demand items
# Pure Poisson demand
pois_dmds_high <- rpois(156,64) # 3 years of randomly-generated Poisson weekly demands: mean = 64, variance = 64, std deviation = sqrt(64) = 8
# Compound Poisson demand  -  particular compounding distribution is of course arbitrary and for demonstration only
n <- rpois(156,32)
cpois_dmds_high <- NULL
for (i in 1:156){
cpois_dmds_high <- c(cpois_dmds_high,sum(sample.int(4,n[i],replace=TRUE,prob=c(.4,.3,.2,.1))))} # 3 years of randomly-generated Compound Poisson weekly demands: mean = 64, variance = 160, std deviation = sqrt(160) = 12.649111

write.csv(cbind(pois_dmds_low,cpois_dmds_low,pois_dmds_high,cpois_dmds_high),file="c://RETAIL/DEMANDS.csv",row.names=FALSE)