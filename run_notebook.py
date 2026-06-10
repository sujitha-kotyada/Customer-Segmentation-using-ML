import os
import matplotlib
matplotlib.use('Agg')  # non-interactive backend

import numpy as np     
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")



df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Mall_Customers.csv"))
df.head()



df.shape



df.describe



df = df.rename(columns={'Genre': 'Gender','Annual Income (k$)': 'Annual_income', 'Spending Score (1-100)': 'Spending_score'})



df.head()



df.isna().sum()



df.info()



df['Gender'] = df['Gender'].replace(['Female','Male'], [0,1])



df['Gender']




sns.set_style('whitegrid')
sns.pairplot(df, palette="husl")



plt.figure(1,figsize=(15 , 6))
feature_list = ['Age','Annual_income', "Spending_score"]
pos = 1 
for i in feature_list:
    plt.subplot(1 , 3 , pos)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.distplot(df[i], bins=20, kde = True)
    pos = pos + 1
plt.show()



sns.countplot(y = 'Gender', data = df, palette="husl", hue = "Gender")
df["Gender"].value_counts()



sns.pairplot(df, vars=["Age", "Annual_income", "Spending_score"],  kind ="reg", hue = "Gender", palette="husl", markers = ['+','*'])



sns.lmplot(x = "Age", y = "Annual_income", data = df, hue = "Gender")



sns.lmplot(x = "Annual_income", y = "Spending_score", data = df, hue = "Gender")



sns.lmplot(x = "Age", y = "Spending_score", data = df, hue = "Gender")



X = df.loc[:,["Age", "Annual_income", "Spending_score"]]
distortions = []
k = range(1,20)
for i in k:
    k_means_model = KMeans(n_clusters=i, random_state=0)
    k_means_model.fit(X)
    distortions.append(k_means_model.inertia_)
plt.plot(k , distortions , 'bo-')
plt.xlabel('Number of Clusters  (k)') , plt.ylabel('Distortions')
plt.show() 



k_means_model = KMeans(n_clusters=5,random_state=0)
k_means_model.fit(df)



labels = k_means_model.labels_



plt.scatter(df['Spending_score'],df['Annual_income'], c=k_means_model.labels_,cmap='rainbow')



plt.scatter(df['Age'],df['Spending_score'], c=k_means_model.labels_,cmap='rainbow')



plt.scatter(df['Age'],df['Annual_income'], c=k_means_model.labels_,cmap='rainbow')



Y = df.loc[:,['Age', 'Spending_score']]
distortions = []
k = range(1,10)
for i in k:
    k_means_model = KMeans(n_clusters = i)
    k_means_model.fit(Y)
    distortions.append(k_means_model.inertia_)
plt.plot(k , distortions , 'bo-')
plt.xlabel('Number of Clusters  (k)') , plt.ylabel('Distortions')
plt.show() 



k_means_model = KMeans(n_clusters=4)
k_means_model.fit(Y)



plt.scatter(df['Age'],df['Spending_score'], c=k_means_model.labels_,cmap='rainbow')



distortions = []
Z = df.loc[:,['Age', 'Annual_income']]
k = range(1,10)
for i in k:
    k_means_model = KMeans(n_clusters = i)
    k_means_model.fit(df)
    distortions.append(k_means_model.inertia_)
plt.plot(k , distortions , 'bo-')
plt.xlabel('Number of Clusters  (k)') , plt.ylabel('Distortions')
plt.show()



k_means_model = KMeans(n_clusters=6)
k_means_model.fit(Z)



plt.scatter(df['Age'],df['Annual_income'], c=k_means_model.labels_,cmap='rainbow')



# Save all open figures
import matplotlib.pyplot as plt
for i, fig_num in enumerate(plt.get_fignums()):
    fig = plt.figure(fig_num)
    output_path = os.path.join(os.path.dirname(__file__), f"output_figure_{i+1}.png")
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"Saved figure {i+1} to {output_path}")
print("\nAll figures saved. Script completed successfully!")
