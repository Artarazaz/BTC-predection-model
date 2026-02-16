# Binance BTCUSDT Historical Data (1m & 1h)

Clean, gap-free historical OHLCV data for **BTC/USDT** from Binance (Spot).  
Ideal for machine learning, trading strategy backtesting, and price prediction models.

## Key Features

- **Source**: Binance (via CryptoDataDownload & data.binance.vision)
- **Symbol**: BTCUSDT
- **Timeframes**:
  - 1-minute (yearly CSV files 2020–2026)
  - 1-hour
  - Daily
- **Period**: 2020 → February 2026 (continuously updated)
- **Columns**:
  - Unix timestamp
  - Date (UTC)
  - Symbol
  - Open / High / Low / Close
  - Volume BTC
  - Volume USDT
  - Trade count

High-quality data, no gaps, directly sourced from Binance.

## Folder Structure

```
├── data/
│   ├── minute/               # yearly CSV files (~50–85 MB each)
│   ├── daily/                # daily CSV file
│   └── hourly/
│       └── Binance_BTCUSDT_1h.csv
├── notebooks/                # Jupyter notebooks and python files for analysis and modeling
├── LICENSE/
├── requirements.txt
└── README.md
```

**Note**: Large minute files are tracked with Git LFS or can be downloaded directly from the sources.

## Quick Start

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Load data example
   ```python
   import pandas as pd

   df = pd.read_csv("data/hourly/Binance_BTCUSDT_1h.csv",
                    parse_dates=["Date"], index_col="Date")
   print(df.head())
   ```

## Project Goals

- Prepare clean time-series dataset for ML models (LSTM, Transformer, XGBoost, ...)
- Engineer technical indicators (RSI, MACD, EMA, Bollinger Bands, volume features, ...)
- Backtest trading strategies
- Future: integrate news / sentiment data

## Current Status (February 2026)

- Data updated up to 2026-02-16
- Exploration & feature engineering notebooks in progress
- Baseline model coming soon

## License

MIT License

## Useful Links

- [CryptoDataDownload – Binance](https://www.cryptodatadownload.com/data/binance/)
- [Binance Historical Data](https://data.binance.vision/)
- [CCXT](https://github.com/ccxt/ccxt) – for live data
- [pandas-ta](https://github.com/twopirllc/pandas-ta) – technical indicators

Contributions, issues, and stars are welcome! 🚀
