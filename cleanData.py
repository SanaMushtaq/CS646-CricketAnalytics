from getCountryCode import *

import pandas as pd


class CleanData():

    def clean(self, country, df):
        df.columns = ['Team', 'Result', 'Margin', 'Toss', 'Bat', 'Opposition', 'Ground', 'Date']

        df.loc[df['Result'] == 'won', 'Result'] = 1
        df.loc[df['Result'] == 'lost', 'Result'] = 0

        indexNames = df[df['Result'] == 'aban'].index
        df.drop(indexNames, inplace=True)
        indexNames = df[df['Result'] == 'n/r'].index
        df.drop(indexNames, inplace=True)
        indexNames = df[df['Result'] == 'tied'].index
        df.drop(indexNames, inplace=True);
        indexNames = df[df['Result'] == 'canc'].index
        df.drop(indexNames, inplace=True)

        df.loc[df['Toss'] == 'won', 'Toss'] = 1
        df.loc[df['Toss'] == 'lost', 'Toss'] = 0

        df.loc[df['Bat'] == '1st', 'Bat'] = 1
        df.loc[df['Bat'] == '2nd', 'Bat'] = 0

        countryCode = getCountryCode(country)
        if countryCode == '1':
            # IND=1, AUS=2, PAK=3, NZ=4, SA=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 1
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 2
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 5
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True)
            indexNames = df[df['Opposition'] == 10].index
            df.drop(indexNames, inplace=True)

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'East London', 'Ground'] = 1
            df.loc[df['Ground'] == 'The Oval', 'Ground'] = 1
            df.loc[df['Ground'] == 'Lord\'s', 'Ground'] = 1
            df.loc[df['Ground'] == 'Manchester', 'Ground'] = 1
            df.loc[df['Ground'] == 'Chester-le-Street', 'Ground'] = 1
            df.loc[df['Ground'] == 'Birmingham', 'Ground'] = 1
            df.loc[df['Ground'] == 'Nottingham', 'Ground'] = 1
            df.loc[df['Ground'] == 'Bristol', 'Ground'] = 1
            df.loc[df['Ground'] == 'Leeds', 'Ground'] = 1
            df.loc[df['Ground'] == 'Southampton', 'Ground'] = 1
            df.loc[df['Ground'] == 'Cardiff', 'Ground'] = 1
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True)

        if countryCode == '2':
            # IND=1, ENG=2, PAK=3, NZ=4, SA=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Brisbane', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Sydney', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Adelaide', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Perth', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Melbourne', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Hobart', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Canberra', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        if countryCode == '3':
            # IND=1, ENG=2, PAK=3, NZ=4, AUS=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Johannesburg', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Bloemfontein', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Cape Town', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Durban', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Port Elizabeth', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Potchefstroom', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Benoni', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Centurion', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Kimberley', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Paarl', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        if countryCode == '4':
            # IND=1, ENG=2, PAK=3, NZ=4, AUS=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

        if countryCode == '5':
            # IND=1, ENG=2, PAK=3, SA=4, AUS=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Auckland', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Taupo', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Napier', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Wellington', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Christchurch', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Dunedin', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Queenstown', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Hamilton', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Mount Maunganui', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Whangarei', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Nelson', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        if countryCode == '6':
            # AUS=1, ENG=2, PAK=3, NZ=4, SA=5, SL=6, BANGLADESH=7
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Hyderabad (Deccan)', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Guwahati', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Mumbai', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Rajkot', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Nagpur', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Cuttack', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Kolkata', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Delhi', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Jaipur', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Gwalior', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Ahmedabad', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Kochi', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Visakhapatnam', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Margao', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Vadodara', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Bengaluru', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Mohali', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Mumbai', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Indore', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Ranchi', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Pune', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Kanpur', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Mumbai (BS)', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Thiruvananthapuram', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        if countryCode == '7':
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Sri Lanka', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Karachi', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Lahore', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Rawalpindi', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        if countryCode == '8':
            df.loc[df['Opposition'] == 'v Australia', 'Opposition'] = 1;
            df.loc[df['Opposition'] == 'v England', 'Opposition'] = 2;
            df.loc[df['Opposition'] == 'v India', 'Opposition'] = 3;
            df.loc[df['Opposition'] == 'v New Zealand', 'Opposition'] = 4;
            df.loc[df['Opposition'] == 'v South Africa', 'Opposition'] = 5;
            df.loc[df['Opposition'] == 'v Pakistan', 'Opposition'] = 6;
            df.loc[df['Opposition'] == 'v Bangladesh', 'Opposition'] = 7;

            df['Opposition'].replace(to_replace=r'^.*$', value=10, regex=True, inplace=True);
            indexNames = df[df['Opposition'] == 10].index;
            df.drop(indexNames, inplace=True);

            # HomeGround=1, Otherwise=0
            df.loc[df['Ground'] == 'Galle', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Colombo (RPS)', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Colombo (SSC)', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Dambulla', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Kandy', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Pallekele', 'Ground'] = 1;
            df.loc[df['Ground'] == 'Hambantota', 'Ground'] = 1;
            df['Ground'].replace(to_replace=r'^.*$', value=0, regex=True, inplace=True);

        return df

    def cleanMargins(self, df):
        df_run = df[['Margin', 'Date']].copy()
        df_run = df_run[df_run['Margin'].astype(str).str.contains("runs")]
        df_run['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_run['Margin'] = pd.to_numeric(df_run['Margin'])
        bin_labels = ['okay', 'good', 'very good']
        bin_range = [0, 50, 100, 400]
        df_run['Margin'] = pd.cut(df_run['Margin'], bins=bin_range, labels=bin_labels)
        df_run["Margin_cat_codes"] = df_run["Margin"].astype('category').cat.codes

        df_wkt = df[['Margin', 'Date']].copy()
        df_wkt = df_wkt[df_wkt['Margin'].astype(str).str.contains("wickets")]
        df_wkt['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_wkt['Margin'] = pd.to_numeric(df_wkt['Margin'])
        bin_range = [0, 2, 5, 10]
        df_wkt['Margin'] = pd.cut(df_wkt['Margin'], bins=bin_range, labels=bin_labels)
        df_wkt["Margin_cat_code"] = df_wkt["Margin"].astype('category').cat.codes

        df = df.merge(df_run, on="Date", how='left')
        df.rename(columns={'Margin_cat_codes': 'Margin_cat'}, inplace=True)
        df.drop(columns=['Margin_y'], inplace=True)
        df['Margin_cat'].fillna(0, inplace=True)

        df = df.merge(df_wkt, on="Date", how='left')
        df.rename(columns={'Margin_cat_code': 'Margin_cat_w'}, inplace=True)
        df['Margin_cat_w'].fillna(0, inplace=True)
        df.head()

        df['Margin'] = df['Margin_cat'] + df['Margin_cat_w']
        df.drop(columns=['Margin_x', 'Margin_cat', 'Margin_cat_w'], inplace=True)
        df['Margin'] = df['Margin'].astype(int)

        df.drop(columns=['Date'], inplace=True)

        return df