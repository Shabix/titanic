import kaggle
import re
import pandas as pd 


titanic_kaggle = kaggle.KaggleApi()
titanic_kaggle.authenticate()
titanic_dataset_loc = '/azeembootwala/titanic'
titanic_dataset = titanic_kaggle.dataset_view(titanic_dataset_loc)
titanic_dataset.files