from unittest import TestCase
from parameterized import parameterized
from os import path
from scrapeData import *


class TestScrape(TestCase):
    @parameterized.expand([
        ["pakistan"],
        ["england"]
    ])
    def test_fetch_data(self, country):
        df = Scrape.fetchData(self, country)
        df.columns = ['Team', 'Result', 'Margin', 'Toss', 'Bat', 'Opposition', 'Ground', 'Date']
        df_unique = df['Team']
        ser = pd.Series(df_unique.drop_duplicates())
        value = (ser[0].lower() == country and ser.size == 1)
        self.assertTrue(value)
        self.assertTrue(str(path.exists(country + '.csv')))


if __name__ == '__main__':
    TestCase.main()