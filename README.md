# LSTM-Solar-Production-ERCOT

The idea behind this project is basically to forecast when energt price spikes and price differences between locations. By forecasting when energy energy price spikes we can enable battery companies in Texas to more efficiently perform energy arbitrage.

### Value Proposition Of Project:

A battery in West Texas could charge at $25/MWh and sell at $800/MWh if it could somehow transport that electricity to North Texas (Dallas area) instantly (which it can't). But a battery strategically located between congested areas can capture these price differentials. The ML project predicts the price spread between West and North hubs, with a focus on daily patterns.
By forecasting a complex system where supply, demand, transmission constraints, and weather we can create profit opportunities.

### Scope:

I will focus exclusively on ERCOT's North and West load zones, using historical settlement point price data to build an LSTM model that predicts daily average price spreads between these regions. The model will identify arbitrage opportunities by forecasting when West Texas prices will be significantly lower than North Texas prices (>$25/MWh differential), enabling battery storage companies to optimize charge/discharge timing across geographic locations.

### Target Variable: 

Day-Ahead Market Settlement Prices: https://www.ercot.com/mp/data-products/data-product-details?id=NP4-190-CD