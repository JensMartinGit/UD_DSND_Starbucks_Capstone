### UD_DSND_Starbucks_Capstone
# Predicting Customer Response on Starbucks Promotional Offers 
### Detailed Walk-Through of a Udacity Data Scientist Nanodegree Capstone Project using Supervised Machine Learning with Python, Pandas and Scikit-learn

![Starbucks Header](/pics/starbucks_ml_capstone.png)

*Picture: Derivative from [DAKALUK](https://commons.wikimedia.org/wiki/File:HK_Starbucks_Coffee_in_Caine_Road.jpg), [CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5)*

This project was developed as part of my [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025). It is based on data from a **simulated customer** test provided by **Starbucks**. The data set depicts how customers make **purchasing decisions** and how these decisions are **influenced by promotional offers**. While the task for this project is not exactly prescribed, my approach is to use the data to **build a supervised machine learning model** that - based on demographic customer data and offer features -  **predicts customer response** on different types of promotional offers.

### Results  

The results are presented in a blog post on [Medium](https://medium.com/).

The post describes the complete data science process involved in using demographic customer data, meta data on promotional offers, and transaction data records from a 30-day experiment provided by Starbucks to build a machine learning model for predicting customer response on promotional offers. The post highlights the importance of data understanding and wrangling in this process. The project was **succesfully completed by training a supervised classifier using gradient boosting**, an ensemble method based on decision trees, which turned out to be the best algorithm for this task, and predicts customer response with an accuracy rate of almost 70 percent. Given the fact that also one and the same customer will react differently on one and the same offer, this is a quite satisfying result. I also drafted a few possible real-world applications for the model.

### Requirements

The project uses Python 3.7.9 (Anaconda 4.9.2 distribution) with the following libraries:
- pandas
- numpy
- matlotlib
- seaborn
- sklearn
- imblearn
- json
- pickle

### Licensing

This project is licensed under the terms of the [MIT license](https://mit-license.org/).
