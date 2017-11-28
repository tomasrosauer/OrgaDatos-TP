import numpy as np

from time import time
from scipy.stats import randint as sp_randint
import random as random

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer

# get some data
from sklearn.model_selection import train_test_split
df = pd.read_csv('data/pp-training.csv', low_memory=False)
X, X_test, y, y_test = train_test_split(df.drop(['price_usd_per_m2'], axis=1),df.price_usd_per_m2, test_size=0.2)
X, y = df.drop(df[['price_usd_per_m2']], axis=1), df.price_usd_per_m2

# build a classifier
clf = RandomForestRegressor(n_jobs=-1)


# Utility function to report best scores
def report(results, n_top=5):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


# specify parameters and distributions to sample from
# param_dist = { "n_estimators": [50,100,150,200],
#               "learning_rate": [0.1,0.5,1,1.5,2],
#               }

param_dist = {"max_depth": sp_randint(1, 15),
              "n_estimators": [100,150,200,400,500],
              "min_samples_split": sp_randint(2, 10),
              "min_samples_leaf": sp_randint(1, 10)}

# run randomized search
n_iter_search = 10
random_search = RandomizedSearchCV(clf, param_distributions=param_dist,
                                   n_iter=n_iter_search)

start = time()
random_search.fit(X, y)
print("RandomizedSearchCV took %.2f seconds for %d candidates"
      " parameter settings." % ((time() - start), n_iter_search))
report(random_search.cv_results_)
