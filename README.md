# NSE Market Risk Analytics Platform

## Executive Summary

The NSE Market Risk Analytics Platform is an end-to-end portfolio risk management and analytics solution built using Python, Databricks, dbt, and Power BI.

The platform ingests historical market data for NSE-listed equities, computes portfolio risk metrics, performs portfolio optimization using Modern Portfolio Theory, and delivers executive-level risk dashboards for portfolio monitoring and investment decision-making.

The solution follows a Medallion Architecture (Raw → Bronze → Silver → Gold) implemented using Databricks and dbt, providing a production-style analytics pipeline commonly used in institutional asset management environments.

---

## Business Problem

Portfolio managers and investment analysts must continuously evaluate risk-adjusted performance, monitor downside risk, and optimize asset allocation decisions.

Traditional spreadsheet-based workflows often suffer from:

* Manual processing
* Limited scalability
* Data quality challenges
* Lack of reproducibility
* Poor governance

This project demonstrates how modern analytics engineering practices can be applied to portfolio risk management using automated pipelines and business intelligence reporting.

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Platform

* Databricks
* Delta Lake

### Analytics Engineering

* dbt Core
* Medallion Architecture

### Business Intelligence

* Power BI

### Version Control

* Git
* GitHub

---

## Key Risk Metrics

The platform calculates:

* Daily Returns
* Log Returns
* Annualized Volatility
* Historical Value-at-Risk (VaR)
* Conditional Value-at-Risk (CVaR)
* Sharpe Ratio
* Maximum Drawdown
* Correlation Analysis
* Portfolio Optimization
* Efficient Frontier

---

## Project Architecture

NSE Market Data

↓

Python Data Ingestion

↓

Databricks Raw Layer

↓

dbt Bronze Layer

↓

dbt Silver Layer

↓

dbt Gold Layer

↓

Power BI Dashboard

---

## dbt Medallion Architecture

### Bronze Layer

Data standardization and cleansing

Models:

* bronze_nse_stock_prices

### Silver Layer

Business-ready transformations

Models:

* silver_daily_returns
* silver_rolling_volatility

### Gold Layer

Executive and portfolio risk reporting

Models:

* gold_risk_summary
* gold_portfolio_metrics

---

## Dashboard Pages

### Page 1 — Executive Risk Overview

KPIs:

* Annual Return
* Annual Volatility
* Sharpe Ratio
* VaR 95%
* CVaR 95%
* Maximum Drawdown

### Page 2 — Portfolio Optimization

Visuals:

* Efficient Frontier
* Maximum Sharpe Portfolio
* Minimum Variance Portfolio

### Page 3 — Market Risk Analytics

Visuals:

* Rolling Volatility
* Drawdown Analysis
* Return Distribution

### Page 4 — Diversification Analysis

Visuals:

* Portfolio Allocation
* Stock Return Comparison

---

## Portfolio Optimization

The platform generates 10,000 simulated portfolios to identify:

### Maximum Sharpe Portfolio

Portfolio with the highest risk-adjusted return.

### Minimum Variance Portfolio

Portfolio with the lowest overall volatility.

### Efficient Frontier

Risk-return combinations representing optimal portfolio allocations.

---

## Key Outcomes

* Automated market risk analytics pipeline
* Production-style dbt implementation
* Portfolio optimization framework
* Executive-level Power BI dashboard
* Institutional asset management use case
* End-to-end analytics engineering workflow

---

## Future Enhancements

Planned enhancements include:

* Beta Analysis
* Alpha Analysis
* Information Ratio
* Sortino Ratio
* Calmar Ratio
* ESG Portfolio Screening
* Sector Allocation Analytics
* Real-Time Market Data Integration

---

## Author

G Aresh

MBA Candidate (2027)

Asset Management | Risk Analytics | Data Analytics | Analytics Engineering

Target Roles:

* Goldman Sachs New Analyst
* Asset Management Analyst
* Risk Analyst
* Investment Analytics
* Portfolio Analytics
