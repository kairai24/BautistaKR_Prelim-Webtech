import pandas as pd

data = {
    'Milk': [True, True, False, True, False],
    'Bread': [True, True, True, False, False],
    'Butter': [False, True, True, True, False]
}

df = pd.DataFrame(data)

from mlxtend.frequent_patterns import apriori, association_rules

frequent_itemsets = apriori(df, min_support = 0.6, use_colnames = True)

print("Frequent Itemsets:")
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.7)

print("Association Rules:")
print(rules)