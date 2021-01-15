# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

from pandas import DataFrame
def scoring_fn(x, model):
    """
    x should be a dataframe of featurized inputs
    return a dataframe with as many rows as x
    """
    return DataFrame(model.predict_proba(x),
                     columns=list(model.classes_.astype(str)),
                     index=x.index)