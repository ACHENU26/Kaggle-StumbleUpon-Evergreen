# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

def featurization_fn(X_raw):
    
    X = X_raw.copy()
    
    # Set "MonthlyIncome" to 0 when there's no value
    no_income = X["MonthlyIncome"].isna()
    X.loc[no_income, "MonthlyIncome"] = 0
    
    # New feature: "MonthlyDebt"
    X.loc[no_income, "MonthlyDebt"] = X.loc[no_income, "DebtRatio"]
    
    # Replace "DebtRatio" with a value which is extremely high, for those with no income
    # (in theory it should be infinite)
    pos_debt = (X["DebtRatio"]>0)
    X.loc[no_income & pos_debt, "DebtRatio"] = 1000
    
    # Set "MonthlyDebt" for everyone who has an income
    X.loc[~no_income, "MonthlyDebt"] = X.loc[~no_income, "MonthlyIncome"] * X.loc[~no_income, "DebtRatio"]
    
    # New feature: "MonthlyBalance"
    X["MonthlyBalance"] = X["MonthlyIncome"] - X["MonthlyDebt"]

    return X
