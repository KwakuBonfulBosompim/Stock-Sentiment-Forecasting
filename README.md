# Stock Price Forecasting with Sentiment Analysis

## Overview

This project predicts Apple’s stock closing price using historical price data combined with news sentiment scores derived from VADER sentiment analysis.

## Data

- Stock data: Historical daily prices and volume  
- Sentiment data: News headlines sentiment scores

## Features

- Price features: Open, High, Low, Close, Volume  
- Sentiment: VADER compound scores

## Models Used

- Random Forest Regressor  
- ARIMA with sentiment as exogenous variable

## Results

| Model         | RMSE   | R² Score |
|---------------|--------|----------|
| Random Forest | 25.73  | -0.018   |
| ARIMA         | 28.82  | -0.29    |

## How to Run

1. Clone the repo  
2. Install requirements:  
   ```bash
   pip install -r requirements.txt
