# LSTM-West-Texas-Price-Forecasting-ERCOT

The idea behind this project is to forecast energy price spikes in WEST_HUB (West Texas) settlement prices. By forecasting when energy price spikes occur in West Texas, we can enable battery companies to more efficiently perform energy arbitrage and optimize their charge/discharge timing.

### Value Proposition Of Project:

A battery storage system in West Texas can capture significant arbitrage opportunities by charging during low-price periods and discharging during high-price spikes. For example, a battery could charge at $25/MWh during off-peak hours and sell at $800/MWh during extreme price events. The ML project predicts West Texas settlement prices with a focus on identifying when price spikes will occur, enabling battery storage companies to optimize their operational timing and maximize revenue.

By forecasting this complex system where supply, demand, transmission constraints, and weather all influence prices, we can create profitable opportunities for energy storage deployment and operation.

### Scope:

I will focus exclusively on ERCOT's West Texas load zone (WEST_HUB), using historical settlement point price data to build an LSTM model that predicts hourly and daily price movements. The model will identify price spike opportunities by forecasting when West Texas prices will exceed certain thresholds (e.g., >$100/MWh), enabling battery storage companies to optimize their charge/discharge timing and maximize arbitrage profits in this specific geographic region.

### Target Variable: 

Day-Ahead Market Settlement Prices for WEST_HUB: https://www.ercot.com/mp/data-products/data-product-details?id=NP4-190-CD


## DIRECTORY STRUCTURE (for context)

```
Energy Forecasting/
  ├── Data/
  │     ├── ERCOT Data/
  │     │     └── Wind Data/
  │     │           └── windPull.ipynb
  │     ├── Scripts/
  │     │     ├── HubFilter.py
  │     │     ├── merge.py
  │     │     ├── dataExtraction.py
  │     │     ├── merge_ercot_csv.py
  │     │     └── unzip_ercot_data.py
  │     └── filter_merged_ercot_data.csv
  ├── ERCOT.md
  ├── notebooks/
  │     └── model.ipynb
  ├── README.md
  ├── requirements.txt
  └── src/
```

