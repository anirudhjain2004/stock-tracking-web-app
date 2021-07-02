# Stock Analysis Web Application (Basic)
A web-application to obtain basic information about any S&P500 company and analyze it's stock using historical prices. 

[Click here to check the demo Website](https://share.streamlit.io/anirudhjain2004/stock-tracking-web-app/app.py)

![Capture](https://user-images.githubusercontent.com/77311854/114436486-fe856000-9be2-11eb-9267-018a12f62cf3.PNG)


## Linked File(s): 
1. ticker-data.csv (csv file containing list of stock tickers of companies in the S&P500 index)


## Modules used:
1. Streamlit (for creating simple web app)
2. YFinance (for obtaining stock data)
3. Pandas (for management of data)
4. Datetime
5. Cufflinks (for data visualisation/ plotting graphs)


## Stock Information Obtained (using it's Ticker):
![Capture1](https://user-images.githubusercontent.com/77311854/114436632-31c7ef00-9be3-11eb-8055-03c636189777.PNG)

1. Company name
2. Company Logo
3. Company Description
4. Historical Stock Prices (High,Low,Open,Close,20-Day moving avg)
5. Stock Trading volume
6. Dividend history + Stock-split history
7. Bollinger Bands

![Capture2](https://user-images.githubusercontent.com/77311854/114436629-312f5880-9be3-11eb-96da-9bc2e10d1f9b.PNG)



## Run the following code after downloading the 'requirements.txt' to download the pre-requisites:

```
$ pip install -r requirements.txt
```
Ensure pip is added to the PATH
Ensure requirements.txt is downloaded in the right directory


## Launch a Streamlit app (app.py) by running the following query in the command prompt:

```
$ streamlit run app.py
```



### Created By: Anirudh Jain
