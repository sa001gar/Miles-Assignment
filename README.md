# Python Assignment Solutions

This repository contains solutions to the Python assignment provided by Miles Business India Pvt. Ltd. The assignment includes three questions covering WebSocket connections, data visualization with `matplotlib`, and data manipulation with `pandas`.

## Questions

### 1. **Reading Data from a WebSocket and Storing it in a Tabular Format**

- **Objective**: Implement a Python function that connects to a WebSocket, reads live stock market data in JSON format, and stores it in a CSV file. The solution also handles reconnections if the WebSocket connection is interrupted and batch inserts data for performance optimization.
- **Improvement**: The code is enhanced to:
  - Automatically reconnect if the WebSocket connection drops.
  - Store incoming data in batches to reduce disk writes and improve performance.
  - Use a `while` loop to continuously fetch and store new data even if interruptions occur.

**Code Improvements**:
- Reconnection logic using an `asyncio` loop.
- Batch processing of WebSocket data to optimize CSV writing performance.
- Graceful error handling to ensure the process continues even if some data packets are malformed.

### 2. **Arranging Data Using matplotlib**

- **Objective**: Visualize the daily temperature variations in a city using data stored in a CSV file. The plot should show temperature changes over time, with annotations marking the highest and lowest temperatures.
- **Improvement**: The script is improved to:
  - Parse the date column correctly and format it for use on the x-axis.
  - Handle missing or NaN temperature values gracefully.
  - Annotate the highest and lowest temperature points on the graph to provide better insights.

**Code Improvements**:
- Correct handling of date formatting for matplotlib's x-axis.
- Inclusion of annotations for the highest and lowest temperatures.
- Filtering out NaN values to avoid distortions in the plot.

### 3. **Using pandas for Extensive Data Manipulation**

- **Objective**: Manipulate a sales dataset by grouping data by region, calculating total sales, adding a new column for average price per unit, and filtering rows based on total sales exceeding ₹10,000.
- **Improvement**: The solution is optimized to:
  - Efficiently handle large datasets using `pandas`.
  - Use `groupby` and `agg` functions for performance optimization.
  - Filter rows based on a threshold and handle potential issues with missing or duplicate data.

**Code Improvements**:
- Optimized the data manipulation steps using `pandas` functions for grouping and aggregating sales.
- Ensured that the dataset handles missing or duplicate `product_id` values without crashing.

## Directory Structure
```
- question_01/
  - stock.py
  - stock_data.csv
- question_02/
  - temparature.py
  - temparature_data.csv
- question_03/
  - sales.py
  - sales_data.py

```
## Requirements

```python
pip install -r requirements.txt
```

# Thank You 💕