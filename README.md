# AI Challenge

Welcome! you are a super star for making it here. This is your time to shine, an opportunity to show off your skills, understanding and more importantly coding abilities 😉. So relax, grab some coffee / whiskey (depending on time of day) and start developing on this take-home exercise.

We recommend that you implement deep learning models, using PyTorch exclusively for any models you develop

## Setup 💿

1. Clone this repository to your local machine.
2. Install the required Python libraries:

```shell
pip install -r requirements.txt
```

Please feel free to install any other repositories of your choice. For any deep learning implementations, please use [`PyTorch`](https://pytorch.org/)

## Challenge Overview 💪

The challenge is split into two parts, where first part involves the implementation of a model, training it on the data and testing it. Second part involves reporting and analysis, we recommend you create a Jupyter Notebook to showcase your analysis and interpretation of your model performance. The following sections go into greater detail for each of the parts.

### Part 1: Time Series Forecasting
In this part you will:

- Implement a time series forecasting model with a transformer backbone and any prediction head design of your choice. (Implemented yourself, do not use externally implemented models) 
- Train the model on the provided dataset.
- Test the model to evaluate its performance.
- Benchmark your model to predict future trend in different time-windows, Select a time window that performs the best.

---
#### Datasets
There are 2 datasets we have selected for this exercise, feel free to explore and choose the one that you'd like to use.

1. **Yahoo finance stock data**: As the name suggests this is a financial time series dataset. To download it a python script has already been written for you. You can download the data via the following:

```shell
python src/utils/download_yfinance_data.py AAPL
```

This will download the stock data for Apple Inc. (AAPL) from 5 days ago to yesterday in 5-minute intervals, and save it to a CSV file named `AAPL_stock_data.csv`. You can also specify custom dates if needed as shown by the sample command below. Though minimum, 60 days length in 5 minute intervals is what we recommend.

```shell
python src/utils/download_yfinance_data.py AAPL --start_date 2024-05-17 --end_date 2024-05-22 --interval 5m
```

2. **ETT (Electricity Transformer Temperature) [Dataset](https://github.com/zhouhaoyi/ETDataset)**: is designed for long sequence time-series forecasting, covering data from July 2016 to July 2018. It includes datasets for small, large, and full scales, containing measurements such as load and oil temperature for multiple transformer stations. Obviously for this use case, **only focus on the small version of the data**. To download it a python script has already been written for you. You can download the data via the following:

```shell
python src/utils/download_ett_small.py
```

This will download the four CSV files `(ETTh1.csv, ETTh2.csv, ETTm1.csv, ETTm2.csv)` from the specified [GitHub repository](https://github.com/zhouhaoyi/ETDataset) and save them in the `ETT-small` directory. Adjust the script if you need to download files from different locations or add additional functionality.

---

### Part 2: Interpretability & Reporting
In this part, you will:

- Analyse the performance of your model.
- Interpret the results and provide insights.
- Document your analysis and findings in a Jupyter Notebook, including visualizations and detailed explanations.

## What we'd like to see 🙀
We'd like to see:

- Effective use of deep learning models, innovative learning strategies and monitoring techniques, implemented exclusively in PyTorch.
- Clear and concise code, with appropriate comments and documentation. Please share your results in a github repository with instructions on how to run and reproduce your results.
- Analysis and interpretation of your model's performance.
- Insightful visualisations that help explain your results and findings.

## What you'd be assessed on 🔎

You will be assessed on:

- Model Implementation: How well you implement the time series forecasting model using PyTorch.
- Performance: The accuracy and reliability of your model on the test data.
- Analysis: The depth and clarity of your analysis in the Jupyter Notebook.
- Interpretability: How well you interpret and explain the results of your model.
- Code Quality: The readability, organization, and documentation of your code.
- Visualizations: The effectiveness of your visualizations in conveying your findings.

Good luck, and we look forward to seeing your work!

## Additional support 🤝
If you have any questions, or need further clarification of any of the challenges. 

Then please reach out to: 
📣 nick@kashmirintelligence.com 📣
