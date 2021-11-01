House Price Estimation from House Attributes

Given house characteristics, the goal of this project is to predict house price using regression machine learning algorithms and optimize the resulting models. 

Redundant features are removed using correlation and feature engineering as well as target encoding are conducted to create new features and help add more 
information about target with less chance of overfitting as possible.

To maximize the models' performance on unseen data, hyperparameter tuning is done with k-fold cross validation to come up with best hyper parameters combination for the problem.
The combination of top 2 best models, each given some weight, produced greatest performance on test set.

Predictions were submitted to 2 Kaggle competitions namely [Housing Prices Competition for Kaggle Learn Users](https://www.kaggle.com/c/home-data-for-ml-course), 
[House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) scoring top 1% and top 9% on leaderboard, respectively.

Set up
* Kaggle
1. Create a `Kaggle account` if you don't have
2. Upload `house-price-prediction.ipynb` jupyter notebook to Kaggle
3. Open and link the notebook with [dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
4. Run the notebook

To Dos
* deploy models to a house price estimation application