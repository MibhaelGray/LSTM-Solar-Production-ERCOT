# ERCOT Market Structure: Key Concepts Guide

## Overview
ERCOT (Electric Reliability Council of Texas) operates the electricity grid and wholesale market for ~90% of Texas. Understanding its market structure is essential for electricity price forecasting and energy storage arbitrage projects.

## Geographic Structure

### Load Zones
**What they are**: Large geographic regions that group areas with similar electricity supply/demand characteristics.

**ERCOT's Four Load Zones**:
- **North**: Dallas-Fort Worth metroplex area (highest demand, urban)
- **West**: Sparsely populated area with abundant wind generation
- **South**: Austin, San Antonio, and surrounding areas
- **Houston**: Houston metropolitan area and Gulf Coast

**Why they matter**: Load zones have different price dynamics due to local supply/demand balance and transmission constraints.

### Trading Hubs
**What they are**: Virtual locations that aggregate multiple physical nodes for simplified trading.

**Key ERCOT Hubs**:
- **HB_BUSAVG**: System-wide average price (benchmark)
- **HB_NORTH**: North Load Zone hub
- **HB_WEST**: West Load Zone hub  
- **HB_SOUTH**: South Load Zone hub
- **HB_HOUSTON**: Houston Load Zone hub

**Purpose**: Allow market participants to trade electricity without specifying exact physical locations.

### Electrical Nodes (Buses)
**What they are**: Specific physical locations on the transmission grid where electricity is injected (generation) or withdrawn (load).

**Scale**: ERCOT has ~17,000 electrical buses, but only ~900 are "settlement points" where actual resources connect.

**Pricing**: Each node has its own Locational Marginal Price (LMP) reflecting local supply/demand conditions.

## Market Structure

### Day-Ahead Market (DAM)
**Timing**: Market participants submit bids/offers by 10 AM for the next day's electricity.

**Purpose**:
- Price discovery for planning purposes
- Generator scheduling and commitment
- Load scheduling and hedging

**Process**:
1. Market participants submit hourly bids/offers for all 24 hours of the next day
2. ERCOT runs optimization to clear the market
3. DAM prices published for each hour and location
4. Generators receive start-up instructions

**Key Point**: DAM prices are for planning - actual settlement uses Real-Time Market prices.

### Real-Time Market (RTM)
**Timing**: Runs every 5 minutes based on current grid conditions.

**Purpose**: 
- Balance actual supply and demand in real-time
- Handle deviations from DAM schedules
- Maintain grid reliability

**Process**:
1. Security Constrained Economic Dispatch (SCED) runs every 5 minutes
2. Calculates optimal generator dispatch and prices
3. All electricity consumption/production settled at RTM prices

## Pricing Concepts

### Locational Marginal Pricing (LMP)
**Definition**: The marg