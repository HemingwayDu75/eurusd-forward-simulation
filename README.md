# eurusd-forward-simulation
Python tool to simulate and visualize EUR/USD forward rate projections under various USD interest rate cut scenarios, using historical dates and user-imported CSV data.
# EUR/USD Forward Rate Simulation

This Python tool allows you to simulate and visualize EUR/USD forward rate projections under various assumptions of USD interest rate cuts. The simulation uses interest rate parity formulas and a user-provided timeline of future dates imported from a CSV file.

## 📌 Purpose

The goal is to assess the impact of different USD interest rate scenarios on the EUR/USD forward rate, based on an initial market configuration. This is particularly useful for financial analysts, traders, or corporate treasurers evaluating FX hedging strategies.

## ⚙️ Features

- Load a list of future value dates from a CSV file
- Simulate forward rates based on interest rate parity formula
- Define scenarios with different levels of USD rate cuts
- Display interactive plots showing forward rate evolution
- Built-in graphical user interface for file selection

## 🧮 Methodology

The forward rate is computed using the formula: Forward = Spot × (1 + r_EUR × Δt) / (1 + r_USD × Δt)


Where:
- `r_EUR` is the current EUR interest rate (default: 4.00%)
- `r_USD` is the current USD interest rate (default: 3.00%)
- `Δt` is the time to maturity in days / 360

## 🖥️ Requirements

- Python 3.8+
- Packages:
  - `pandas`
  - `matplotlib`
  - `tkinter` (built-in with most Python distributions)

Install dependencies (if needed):

```bash
pip install pandas matplotlib

📂 CSV Format
Your input CSV file must contain at least one column named date with dates in the format YYYY-MM-DD.

Example:

date
2024-09-30
2024-10-31
2024-11-29


▶️ How to Use
Run the script.

A file selection dialog will appear.

Choose your CSV file containing the future value dates.

The simulation will generate a plot comparing:

The current forward curve

The forward curves under various USD rate cut scenarios (default: -25bps, -50bps, -100bps)

🧪 Customization
You can modify the following default values directly in the script:

taux_eur = 4.00       # EUR interest rate
taux_us_initial = 3.00  # Initial USD interest rate
spot_eurusd = 1.11667   # Spot EUR/USD rate
start_date = datetime(2024, 8, 27)  # Pricing date
taux_us_baisse_points = [0.25, 0.50, 1.00]  # Simulated rate cuts

