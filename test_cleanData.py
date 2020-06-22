from unittest import TestCase
from parameterized import parameterized

from cleanData import *


class TestCleanData(TestCase):
    @parameterized.expand([
        ["pakistan"],
        ["england"]
    ])
    def test_clean(self, country):
        df = pd.read_csv(country + '.csv')
        df = CleanData.clean(self, country, df)
        value = df['Result'].isin([0, 1]).all() and df['Toss'].isin([0, 1]).all() and df['Bat'].isin([0, 1]).all() \
                and df['Opposition'].isin([1, 2, 3, 4, 5, 6, 7]).all() and df['Ground'].isin([0, 1]).all()
        self.assertTrue(value)


if __name__ == '__main__':
    TestCase.main()