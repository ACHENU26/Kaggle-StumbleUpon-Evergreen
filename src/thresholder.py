# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

THRESHOLD = 0.5
def thresholding_fn(proba, pos_col="1"):
    pred = [True if p >= THRESHOLD else False for p in proba[pos_col].values]
    return pred