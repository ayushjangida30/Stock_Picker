import yfinance as yf
import pandas as pd

def check_stock_52_week_high(last_close_price, close_price_52_week):
    return last_close_price >= close_price_52_week.max()

df = pd.read_csv('./tse_stocks.csv')
symbol = df['stock_symbol'].astype(str).tolist()


failed_tickers = [
    'DSV', 'INE', 'WJX', 'FRU', 'TBL', 'WTE', 'MATR', 'EMA', 'SVI', 'CVO', 'AYA', 'GWO', 'KEL', 'GGD', 'TNZ', 'POU', 'WSP', 'GUD', 'SDE', 'DND', 'DXT', 'MNT', 'AII', 'ATZ', 'ECN', 'SYZ', 'NPI', 'HAI', 'CKI', 'SOY', 'FEC', 'CPH', 'DR', 'EQB', 'ORE', 'RUS', 'ISV', 'CXB', 'BLN', 'KEC', 'MEQ', 'PXT', 'ADEN', 'CFP', 'SIA', 'GCG', 'CGX', 'PNE', 'NWC', 'CGI', 'SGY', 'PMET', 'CTC', 'RUP', 'ALS', 'BDT', 'DSG', 'BDI', 'KRR', 'PRB', 'KBL', 'TWC', 'IVN', 'FIL', 'CPX', 'DRX', 'EFN', 'MTY', 'AFN', 'EXE', 'PLC', 'HWX', 'SEC', 'LUG', 'ARG', 'DRM', 'VLE', 'MAL', 'CU', 'MXG', 'ABX', 'EIF', 'MRE', 'ATD', 'WN', 'MRD', 'CURA', 'CJT', 'IFC', 'RCH', 'TOU', 'FFH', 'CGY', 'WCP', 'TOY', 'FVI', 'CGG', 'FCU', 'TVK', 'NGT', 'DBM', 'AAV', 'UNC', 'FVL', 'SRU.UN', 'MND', 'DFY', 'HTL', 'LUN', 'PRL', 'FFN', 'OLY', 'QRC', 'MDA', 'SFC', 'KNT', 'KXS', 'LNF', 'WPK', 'IFP', 'MDI', 'FTN', 'VNP', 'BBD.B', 'NFI', 'SBC', 'HRX', 'SIS', 'SPLT', 'URC', 'PIF', 'ALA', 'ACQ', 'OLA', 'CCL.B', 'NDM', 'IMG', 'URB', 'TIH', 'LNR', 'DML', 'TF', 'STLC', 'ARX', 'WDO', 'REI.UN', 'TCW', 'AOI', 'GEI', 'SFTC', 'MRU', 'BIR', 'RAY.B', 'FAR', 'XTC', 'CFW', 'MKP', 'FOM', 'THNC', 'BDGI', 'CAR.UN', 'GIVX', 'HR.UN', 'MRG.UN', 'SCR', 'PRYM', 'GCG.A', 'BBD.A', 'CS', 'GIB.A', 'TA', 'CUP.U', 'LIRC', 'DTOL', 'TCL.B', 'TPX.B', 'DHT.UN', 'U.UN', 'WILD', 'ERE.UN', 'PLZ.UN', 'AP.UN', 'EMP.A', 'AND', 'TECK.A', 'ONEX', 'TECK.B', 'CJ', 'KITS', 'LAS.A', 'PKI', 'CAS', 'GDI', 'CSW.B', 'DPM', 'HOM.U', 'QBR.B', 'JAG', 'NGEX', 'CPLF', 'AD.UN', 'FCR.UN', 'APR.UN', 'AGF.B', 'ZCPB', 'NWH.UN', 'CCA', 'PRV.UN', 'MTL', 'RPI.UN', 'DII.B', 'NXR.UN', 'MRT.UN', 'DNTL', 'GRA', 'TSND', 'IIP.UN', 'AAUC', 'CRR.UN', 'GMIN', 'MI.UN', 'BBU.UN', 'RAY.A', 'IPCO', 'TSU', 'FIH.U', 'GLXY', 'DHT.U', 'ATRL', 'SOLG', 'CHP.UN', 'KMP.UN', 'CNR', 'QBTC', 'CTC.A', 'GTWO', 'HPS.A', 'CRT.UN', 'BANK', 'ENGH', 'BPF.UN', 'BEI.UN', 'HOM.UN', 'FTT', 'ACO.X', 'RCI.B', 'ACO.Y', 'BEP.UN', 'URB.A', 'MARI', 'CCL.A', 'QSP.UN', 'AW.UN', 'QBR.A', 'BIP.UN', 'D.UN', 'ATH', 'CSW.A', 'MHC.U', 'PMZ.UN', 'TOT', 'TCL.A', 'FCD.UN', 'FRX', 'KSI', 'GBT', 'GRT.UN', 'SGR.UN', 'AX.UN', 'DIR.UN', 'BTB.UN', 'CSU', 'CSH.UN', 'CHE.UN', 'LIF', 'CNL', 'NVA', 'MFI', 'LB', 'POW', 'CEU', 'AIDX', 'RCI.A'
    # (continue the list with all failed tickers)
]


valid_symbols = [ticker for ticker in symbol if ticker not in failed_tickers]


# Fetch historical data for the list of tickers
data = yf.download(valid_symbols, start='2023-01-01', end='2024-09-10')

close_prices = data['Close']

list_of_52_week_high_stocks = []

for stock in close_prices.columns:
    # Get the past 252 days' closing prices for the current stock
    close_price_52_week = close_prices[stock][-252:]
    
    # Get the last closing price
    last_close_price = close_prices[stock].iloc[-1]
    
    # Check if the last closing price is at or above the 52-week high
    is_at_52_week_high = check_stock_52_week_high(last_close_price, close_price_52_week)
    
    if is_at_52_week_high:
        list_of_52_week_high_stocks.append(stock)

print(list_of_52_week_high_stocks)





















# close_prices = data['Close']
# close_price_52_week = data['Close'][-252:]
# last_close_price = close_prices.iloc[-1]

# check_stock_52_week_high(last_close_price, close_price_52_week)


# print(last_close_price)

# last_close_price = close_prices.iloc[-1]
# stocks_above_10 = last_close_price[last_close_price >= 10].index


# filtered_data = data.loc[:, (data.columns.get_level_values(1).isin(stocks_above_10))]


# close_prices_ = filtered_data['Close']
# high_52_week = calculate_52_week_high(close_prices_)
# latest_prices = close_prices_.iloc[-1]
# latest_52_week_highs = high_52_week.iloc[-1]
# at_or_above_52_week_high = latest_prices >= latest_52_week_highs

# symbols_at_or_above_52_week_high = at_or_above_52_week_high[at_or_above_52_week_high].index

# print("Symbols at or above 52-week high:")
# for symbol in filtered_data:
#     print(symbol)

