from sklearn.cluster import DBSCAN
import pandas as pd

x = ('https://raw.githubusercontent.com/Learningator/learning-200-data/main/train_set.csv')

model = pd.read_csv(x)

clustering = DBSCAN(eps=3, min_samples=8).fit(model)
model["cluster"] = clustering.fit_predict(model)

file = 'data.json'
with open(file) as train_file:
    dict_train = json.load(train_file)

lp = pd.DataFrame.from_dict(dict_train, orient='index')
train.reset_index(level=0, inplace=True)

lp["cluster"] = clustering.fit_predict(model)

trained_lp = lp.to_json(lp)