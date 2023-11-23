import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Check which companies' data is available on Yahoo Finance at t2
def check_yahoo_availability(ticker, t1, t2):
    try:
        data = yf.Ticker(ticker).history(start=t1, end=t2)
        latest_date = data.index[-1]
        # print(ticker,latest_date)
        return latest_date
    except:
        # print('false',ticker)
        return None

def map_to_gics(industry):
    industry = industry.strip()  # Remove spaces at the beginning and end
    industry = ' '.join(industry.split())  # Replace multiple spaces with a single space
    # print(industry)
    mapping = {
        'Consumer Staples': ['Tobacco', 'Packaged Foods', 'Beverages—Wineries & Distilleries', 'Food Distribution', 'Household & Personal Products', 'Farm Products'],
        'Financials': ['Capital Markets', 'Credit Services', 'Asset Management', 'Insurance—Property & Casualty', 'Insurance—Specialty', 'Mortgage Finance', 'Rental & Leasing Services', 'Asset Management'],
        'Utilities': ['Utilities—Renewable', 'Solar','Scientific & Technical Instruments'],
        'Information Technology': [
            'Software—Application', 'Computer Hardware',
            'Software—Infrastructure', 'Semiconductors', 'Internet Retail', 'Internet Content & Information',
            'Semiconductor Equipment & Materials',
        ],
        'Health Care': [
            'Biotechnology', 'Medical Devices', 'Health Information Services', 'Medical Care Facilities',
            'Pharmaceutical Retailers', 'Drug Manufacturers—General', 'Diagnostics & Research', 'Healthcare Plans'
        ],
        'Industrials': [
            'Aerospace & Defense', 'Specialty Industrial Machinery', 'Farm & Heavy Construction Machinery',
            'Engineering & Construction', 'Tools & Accessories', 'Airports & Air Services', 'Trucking',
            'Metal Fabrication', 'Pollution & Treatment Controls',
        ],
        'Communication Services': ['Telecom Services', 'Entertainment', 'Electronic Gaming & Multimedia', 'Communication Equipment'],
        'Consumer Discretionary': [
            'Leisure', 'Specialty Business Services',  'Lodging', 'Specialty Retail','Advertising Agencies',
            'Recreational Vehicles',  'Department Stores',
            'Travel Services', 'Gambling','Furnishings', 'Fixtures & Appliances', 'Education & Training Services','Personal Services','Security & Protection Services'
        ],
        'Real Estate': ['Real Estate Services', 'Real Estate—Development'],
        'Materials': ['Chemicals', 'Other Industrial Metals & Mining', 'Packaging & Containers', 'Steel', 'Other Precious Metals & Mining', 'Specialty Chemicals',],
        'Energy': ['Oil & Gas E&P', 'Oil & Gas Midstream'],

        'Electric Vehicle': ['Auto Parts','Auto Manufacturers','Auto & Truck Dealerships','Electrical Equipment & Parts', 'Electronic Components','Information Technology Services',]
    }

    for gics, sub_inds in mapping.items():
        if industry in sub_inds:
            return gics
    print('"{}"'.format(industry))
    return 'Others'

def df_map2gics(df_to_map, df_industry):
    df_to_map.insert(0,'Industry',df_industry['Industry'].values)
    df_to_map.insert(0, 'GICS_Sector', df_to_map['Industry'].apply(map_to_gics))
    df_mapped = df_to_map.groupby('GICS_Sector').mean()
    return df_mapped
