'''MADE BY: ANIRUDH JAIN
CODE CREDITS: DATA PROFESSOR (https://github.com/dataprofessor/stock-app)
DATE: 12th April 2021
DESCRIPTION: WEB-APP FOR STOCK ANALYSIS (S&P500 stocks)
MAIN MODULES USED: YFINANCE AND STREAMLIT
'''

## CHANGE THIS PATH 
filePath = "ticker-data.csv"
## CHANGE THIS PATH 


comment1 = '''IMPORTS'''
###################################################
###################################################

import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
from datetime import date
###################################################
###################################################


comment2 = '''APP INTRO'''
###################################################
###################################################
###################################################

# App title
st.markdown('''
# Astrapia - a stock tracking web app
Shown are the stock price data for query companies!
''')
st.write('---')

###################################################
###################################################
###################################################



comment3 = '''SIDEBAR'''
###################################################
###################################################
###################################################
# Heading
st.sidebar.subheader('Query parameters')

# Retrieving tickers data
ticker_list = pd.read_csv(filePath,usecols = ['Symbol'])
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list['Symbol']) # selecting ticker symbol
tickerData = yf.Ticker(tickerSymbol) # getting ticker data from yahoo finance


# Desired Time Period of Stock Data
todays_date = date.today()      # setting today's date as default end date and first day of this year as default start date
start_date = st.sidebar.date_input("Start date", date(todays_date.year, 1, 1))
end_date = st.sidebar.date_input("End date", todays_date)


###################################################
###################################################
###################################################




comment4 = '''BASIC TICKER INFO: LOGO, NAME, DESCRIPTION'''
###################################################
###################################################
###################################################



# Ticker information
company_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(company_logo, unsafe_allow_html=True)

company_name = tickerData.info['longName']
st.header('**%s**' % company_name)

company_summary = tickerData.info['longBusinessSummary']
st.info(company_summary)


###################################################
###################################################
###################################################




comment5 = '''HISTORICAL PRICE DATA (OPEN,CLOSE,HIGH,LOW,VOLUME,DIVIDENDS,SPLITS)'''
###################################################
###################################################
###################################################


# Ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #getting the historical prices for this ticker
st.header('**Ticker data**')
st.write(tickerDf)



###################################################
###################################################
###################################################



comment6 = '''BOLINGER BANDS'''
###################################################
###################################################
###################################################



# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title=  company_name,legend='top',name='Candle Graph')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
st.write('---')


###################################################
###################################################
###################################################




comment7 = '''LIST OF ALL COMPANIES (S&P500)'''
###################################################
###################################################
###################################################

st.markdown("""
# List of S&P500 Companies""")
ticker_list_demo = pd.read_csv(filePath)
st.write(ticker_list_demo)


###################################################
###################################################
###################################################
