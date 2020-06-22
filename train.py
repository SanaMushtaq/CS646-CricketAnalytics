from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Model():

    def trainLogisticRegressionModel(self, features, df):
        X = df.filter(features, axis=1)
        y = df.filter(['Result'], axis=1)
        y = y.astype('int')

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=5, test_size=0.25)

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel())
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r", align="center")
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using Logistic Regression')
        clf_lr = LogisticRegression()
        clf_lr.fit(X_train, y_train)
        y_pred_test = clf_lr.predict(X_test)
        y_pred_train = clf_lr.predict(X_train)

        return y_test, y_train, y_pred_test, y_pred_train

    def trainDecisionTreeModel (self, features, df):
        X = df.filter(features, axis=1)
        y = df.filter(['Result'], axis=1)
        y = y.astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.25)

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel())
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r",
                align="center")
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using Decision Tree Classifier')
        clf_dt = DecisionTreeClassifier(criterion='entropy')
        clf_dt.fit(X_train, y_train)
        y_pred_test = clf_dt.predict(X_test)
        y_pred_train = clf_dt.predict(X_train)

        return y_test, y_train, y_pred_test, y_pred_train

    def trainRandomForestModel(self, features, df):
        X = df.filter(features, axis=1);
        y = df.filter(['Result'], axis=1);
        y = y.astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.25);

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel());
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r",
                align="center")  # , yerr=std[indices] can be added as parameter
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using Random Forest Classifier')
        clf_rf = RandomForestClassifier(n_estimators=50);
        clf_rf.fit(X_train, y_train.values.ravel());
        y_pred_test = clf_rf.predict(X_test);
        y_pred_train = clf_rf.predict(X_train);

        return y_test, y_train, y_pred_test, y_pred_train

    def trainNaiveBayesModel(self, features, df):
        X = df.filter(features, axis=1);
        y = df.filter(['Result'], axis=1);
        y = y.astype('int')
        print(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=15, test_size=0.25);

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel());
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r",
                align="center")  # , yerr=std[indices] can be added as parameter
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using Naive Bayes Classifier')
        clf_gnb = GaussianNB()
        clf_gnb.fit(X_train, y_train.values.ravel())
        y_pred_test = clf_gnb.predict(X_test);
        y_pred_train = clf_gnb.predict(X_train);

        return y_test, y_train, y_pred_test, y_pred_train

    def trainSVMModel(self, features, df):
        X = df.filter(features, axis=1);
        y = df.filter(['Result'], axis=1);
        y = y.astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.25);

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel());
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r",
                align="center")  # , yerr=std[indices] can be added as parameter
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using SVM Classifier')
        clf_svm = svm.SVC(kernel='linear');
        clf_svm.fit(X_train, y_train.values.ravel());
        y_pred_test = clf_svm.predict(X_test);
        y_pred_train = clf_svm.predict(X_train);

        return y_test, y_train, y_pred_test, y_pred_train

    def trainKMeanModel(self, features, df):
        X = df.filter(features, axis=1);
        y = df.filter(['Result'], axis=1);
        y = y.astype('int')
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.25);

        forest = ExtraTreesClassifier(n_estimators=2, random_state=0)
        forest.fit(X, y.values.ravel());
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
        indices = np.argsort(importances)[::-1]
        # Plot the feature importances of the forest
        plt.figure(8)
        plt.title("Feature importances")
        plt.bar(range(X.shape[1]), importances[indices], color="r",
                align="center")  # , yerr=std[indices] can be added as parameter
        plt.xticks(range(X.shape[1]), indices)
        plt.xlim([-1, X.shape[1]])
        plt.show()

        print('Training using K-Means Classifier')
        clf_kmeans = KMeans(n_clusters=2, random_state=0);
        clf_kmeans.fit(X_train);
        y_pred_test = clf_kmeans.predict(X_test);
        y_pred_train = clf_kmeans.predict(X_train);

        return y_test, y_train, y_pred_test, y_pred_train

    def evaluate(self, y_test, y_train, y_pred_test, y_pred_train):
        print('Accuracy Score on train data: ', metrics.accuracy_score(y_true=y_train, y_pred=y_pred_train.ravel()))
        print('Accuracy Score on test data: ', metrics.accuracy_score(y_true=y_test, y_pred=y_pred_test.ravel()))
        print("Precision on test data:", metrics.precision_score(y_test, y_pred_test))
        print("Recall on test data:", metrics.recall_score(y_test, y_pred_test))
        data = metrics.confusion_matrix(y_test, y_pred_test)
        df_cm = pd.DataFrame(data, columns=np.unique(y_test), index=np.unique(y_test))
        df_cm.index.name = 'Actual'
        df_cm.columns.name = 'Predicted'
        plt.figure(9)
        sns.heatmap(df_cm, cmap="Blues", annot=True).set_title('Confusion Matrix')
        plt.show()
