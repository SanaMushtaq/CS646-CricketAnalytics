from scrapeData import *
from cleanData import *
from visualise import *
from train import *
import os


def main():
    if os.path.exists("australia.csv"):
        os.remove("australia.csv")
    scraper = Scrape()
    df = scraper.fetchData('australia')
    #print(df.shape)
    #print(df.head())
    cleanData = CleanData()
    df = cleanData.clean('australia', df)
    #print(df.shape)
    #print(df.head())

    visualisations = Visualisations()
    visualisations.visualiseMargins(df)

    df = cleanData.cleanMargins(df)
    visualisations.visualise(df)

    #model = Model()
    #features = ['Bat', 'Toss', 'Opposition', 'Ground']
    #features = ['Toss', 'Opposition']
    #features = ['Opposition']
    #[y_test, y_train, y_pred_test, y_pred_train] = model.trainKMeanModel(features, df)
    #model.evaluate(y_test, y_train, y_pred_test, y_pred_train)


class Controller:
    if __name__ == "__main__":
        main()
