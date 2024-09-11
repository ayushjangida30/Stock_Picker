import yfinance as yf
import pandas as pd

fast_period = 20   # Fast EMA period
slow_period = 35  # Slow EMA period
signal_period = 10 # Signal line period

def compute_ema(series, period):
    """Compute Exponential Moving Average (EMA)"""
    return series.ewm(span=period, adjust=False).mean()

def compute_macd(close_prices, fast_period=fast_period, slow_period=slow_period, signal_period=signal_period):
    """Compute MACD line, Signal line, and MACD Histogram"""
    # Compute Fast and Slow EMAs
    fast_ema = compute_ema(close_prices, fast_period)
    slow_ema = compute_ema(close_prices, slow_period)
    
    # Compute MACD Line
    macd_line = fast_ema - slow_ema
    
    # Compute Signal Line
    signal_line = compute_ema(macd_line, signal_period)
    
    return macd_line, signal_line

def identify_buy_signals(macd_line, signal_line):
    """Identify buy signals when MACD line crosses above the Signal line"""
    # Create a DataFrame to store MACD and Signal line
    df = pd.DataFrame({
        'MACD_Line': macd_line,
        'Signal_Line': signal_line
    })
    
    # Create a column to store buy signals
    df['Buy_Signal'] = (df['MACD_Line'] > df['Signal_Line']) & (df['MACD_Line'].shift(1) <= df['Signal_Line'].shift(1))
    
    return df[df['Buy_Signal']]

df = pd.read_csv('./tse_stocks.csv')
symbol = df['stock_symbol'].astype(str).tolist()


failed_tickers = [
    'DSV', 'INE', 'WJX', 'FRU', 'TBL', 'WTE', 'MATR', 'EMA', 'SVI', 'CVO', 'AYA', 'GWO', 'KEL', 'GGD', 'TNZ', 'POU', 'WSP', 'GUD', 'SDE', 'DND', 'DXT', 'MNT', 'AII', 'ATZ', 'ECN', 'SYZ', 'NPI', 'HAI', 'CKI', 'SOY', 'FEC', 'CPH', 'DR', 'EQB', 'ORE', 'RUS', 'ISV', 'CXB', 'BLN', 'KEC', 'MEQ', 'PXT', 'ADEN', 'CFP', 'SIA', 'GCG', 'CGX', 'PNE', 'NWC', 'CGI', 'SGY', 'PMET', 'CTC', 'RUP', 'ALS', 'BDT', 'DSG', 'BDI', 'KRR', 'PRB', 'KBL', 'TWC', 'IVN', 'FIL', 'CPX', 'DRX', 'EFN', 'MTY', 'AFN', 'EXE', 'PLC', 'HWX', 'SEC', 'LUG', 'ARG', 'DRM', 'VLE', 'MAL', 'CU', 'MXG', 'ABX', 'EIF', 'MRE', 'ATD', 'WN', 'MRD', 'CURA', 'CJT', 'IFC', 'RCH', 'TOU', 'FFH', 'CGY', 'WCP', 'TOY', 'FVI', 'CGG', 'FCU', 'TVK', 'NGT', 'DBM', 'AAV', 'UNC', 'FVL', 'SRU.UN', 'MND', 'DFY', 'HTL', 'LUN', 'PRL', 'FFN', 'OLY', 'QRC', 'MDA', 'SFC', 'KNT', 'KXS', 'LNF', 'WPK', 'IFP', 'MDI', 'FTN', 'VNP', 'BBD.B', 'NFI', 'SBC', 'HRX', 'SIS', 'SPLT', 'URC', 'PIF', 'ALA', 'ACQ', 'OLA', 'CCL.B', 'NDM', 'IMG', 'URB', 'TIH', 'LNR', 'DML', 'TF', 'STLC', 'ARX', 'WDO', 'REI.UN', 'TCW', 'AOI', 'GEI', 'SFTC', 'MRU', 'BIR', 'RAY.B', 'FAR', 'XTC', 'CFW', 'MKP', 'FOM', 'THNC', 'BDGI', 'CAR.UN', 'GIVX', 'HR.UN', 'MRG.UN', 'SCR', 'PRYM', 'GCG.A', 'BBD.A', 'CS', 'GIB.A', 'TA', 'CUP.U', 'LIRC', 'DTOL', 'TCL.B', 'TPX.B', 'DHT.UN', 'U.UN', 'WILD', 'ERE.UN', 'PLZ.UN', 'AP.UN', 'EMP.A', 'AND', 'TECK.A', 'ONEX', 'TECK.B', 'CJ', 'KITS', 'LAS.A', 'PKI', 'CAS', 'GDI', 'CSW.B', 'DPM', 'HOM.U', 'QBR.B', 'JAG', 'NGEX', 'CPLF', 'AD.UN', 'FCR.UN', 'APR.UN', 'AGF.B', 'ZCPB', 'NWH.UN', 'CCA', 'PRV.UN', 'MTL', 'RPI.UN', 'DII.B', 'NXR.UN', 'MRT.UN', 'DNTL', 'GRA', 'TSND', 'IIP.UN', 'AAUC', 'CRR.UN', 'GMIN', 'MI.UN', 'BBU.UN', 'RAY.A', 'IPCO', 'TSU', 'FIH.U', 'GLXY', 'DHT.U', 'ATRL', 'SOLG', 'CHP.UN', 'KMP.UN', 'CNR', 'QBTC', 'CTC.A', 'GTWO', 'HPS.A', 'CRT.UN', 'BANK', 'ENGH', 'BPF.UN', 'BEI.UN', 'HOM.UN', 'FTT', 'ACO.X', 'RCI.B', 'ACO.Y', 'BEP.UN', 'URB.A', 'MARI', 'CCL.A', 'QSP.UN', 'AW.UN', 'QBR.A', 'BIP.UN', 'D.UN', 'ATH', 'CSW.A', 'MHC.U', 'PMZ.UN', 'TOT', 'TCL.A', 'FCD.UN', 'FRX', 'KSI', 'GBT', 'GRT.UN', 'SGR.UN', 'AX.UN', 'DIR.UN', 'BTB.UN', 'CSU', 'CSH.UN', 'CHE.UN', 'LIF', 'CNL', 'NVA', 'MFI', 'LB', 'POW', 'CEU', 'AIDX', 'RCI.A'
    # (continue the list with all failed tickers)
]


valid_symbols = [ticker for ticker in symbol if ticker not in failed_tickers]

data = yf.download(valid_symbols, start='2023-01-01', end='2024-09-10')

close_prices = data['Close']

macd_results = {}

for stock in close_prices.columns:
    # Compute MACD, Signal Line, and Histogram
    macd_line, signal_line = compute_macd(close_prices[stock], fast_period = 20, slow_period = 30, signal_period = 10)

    # Identify buy signals
    buy_signals = identify_buy_signals(macd_line, signal_line)

    print(macd_line)

    # # Store results in dictionary
    # macd_results[stock] = {
    #     'MACD_Line': macd_line,
    #     'Signal_Line': signal_line,
    #     'Buy_Signals': buy_signals
    # }

    # # Print the results
    # print(f"\n{stock}:")
    # print("Buy Signals:")
    # print(macd_results[stock]['Buy_Signals'])