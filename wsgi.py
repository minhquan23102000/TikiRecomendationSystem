import math

import dill as pickle
import numpy as np
import pandas as pd
import streamlit as st
from surprise import dump

pd.options.display.float_format = '${:,.2f}'.format


#Support function
def format_price(price):
    price = "{:,.0f}".format(price)
    price = price.replace(',', '.')
    price += " VNĐ"
    return price


st.set_page_config(page_title="Online shop",
                   layout='wide',
                   page_icon="img/tiki_21.1k.jfif")
st.header("Tiki Recommendation System")
st.image('img/Logo_Website_Tiki.vn.png')

products = pd.read_csv('ProductRaw.csv')

menu = ["Content base recomendation", "Collaborative filtering recomendation"]

#Init meunu button
menuBtn = st.radio("Choose a recomendation system", menu)

for i in range(4):
    st.write('')

if menuBtn == menu[0]:

    #Create products menu k
    product_choice = st.sidebar.multiselect(
        "Choose your product",
        options=products.index,
        format_func=lambda x: products.iloc[x]['name'])

    with st.sidebar.expander("Or input your product content here: "):
        content = st.text_area(
            "", placeholder="Product name or product description", height=200)

    if not content and product_choice:
        product_choice = product_choice[0]
        #Create a placeholder for product
        product_holder = st.columns([2, 3])

        #Query the choice product
        my_product = products.iloc[product_choice]

        #Adding content to product placeholder
        #Loading image
        product_holder[0].image(my_product['image'], width=350)
        #Loading name, price and rating
        product_holder[1].markdown(f"###### Thương hiệu {my_product['brand']}")
        product_holder[1].markdown("### " + my_product['name'])
        product_holder[1].markdown("#### " + format_price(my_product['price']))
        product_holder[1].markdown(f'{my_product["rating"]}/5 :star:')
        #Loading description
        with st.expander("Mô tả sản phẩm"):
            st.write(my_product['description'])

    if content or product_choice:
        #Load content base model
        gmodel = pickle.load(open('model/gensim_contentbase.pkl', 'rb'))
        #Create white space
        for i in range(4):
            st.write()

        st.subheader("Similar products")
        #Get recommendation product
        if content:
            pred = gmodel.recommend(content)
        else:
            pred = gmodel.recommend(my_product['name'] + ' ' +
                                    my_product['description'])
        pred = pred[pred >= 0.12]
        n = len(pred)
        if not pred.empty:
            #Query get product
            rec_product = products[products['item_id'].isin(pred.index)]

            #Create list items
            rows_1 = st.columns(5)
            for i, row in enumerate(rows_1):
                if i >= n:
                    break
                row.image(rec_product.iloc[i]['image'], use_column_width=True)
                row.write(rec_product.iloc[i]['name'])
                price = format_price(rec_product.iloc[i]['price'])

                row.write(price)

            rows_2 = st.columns(5)
            for i, row in enumerate(rows_2):
                if i + 5 >= n:
                    break
                row.image(rec_product.iloc[i + 5]['image'],
                          use_column_width=True)
                row.write(rec_product.iloc[i + 5]['name'])
                price = format_price(rec_product.iloc[i + 5]['price'])
                row.write(price)
        else:
            st.write("There are no similar products in our data")

elif menuBtn == menu[1]:
    reviews = pd.read_csv('review_clean.csv', index_col=0)
    customers = reviews['customer_id'].unique()
    customer_id = st.sidebar.selectbox("Customer id", customers[:100])

    #Select id of product was not bought by user
    product_bought = reviews[reviews['customer_id'] == customer_id]

    def recommend(customer_id, top_n=10):
        _, model = dump.load('model/suprise_model.pkl')
        #Query products that have not bought yet by user
        list_product = products['item_id']
        cond = ~np.isin(list_product, product_bought['product_id'])
        product_not_bought = np.where(cond, list_product, list_product)

        recommend_product = pd.DataFrame(product_not_bought,
                                         columns=['product_id'])
        recommend_product['estimation_score'] = recommend_product[
            'product_id'].apply(lambda x: model.predict(customer_id, x).est)
        return recommend_product.nlargest(top_n, 'estimation_score')

    #Show history products
    st.write("History invoice")
    history_products = pd.merge(product_bought,
                                products,
                                right_on='item_id',
                                left_on='product_id')
    history_products['review_rating'] = list(
        product_bought['rating'].apply(lambda x: f'{x:.1f}'))
    history_products = history_products[['name', 'price', 'review_rating']]

    st.write(history_products)

    #Show pred products
    st.write("Our product that you may love")
    pred = recommend(customer_id)
    pred = pred[pred['estimation_score'] > 4]
    if (pred.shape[0] > 0):
        #Query get product
        rec_product = products[products['item_id'].isin(pred['product_id'])]
        #Create list items
        rows_1 = st.columns(5)
        for i, row in enumerate(rows_1):
            row.image(rec_product.iloc[i]['image'], use_column_width=True)
            #row.markdown(get_img_with_href(rec_product.iloc[i]['image'], rec_product.iloc[i]['url']), unsafe_allow_html=True)
            row.write(rec_product.iloc[i]['name'])
            price = format_price(rec_product.iloc[i]['price'])
            row.write(price)

        rows_2 = st.columns(5)
        for i, row in enumerate(rows_2):
            row.image(rec_product.iloc[i + 5]['image'], use_column_width=True)
            row.write(rec_product.iloc[i + 5]['name'])
            price = format_price(rec_product.iloc[i + 5]['price'])
            row.write(price)
