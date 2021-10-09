Sign Language Classification from Image

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
- Batch normalization layer standardize intermediate outputs of neurons across the batch to give them equal importance and make the neural network converge faster
- Dropout layer can help model be less overfit to training data and increases model performance on unseen data

To Dos
- Make colored images able to be classified by developing a preprocessing pipeline that resize image to be compatible with model and turn the image into grayscale image
- Try using regularization with dropout to reduce missclassification on unseen data set
