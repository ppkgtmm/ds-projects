Sign Language Image Classification

This project aims to build multi-class classification model to predict american sign language letters from black and white images.
<br/><br/>

Set up 
- Google Colab
1. Download [dataset](https://www.kaggle.com/datamunge/sign-language-mnist)
2. Upload the dataset to your Google Drive
3. Mount the google drive to your Google Colab session
4. Replace `train_path` and `test_path` in the second cell with path to train set and test set
<br/><br/>


Findings
- Standardization gives equal chance to all features (image pixels) to contribute in target prediction
- Batch normalization layer standardize intermediate outputs of neurons
- Dropout layer can help model be less overfit to training data and increases model performance on unseen data
