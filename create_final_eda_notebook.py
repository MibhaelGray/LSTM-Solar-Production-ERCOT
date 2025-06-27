import json

# Create the notebook structure
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Final ERCOT Dataset Analysis\n",
                "\n",
                "This notebook analyzes the final_ercot_dataset.csv with comprehensive EDA similar to the preliminary analysis."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Import and Load Final Dataset"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "import numpy as np\n",
                "from scipy import stats\n",
                "\n",
                "# Load the final dataset\n",
                "print(\"Loading final_ercot_dataset.csv...\")\n",
                "final_dataset = pd.read_csv(\"../Data/ERCOT Data/final_ercot_dataset.csv\")\n",
                "\n",
                "print(f\"Dataset shape: {final_dataset.shape}\")\n",
                "print(f\"Columns: {final_dataset.columns.tolist()}\")\n",
                "print(\"\\nFirst 5 rows:\")\n",
                "print(final_dataset.head())\n",
                "print(\"\\nData types:\")\n",
                "print(final_dataset.dtypes)\n",
                "print(\"\\nMissing values:\")\n",
                "print(final_dataset.isna().sum())"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Data Preprocessing"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Convert date column to datetime\n",
                "final_dataset['Hour Ending'] = pd.to_datetime(final_dataset['Hour Ending'])\n",
                "final_dataset['DeliveryDate'] = final_dataset['Hour Ending'].dt.date\n",
                "final_dataset['DayOfWeek'] = final_dataset['Hour Ending'].dt.day_name()\n",
                "final_dataset['Month'] = final_dataset['Hour Ending'].dt.month_name()\n",
                "final_dataset['Year'] = final_dataset['Hour Ending'].dt.year\n",
                "final_dataset['Hour'] = final_dataset['Hour Ending'].dt.hour\n",
                "\n",
                "print(f\"Date range: {final_dataset['Hour Ending'].min()} to {final_dataset['Hour Ending'].max()}\")\n",
                "print(f\"Total data points: {len(final_dataset):,}\")\n",
                "print(f\"Years covered: {final_dataset['Year'].nunique()}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Comprehensive EDA (Similar to Preliminary Analysis)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "fig, axes = plt.subplots(2, 3, figsize=(18, 12))\n",
                "fig.suptitle('Final ERCOT Dataset Analysis - Target Price', fontsize=16, fontweight='bold')\n",
                "\n",
                "# 1. Histogram\n",
                "axes[0, 0].hist(final_dataset['Target_Price'], bins=100, alpha=0.7, color='orange', edgecolor='black')\n",
                "axes[0, 0].set_xlabel('Price ($/MWh)')\n",
                "axes[0, 0].set_ylabel('Frequency')\n",
                "axes[0, 0].set_title('Target Price Distribution')\n",
                "axes[0, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# 2. Box Plot\n",
                "axes[0, 1].boxplot(final_dataset['Target_Price'])\n",
                "axes[0, 1].set_ylabel('Price ($/MWh)')\n",
                "axes[0, 1].set_title('Target Price Box Plot')\n",
                "axes[0, 1].grid(True, alpha=0.3)\n",
                "\n",
                "# 3. Q-Q Plot\n",
                "stats.probplot(final_dataset['Target_Price'], dist=\"norm\", plot=axes[0, 2])\n",
                "axes[0, 2].set_title('Q-Q Plot (Normality Check)')\n",
                "axes[0, 2].grid(True, alpha=0.3)\n",
                "\n",
                "# 4. Average prices by day of week\n",
                "day_avg = final_dataset.groupby('DayOfWeek')['Target_Price'].mean()\n",
                "day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']\n",
                "day_avg = day_avg.reindex(day_order)\n",
                "\n",
                "axes[1, 0].bar(day_avg.index, day_avg.values, color='skyblue', edgecolor='black')\n",
                "axes[1, 0].set_xlabel('Day of Week')\n",
                "axes[1, 0].set_ylabel('Average Price ($/MWh)')\n",
                "axes[1, 0].set_title('Average Prices by Day of Week')\n",
                "axes[1, 0].tick_params(axis='x', rotation=45)\n",
                "axes[1, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# 5. Average prices by month\n",
                "month_avg = final_dataset.groupby('Month')['Target_Price'].mean()\n",
                "month_order = ['January', 'February', 'March', 'April', 'May', 'June', \n",
                "               'July', 'August', 'September', 'October', 'November', 'December']\n",
                "month_avg = month_avg.reindex(month_order)\n",
                "\n",
                "axes[1, 1].bar(month_avg.index, month_avg.values, color='lightgreen', edgecolor='black')\n",
                "axes[1, 1].set_xlabel('Month')\n",
                "axes[1, 1].set_ylabel('Average Price ($/MWh)')\n",
                "axes[1, 1].set_title('Average Prices by Month')\n",
                "axes[1, 1].tick_params(axis='x', rotation=45)\n",
                "axes[1, 1].grid(True, alpha=0.3)\n",
                "\n",
                "# 6. Summary statistics as text\n",
                "stats_text = f\"\"\"\n",
                "TARGET PRICE STATISTICS\n",
                "\n",
                "Mean: ${final_dataset['Target_Price'].mean():.2f}/MWh\n",
                "Median: ${final_dataset['Target_Price'].median():.2f}/MWh\n",
                "Std Dev: ${final_dataset['Target_Price'].std():.2f}/MWh\n",
                "Min: ${final_dataset['Target_Price'].min():.2f}/MWh\n",
                "Max: ${final_dataset['Target_Price'].max():.2f}/MWh\n",
                "\n",
                "Data Points: {len(final_dataset):,}\n",
                "Date Range: {final_dataset['Hour Ending'].min().strftime('%Y-%m-%d')} to {final_dataset['Hour Ending'].max().strftime('%Y-%m-%d')}\n",
                "\"\"\"\n",
                "\n",
                "# Normality test\n",
                "try:\n",
                "    shapiro_stat, shapiro_p = stats.shapiro(final_dataset['Target_Price'].sample(min(5000, len(final_dataset))))\n",
                "    normality_text = f\"\\nNORMALITY TEST\\nShapiro-Wilk p-value: {shapiro_p:.2e}\\n\"\n",
                "    if shapiro_p < 0.05:\n",
                "        normality_text += \"Data is NOT normally distributed\"\n",
                "    else:\n",
                "        normality_text += \"Data appears normally distributed\"\n",
                "except:\n",
                "    normality_text = \"\\nNORMALITY TEST\\nCould not perform Shapiro-Wilk test\"\n",
                "\n",
                "axes[1, 2].text(0.1, 0.5, stats_text + normality_text, transform=axes[1, 2].transAxes, \n",
                "                fontsize=10, verticalalignment='center', fontfamily='monospace')\n",
                "axes[1, 2].set_title('Summary Statistics')\n",
                "axes[1, 2].axis('off')  \n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Time Series Analysis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Time series plot\n",
                "plt.figure(figsize=(15, 6))\n",
                "plt.plot(final_dataset['Hour Ending'], final_dataset['Target_Price'], alpha=0.6, linewidth=0.5)\n",
                "plt.title('Target Price Over Time')\n",
                "plt.xlabel('Date')\n",
                "plt.ylabel('Price ($/MWh)')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.xticks(rotation=45)\n",
                "plt.tight_layout()\n",
                "plt.show()\n",
                "\n",
                "# Average prices by hour of day\n",
                "hour_avg = final_dataset.groupby('Hour')['Target_Price'].mean()\n",
                "plt.figure(figsize=(12, 6))\n",
                "plt.plot(hour_avg.index, hour_avg.values, marker='o', linewidth=2, markersize=6)\n",
                "plt.xlabel('Hour of Day')\n",
                "plt.ylabel('Average Price ($/MWh)')\n",
                "plt.title('Average Prices by Hour of Day')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.xticks(range(0, 24))\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Correlation Analysis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Correlation matrix\n",
                "numeric_columns = ['Target_Price', 'ERCOT.LOAD', 'ERCOT.WIND.GEN', 'Wind Output, % of Load', \n",
                "                   'Wind Output, % of Installed', 'Wind 1-hr MW change', 'Wind 1-hr % change', 'WEST_Load']\n",
                "correlation_matrix = final_dataset[numeric_columns].corr()\n",
                "\n",
                "plt.figure(figsize=(12, 10))\n",
                "sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, \n",
                "           square=True, linewidths=0.5, fmt='.3f')\n",
                "plt.title('Correlation Matrix of Variables')\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Price Spike Analysis"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Price spike analysis\n",
                "price_thresholds = [50, 100, 200, 500, 1000]\n",
                "spike_analysis = []\n",
                "\n",
                "for threshold in price_thresholds:\n",
                "    spike_count = len(final_dataset[final_dataset['Target_Price'] > threshold])\n",
                "    spike_percentage = (spike_count / len(final_dataset)) * 100\n",
                "    avg_spike_price = final_dataset[final_dataset['Target_Price'] > threshold]['Target_Price'].mean()\n",
                "    spike_analysis.append({\n",
                "        'Threshold': threshold,\n",
                "        'Count': spike_count,\n",
                "        'Percentage': spike_percentage,\n",
                "        'Avg_Price': avg_spike_price\n",
                "    })\n",
                "\n",
                "spike_df = pd.DataFrame(spike_analysis)\n",
                "print(\"PRICE SPIKE ANALYSIS:\")\n",
                "print(spike_df.to_string(index=False))\n",
                "\n",
                "# Visualize price spikes\n",
                "plt.figure(figsize=(12, 6))\n",
                "plt.bar(spike_df['Threshold'].astype(str), spike_df['Percentage'], color='red', alpha=0.7)\n",
                "plt.xlabel('Price Threshold ($/MWh)')\n",
                "plt.ylabel('Percentage of Hours (%)')\n",
                "plt.title('Percentage of Hours Above Price Thresholds')\n",
                "plt.grid(True, alpha=0.3)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Feature Relationships"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Feature relationships\n",
                "fig, axes = plt.subplots(2, 2, figsize=(15, 10))\n",
                "fig.suptitle('Feature Relationships with Target Price', fontsize=16, fontweight='bold')\n",
                "\n",
                "# Wind Generation vs Price\n",
                "axes[0, 0].scatter(final_dataset['ERCOT.WIND.GEN'], final_dataset['Target_Price'], alpha=0.5, s=1)\n",
                "axes[0, 0].set_xlabel('Wind Generation (MW)')\n",
                "axes[0, 0].set_ylabel('Target Price ($/MWh)')\n",
                "axes[0, 0].set_title('Wind Generation vs Price')\n",
                "axes[0, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# Load vs Price\n",
                "axes[0, 1].scatter(final_dataset['ERCOT.LOAD'], final_dataset['Target_Price'], alpha=0.5, s=1)\n",
                "axes[0, 1].set_xlabel('ERCOT Load (MW)')\n",
                "axes[0, 1].set_ylabel('Target Price ($/MWh)')\n",
                "axes[0, 1].set_title('Load vs Price')\n",
                "axes[0, 1].grid(True, alpha=0.3)\n",
                "\n",
                "# Wind % of Load vs Price\n",
                "axes[1, 0].scatter(final_dataset['Wind Output, % of Load'], final_dataset['Target_Price'], alpha=0.5, s=1)\n",
                "axes[1, 0].set_xlabel('Wind Output (% of Load)')\n",
                "axes[1, 0].set_ylabel('Target Price ($/MWh)')\n",
                "axes[1, 0].set_title('Wind Penetration vs Price')\n",
                "axes[1, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# WEST Load vs Price\n",
                "axes[1, 1].scatter(final_dataset['WEST_Load'], final_dataset['Target_Price'], alpha=0.5, s=1)\n",
                "axes[1, 1].set_xlabel('WEST Load (MW)')\n",
                "axes[1, 1].set_ylabel('Target Price ($/MWh)')\n",
                "axes[1, 1].set_title('WEST Load vs Price')\n",
                "axes[1, 1].grid(True, alpha=0.3)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Feature Distributions"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Feature distributions\n",
                "fig, axes = plt.subplots(2, 2, figsize=(15, 10))\n",
                "fig.suptitle('Feature Distributions', fontsize=16, fontweight='bold')\n",
                "\n",
                "# Wind Generation\n",
                "axes[0, 0].hist(final_dataset['ERCOT.WIND.GEN'], bins=50, alpha=0.7, color='green', edgecolor='black')\n",
                "axes[0, 0].set_xlabel('Wind Generation (MW)')\n",
                "axes[0, 0].set_ylabel('Frequency')\n",
                "axes[0, 0].set_title('Wind Generation Distribution')\n",
                "axes[0, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# Load\n",
                "axes[0, 1].hist(final_dataset['ERCOT.LOAD'], bins=50, alpha=0.7, color='blue', edgecolor='black')\n",
                "axes[0, 1].set_xlabel('ERCOT Load (MW)')\n",
                "axes[0, 1].set_ylabel('Frequency')\n",
                "axes[0, 1].set_title('Load Distribution')\n",
                "axes[0, 1].grid(True, alpha=0.3)\n",
                "\n",
                "# Wind % of Load\n",
                "axes[1, 0].hist(final_dataset['Wind Output, % of Load'], bins=50, alpha=0.7, color='purple', edgecolor='black')\n",
                "axes[1, 0].set_xlabel('Wind Output (% of Load)')\n",
                "axes[1, 0].set_ylabel('Frequency')\n",
                "axes[1, 0].set_title('Wind Output % of Load Distribution')\n",
                "axes[1, 0].grid(True, alpha=0.3)\n",
                "\n",
                "# WEST Load\n",
                "axes[1, 1].hist(final_dataset['WEST_Load'], bins=50, alpha=0.7, color='red', edgecolor='black')\n",
                "axes[1, 1].set_xlabel('WEST Load (MW)')\n",
                "axes[1, 1].set_ylabel('Frequency')\n",
                "axes[1, 1].set_title('WEST Load Distribution')\n",
                "axes[1, 1].grid(True, alpha=0.3)\n",
                "\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Summary and Key Insights"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"FINAL DATASET SUMMARY:\")\n",
                "print(\"=\" * 50)\n",
                "print(f\"Dataset Shape: {final_dataset.shape}\")\n",
                "print(f\"Date Range: {final_dataset['Hour Ending'].min()} to {final_dataset['Hour Ending'].max()}\")\n",
                "print(f\"Total Hours: {len(final_dataset):,}\")\n",
                "print(f\"Years: {final_dataset['Year'].nunique()}\")\n",
                "print()\n",
                "\n",
                "print(\"TARGET PRICE STATISTICS:\")\n",
                "print(\"=\" * 30)\n",
                "print(f\"Mean: ${final_dataset['Target_Price'].mean():.2f}/MWh\")\n",
                "print(f\"Median: ${final_dataset['Target_Price'].median():.2f}/MWh\")\n",
                "print(f\"Std Dev: ${final_dataset['Target_Price'].std():.2f}/MWh\")\n",
                "print(f\"Min: ${final_dataset['Target_Price'].min():.2f}/MWh\")\n",
                "print(f\"Max: ${final_dataset['Target_Price'].max():.2f}/MWh\")\n",
                "print()\n",
                "\n",
                "print(\"PRICE SPIKE OPPORTUNITIES:\")\n",
                "print(\"=\" * 30)\n",
                "for _, row in spike_df.iterrows():\n",
                "    print(f\"${row['Threshold']}+ prices: {row['Count']:,} hours ({row['Percentage']:.1f}%)\")\n",
                "print()\n",
                "\n",
                "print(\"KEY FEATURES AVAILABLE:\")\n",
                "print(\"=\" * 25)\n",
                "for col in final_dataset.columns:\n",
                "    if col not in ['Hour Ending', 'DeliveryDate', 'DayOfWeek', 'Month', 'Year', 'Hour']:\n",
                "        print(f\"- {col}\")\n",
                "\n",
                "print(\"\\nThis dataset is ready for LSTM model training with multiple features!\")\n",
                "print(\"Key advantages over preliminary data:\")\n",
                "print(\"- 3 years of data vs limited period\")\n",
                "print(\"- Multiple features (wind, load, wind penetration)\")\n",
                "print(\"- Rich feature engineering already done\")\n",
                "print(\"- Clear price spike patterns for arbitrage opportunities\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Write the notebook to file
with open('notebooks/final_dataset_eda.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook created successfully: notebooks/final_dataset_eda.ipynb") 