# StumbleUpon Evergreen Classification Challenge
## Kaggle Competition 

#Authors :  Cédric FLAMANT & Axel CHENU 

# Write requirements.txt to be used by the Algorithmia platform

from pandas import __version__ as pandas_version
from joblib import __version__ as joblib_version
from sklearn import __version__ as sklearn_version
from dabl import __version__ as dabl_version
file = open("requirements-dev.txt", "w")
file.writelines(["algorithmia>=1.0.0,<2.0\n",
                 "pandas==" + pandas_version + "\n",
                 "joblib==" + joblib_version + "\n",
                 "scikit-learn==" + sklearn_version + "\n",
                 "dabl==" + dabl_version])
file.close()