import matplotlib.pyplot as plt
import seaborn as sns


class Visualisations():

    def visualiseMargins(self, df):
        df_won = df[df['Result'] == 1]
        df_w_run = df_won[df_won['Margin'].astype(str).str.contains("runs")]
        df_w_run['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_w_run = df_w_run.astype({"Margin": int})

        categorical = ['Toss', 'Bat', 'Opposition', 'Ground']
        fig, ax = plt.subplots(2, 2, figsize=(10, 10))
        for variable, subplot in zip(categorical, ax.flatten()):
            sns.scatterplot(x="Result", y="Margin", hue=df_w_run[variable], data=df_w_run, ax=subplot)
        plt.show()

        plt.figure(2)
        sns.distplot(df_w_run['Margin'], hist=True, kde=True,
                     bins=int(5), color='darkblue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 4})
        plt.show()

        df_w_wickets = df_won[df_won['Margin'].astype(str).str.contains("wickets")]
        df_w_wickets['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_w_wickets = df_w_wickets.astype({"Margin": int})

        plt.figure(3)
        sns.distplot(df_w_wickets['Margin'], hist=True, kde=True,
                     bins=int(10), color='darkblue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 4})
        plt.show()

        df_lost = df[df['Result'] == 0]
        df_l_run = df_lost[df_lost['Margin'].astype(str).str.contains("runs")]
        df_l_run['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_l_run = df_l_run.astype({"Margin": int})

        categorical = ['Toss', 'Bat', 'Opposition', 'Ground']
        fig, ax = plt.subplots(2, 2, figsize=(10, 10))
        for variable, subplot in zip(categorical, ax.flatten()):
            sns.scatterplot(x="Result", y="Margin", hue=df_l_run[variable], data=df_l_run, ax=subplot)
        plt.show()

        plt.figure(5)
        sns.distplot(df_l_run['Margin'], hist=True, kde=True,
                     bins=int(5), color='darkblue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 4})
        plt.show()

        df_l_wicket = df_lost[df_lost['Margin'].astype(str).str.contains("wickets")]
        df_l_wicket['Margin'].replace(to_replace=r'[\s]+.*', value="", regex=True, inplace=True)
        df_l_wicket = df_l_wicket.astype({"Margin": int})

        plt.figure(6)
        sns.distplot(df_l_wicket['Margin'], hist=True, kde=True,
                     bins=int(10), color='darkblue',
                     hist_kws={'edgecolor': 'black'},
                     kde_kws={'linewidth': 4})
        plt.show()

    def visualise(self, df):
        categorical = ['Toss', 'Bat', 'Opposition', 'Ground']
        fig, ax = plt.subplots(2, 2, figsize=(10, 10))
        for variable, subplot in zip(categorical, ax.flatten()):
            sns.countplot(df[variable], ax=subplot)
        plt.show()
