Sign Language Classification from Image

This project aims to build multi-class classification model to predict american sign language from black and white images. The data set used for training and testing is [Sign Language MNIST](https://www.kaggle.com/datamunge/sign-language-mnist)

There is an image preprocessing function implemented which enable feeding colored image to the model. The preprocessing function resizes and turns the image into grayscale image. However, due to resizing non-square image there could be some distortion caused to the image.
<br/><br/>

Set up 
- Google Colab
1. Create a `Kaggle` account if you don't have
2. Generate `Kaggle API token` from `Account` tab in your `Kaggle Profile` page
3. Upload `kaggle.json` file automatically downloaded from `2.` to `root directory` of your `Google Drive`
4. Download `sign-language-classification.ipynb` jupyter notebook file and open it in Google Colab
5. Run the notebook
<br/><br/>

To Dos
- Implement a real-time application for detecting sign language
