# Review quality classification
![](https://github.com/KevsDe/amz_reviewd_classificator/blob/main/static/rev_ban.gif.gif?raw=true)
## About the project:
61% of the reviews published on Amazon are likely to be fake, the objective of this project is analyse identify low-quality reviews based in contextual and behavioural features.

**This project was made for learning and fun purposes and is not a production service**

## About the data:
The data set is available on Kaggle: 
https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews

## About the model:
 - Model trained with 50630 observations
 - Last Update 2022/12/22
 - The model used is SVC
 - Available parameters: Review text
 
## How to run the model
 - Download the files
 - Download the dataset https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews
 - Run the command pip install -r requirements.txt
 - Run the notebook "amazon_reviewd_project.ipynb"
 - Run train.py
 - Run predict.py

**Option Docker**
 - Build Docker container: `docker build -t review_bandit .`
 - Run Docker container: `docker run -it -p 9696:9696 review_bandit:latest`
 
![alt text](https://github.com/KevsDe/amz_reviewd_classificator/blob/main/static/dualbandit.png?raw=true)


**From Madrid (L)**
