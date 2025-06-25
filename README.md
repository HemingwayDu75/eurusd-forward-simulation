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

The forward rate is computed using the formula:

