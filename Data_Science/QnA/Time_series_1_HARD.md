# Advanced Time Series Analysis – 10 Toughest Questions and Answers

## 1. What is stationarity in time series, and why is it important?
**Answer:**  
A time series is **stationary** if its statistical properties (mean, variance, autocorrelation) are **constant over time**.  
Most forecasting models (ARIMA, SARIMA) assume stationarity.  
Non-stationary data can produce **spurious correlations** and unreliable forecasts.  
Use **ADF or KPSS test** to check for stationarity.

---

## 2. How do you make a non-stationary time series stationary?
**Answer:**  
Common techniques:
- **Differencing** (e.g., subtracting lagged values)
- **Log transformation** (stabilizes variance)
- **Detrending** or **removing seasonality**  
Sometimes a combination of methods (e.g., seasonal differencing) is required.

---

## 3. What is autocorrelation and partial autocorrelation, and how are they used?
**Answer:**  
- **Autocorrelation (ACF)**: Correlation of time series with its lagged values  
- **Partial Autocorrelation (PACF)**: Correlation at a given lag, removing effects of shorter lags  
Used to identify order parameters in **AR(p), MA(q)** models:
- ACF tailing off, PACF cutting off → AR  
- ACF cutting off, PACF tailing off → MA

---

## 4. How does ARIMA modeling work, and what do its parameters (p, d, q) represent?
**Answer:**  
**ARIMA(p, d, q)**:
- `p`: Order of autoregression (AR)
- `d`: Degree of differencing (for stationarity)
- `q`: Order of moving average (MA)  
ARIMA models past lags and forecast errors. Fit with tools like **auto_arima** to select optimal parameters.

---

## 5. Why is cross-validation tricky in time series, and how can it be done properly?
**Answer:**  
Time series data is **not i.i.d.** — observations are **temporally dependent**.  
Don't randomly split data. Use:
- **TimeSeriesSplit**
- **Rolling window validation**
- **Walk-forward validation**  
These respect temporal order and avoid **look-ahead bias**.

---

## 6. What is seasonality, and how is it handled in models?
**Answer:**  
Seasonality is a **repeating pattern** at fixed intervals (e.g., weekly, yearly).  
Handled by:
- **Seasonal differencing**
- Including **seasonal dummies**
- Using models like **SARIMA**, **Prophet**, or **ETS** that handle seasonality explicitly.

---

## 7. How do you deal with missing values in time series?
**Answer:**  
Options:
- **Forward/backward fill** (assumes continuity)
- **Linear/Polynomial interpolation**
- **Kalman filtering** or **EM algorithm**
- Use models that can handle missingness (e.g., certain RNNs)  
Method depends on **missingness pattern** and data characteristics.

---

## 8. What are the key differences between ARIMA, SARIMA, and Prophet?
**Answer:**  
- **ARIMA**: Captures trend and autocorrelation, needs stationary data  
- **SARIMA**: ARIMA + seasonal component  
- **Prophet** (by Facebook): Handles trend, seasonality, holidays automatically, robust to missing data and outliers  
Prophet is more **automated**; ARIMA/SARIMA offers **fine control**.

---

## 9. How do you detect and handle concept drift in time series forecasting?
**Answer:**  
**Concept drift** occurs when the underlying data generation process changes over time.  
Detection:
- Model performance degrades  
- Statistical tests show parameter shifts  
Handling:
- Retrain models regularly  
- Use **sliding windows**, **online learning**, or **adaptive models**

---

## 10. How do exogenous variables (X) integrate into time series forecasting?
**Answer:**  
Incorporated in models like:
- **ARIMAX**: ARIMA + exogenous regressors  
- **SARIMAX**, **VARX**, **XGBoost with lags**  
Exogenous features help explain variance and improve forecasting.  
Ensure they are **known ahead of time** for forecasting use.
