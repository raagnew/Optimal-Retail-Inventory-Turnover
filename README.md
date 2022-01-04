# Optimal-Retail-Inventory-Turnover

The setting here is a periodic-review retail inventory system with random demands, known delivery lead time, and no backlogging (i.e., sales are lost if stock is insufficient).  Inventory items are “staples” with little seasonality or trending, everything from underwear to shock absorbers to service parts.  Exact calculations are very complicated, but lower bounds for service level (fraction of demand serviced) and average unit inventory are readily computed. Moreover, these lower bounds are very sharp in the high service level domain where most inventory systems seek to operate.  Taking into account profit margin, these quantities also allow approximation of optimal order-up-to-level and resulting inventory turnover, providing a tradeoff between lost margin and inventory carrying cost.

Mathematical details are provided in my 1975 Journal of Applied Probability paper plus formulas from Appendix 4 of Hadley & Whitin’s Analysis of Inventory Systems.  Algorithms are provided in Excel/VBA, R, and Python, allowing for easy implementation.  Calculations are illustrated for both Poisson demands and Gaussian demands.

We also provide simple R and Python estimation scripts for the mean and standard deviation of demand.  Since we are dealing with staple items, many with low demand rates, simplicity in “forecasting” seems warranted.

Finally, we provide simulation results for one particular scenario to illustrate that our bounds are tight and to visualize what is going on in the inventory replenishment process.  
