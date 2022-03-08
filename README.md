
# Tiki Online Retail Shop Recommendation System
This project was build on a dataset that scrap from Tiki, an big online retail shop in Vietnam, you can view the website vit this link https://tiki.vn/

####  Project Status: Completed

## Demo
You can will the demo of the project at here: https://tiki-recomendation-system.herokuapp.com   /

## Project Intro/Objective
In this project we will build two type of recommendation system to help the customers fastly find their favorite products:
1. Content base recommendation (recommending base on the similarity of products)
2. Collaborative filtering (recommending base on the similarity of behaviors of customers)

### Methods Used
* Inferential Statistics
* Machine Learning
* Predictive Modeling
* Software Design
* Big Data Handling
* NLP (Natural Langues Preprocessing)

### Technologies
* Python
* Pandas, jupyter
* Sckit-learn, spark
* Streamlit
* Gensim 


## Project Description

The data was gave to us with the following description: 
There are two file, ProductRaw.csv and ReviewRaw.csv. ProductRaw.csv has information about properties of products. On the other hand, ReviewRaw.csv has information about customers rating on products. 

The ProductRaw.csv with the following columns:
+ item_id: products's id
+ name: products' name 
+ description: products's description
+ price: product's price after apply discount
+ list_price: product's true price
+ rating: product's rating average
+ brand: product's brand
+ group: type of product
+ url: the url to the webpage product
+ img: the link to the image of the product

The data was gave to us at "ReviewRaw.csv" with the following description:
1. customer_id: Customer's id 
2. product_id: Product's id 
3. name: customer's last name 
4. full_name: customer's full name 
5. create_time: the time when the record was created 
6. rating: the number of star was rated in range (1 - 5)
7. title: title of the review 
8. content: content of the review

Base on the structure data ProductRaw.csv I apply Tfidf search algorithm to find the similarity of each products, and recommending to customer.

Base on structure data ReviewRaw.csv I apply multiple algorithm of collaborative filtering, I and choose the best one, to find the similarity of each customer to other, and recommend their likely favorite products.

## Needs of this project
- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- big data processing
- web deployment

## Featured Notebooks/Analysis/Deliverables
* [Building Content Base Recommendation System](https://github.com/minhquan23102000/TikiRecomendationSystem/blob/master/Problem_1_ContentBasedRecomendation.ipynb)
* [Building Collaborative Filtering Recommendation System Using PySpark](https://github.com/minhquan23102000/TikiRecomendationSystem/blob/master/Problem_2_Collaborative_Filtering_using_PySpark.ipynb)
* [Building Collaborative Filtering Recommendation System Using Surprise](https://github.com/minhquan23102000/TikiRecomendationSystem/blob/master/Problem_2_Collborative_filtering_using_Suprise.ipynb)



## Contact
Email: minhquan23102000@gmail.com
