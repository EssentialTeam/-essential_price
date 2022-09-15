import jieba

from tgi102_flask import app, db, render_template, request, get_page_parameter, Pagination, session, redirect, url_for
from tgi102_flask.model import Product, Price, Category, Mart

from flask import jsonify
import os
import pandas as pd
import re
import numpy as np
import cv2
from md_test import milk_model
import mysql.connector
from mysql.connector import errorcode



@app.route('/')
def hello_world():  # put application's code here
    index_sql = db.session.query(Product, Price).filter(Product.id == Price.product_id).order_by(db.func.rand()).limit(8)
    query_data_list = []

    for i in index_sql:
        query_data_list.append(i)

    Product1_id = query_data_list[0][0].id
    name1 = query_data_list[0][0].product_name
    pic_url1 = query_data_list[0][0].product_pic_url
    price1 = query_data_list[0][1].price

    Product2_id = query_data_list[1][0].id
    name2 = query_data_list[1][0].product_name
    pic_url2 = query_data_list[1][0].product_pic_url
    price2 = query_data_list[1][1].price

    Product3_id = query_data_list[2][0].id
    name3 = query_data_list[2][0].product_name
    pic_url3 = query_data_list[2][0].product_pic_url
    price3 = query_data_list[2][1].price

    Product4_id = query_data_list[3][0].id
    name4 = query_data_list[3][0].product_name
    pic_url4 = query_data_list[3][0].product_pic_url
    price4 = query_data_list[3][1].price

    Product5_id = query_data_list[4][0].id
    name5 = query_data_list[4][0].product_name
    pic_url5 = query_data_list[4][0].product_pic_url
    price5 = query_data_list[4][1].price

    Product6_id = query_data_list[5][0].id
    name6 = query_data_list[5][0].product_name
    pic_url6 = query_data_list[5][0].product_pic_url
    price6 = query_data_list[5][1].price

    Product7_id = query_data_list[6][0].id
    name7 = query_data_list[6][0].product_name
    pic_url7 = query_data_list[6][0].product_pic_url
    price7 = query_data_list[6][1].price

    Product8_id = query_data_list[7][0].id
    name8 = query_data_list[7][0].product_name
    pic_url8 = query_data_list[7][0].product_pic_url
    price8 = query_data_list[7][1].price

    print(query_data_list)
    return render_template('index-2.html', Product1_id=Product1_id,name1=name1,pic_url1=pic_url1, price1=price1, Product2_id=Product2_id,name2=name2,pic_url2=pic_url2, price2=price2, Product3_id=Product3_id,name3=name3,pic_url3=pic_url3, price3=price3, Product4_id=Product4_id,name4=name4,pic_url4=pic_url4, price4=price4, Product5_id=Product5_id,name5=name5,pic_url5=pic_url5, price5=price5, Product6_id=Product6_id,name6=name6,pic_url6=pic_url6, price6=price6, Product7_id=Product7_id,name7=name7,pic_url7=pic_url7, price7=price7, Product8_id=Product8_id,name8=name8,pic_url8=pic_url8, price8=price8)


@app.route('/index')
def index():  # put application's code here
    return render_template('index-2.html')



@app.route('/shop/<Category_id>')
def category(Category_id):  # put application's code here
    search = False
    q = request.args.get('page', 1)
    int_page = int(q)

    end = (int_page - 1) * 12
    # if q:
    #     search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    count_category_sql = db.session.query(db.func.count(Product.id)).filter(Product.id == Price.product_id).filter(Product.category_id == Category_id).all()[0][0]
    print(count_category_sql)

    pagination = Pagination(page=page, per_page=12, total=count_category_sql, search=search)

    category_sql = db.session.query(Product, Price).filter(Product.id == Price.product_id).filter(Product.category_id == Category_id).order_by(db.func.rand()).limit(12).offset(end)
    query_data_list = []

    for i in category_sql:
        query_data_list.append(i)
    print("query_data_list",  query_data_list)

    product_id1 = query_data_list[0][0].id
    name1 = query_data_list[0][0].product_name
    pic_url1 = query_data_list[0][0].product_pic_url
    price1 = query_data_list[0][1].price

    product_id2 = query_data_list[1][0].id
    name2 = query_data_list[1][0].product_name
    pic_url2 = query_data_list[1][0].product_pic_url
    price2 = query_data_list[1][1].price

    product_id3 = query_data_list[2][0].id
    name3 = query_data_list[2][0].product_name
    pic_url3 = query_data_list[2][0].product_pic_url
    price3 = query_data_list[2][1].price

    product_id4 = query_data_list[3][0].id
    name4 = query_data_list[3][0].product_name
    pic_url4 = query_data_list[3][0].product_pic_url
    price4 = query_data_list[3][1].price

    product_id5 = query_data_list[4][0].id
    name5 = query_data_list[4][0].product_name
    pic_url5 = query_data_list[4][0].product_pic_url
    price5 = query_data_list[4][1].price

    product_id6 = query_data_list[5][0].id
    name6 = query_data_list[5][0].product_name
    pic_url6 = query_data_list[5][0].product_pic_url
    price6 = query_data_list[5][1].price

    product_id7 = query_data_list[6][0].id
    name7 = query_data_list[6][0].product_name
    pic_url7 = query_data_list[6][0].product_pic_url
    price7 = query_data_list[6][1].price

    product_id8 = query_data_list[7][0].id
    name8 = query_data_list[7][0].product_name
    pic_url8 = query_data_list[7][0].product_pic_url
    price8 = query_data_list[7][1].price

    product_id9 = query_data_list[8][0].id
    name9 = query_data_list[8][0].product_name
    pic_url9 = query_data_list[8][0].product_pic_url
    price9 = query_data_list[8][1].price

    product_id10 = query_data_list[9][0].id
    name10 = query_data_list[9][0].product_name
    pic_url10 = query_data_list[9][0].product_pic_url
    price10 = query_data_list[9][1].price

    product_id11 = query_data_list[10][0].id
    name11 = query_data_list[10][0].product_name
    pic_url11 = query_data_list[10][0].product_pic_url
    price11 = query_data_list[10][1].price

    product_id12 = query_data_list[11][0].id
    name12 = query_data_list[11][0].product_name
    pic_url12 = query_data_list[11][0].product_pic_url
    price12 = query_data_list[11][1].price


    return render_template('shop.html', page=page, pagination=pagination,  Category_id=Category_id,  product_id1=product_id1, name1=name1, pic_url1=pic_url1, price1=price1, product_id2=product_id2, name2=name2, pic_url2=pic_url2, price2=price2, product_id3=product_id3, name3=name3, pic_url3=pic_url3, price3=price3, product_id4=product_id4, name4=name4, pic_url4=pic_url4, price4=price4, product_id5=product_id5, name5=name5, pic_url5=pic_url5, price5=price5, product_id6=product_id6, name6=name6, pic_url6=pic_url6, price6=price6, product_id7=product_id7, name7=name7, pic_url7=pic_url7, price7=price7, product_id8=product_id8, name8=name8, pic_url8=pic_url8, price8=price8, product_id9=product_id9, name9=name9, pic_url9=pic_url9, price9=price9, product_id10=product_id10, name10=name10, pic_url10=pic_url10, price10=price10, product_id11=product_id11, name11=name11, pic_url11=pic_url11, price11=price11, product_id12=product_id12, name12=name12, pic_url12=pic_url12, price12=price12)


@app.route('/shop-details/<Product_id>')
def shop_details(Product_id):  # put application's code here

    details_product_sql = db.session.query(Product, Price).filter(Product.id == {Product_id}).first()
    query_data_list = []

    for i in details_product_sql:
        query_data_list.append(i)

    details_Product_id = query_data_list[0].id
    details_name = query_data_list[0].product_name
    details_pic_url = query_data_list[0].product_pic_url
    details_price = query_data_list[1].price
    details_category_id = query_data_list[0].category_id
    details_date = query_data_list[1].date
    details_product_url = query_data_list[0].product_url
    return render_template('shop-details.html', details_Product_id=details_Product_id, details_name=details_name, details_pic_url=details_pic_url, details_price=details_price, details_category_id=details_category_id, details_date=details_date, details_product_url=details_product_url)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error)

# @app.route('/update-pic', methods=["GET", "POST"])
# def uploadprocess():
#     print('upload post')
#     if 'input-id' not in request.files:
#         return jsonify({"errno": 100, "errmsg": "無檔案"})
#     if request.method == 'POST':
#         files = request.files.getlist('input-id')
#
#         for file in files:
#             filename = file.filename
#             print("file", file)
#             print("filename", filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             print(jsonify({"errno": 0, "errmsg": "上傳成功"}))
#
#         return jsonify({"errno": 0, "errmsg": "上傳成"})
#     return render_template('blog-details.html')

@app.route('/upload_search', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # file = request.files['file'].read()
        # file = request.files
        files = request.files.getlist('file')
        photo = request.files['file'].read()
        # print("photo", photo)

        for file in files:
            filename = file.filename
            print("filename", filename)
            # file.save(app.config['UPLOAD_FOLDER'], filename)
            file.save(f'tgi102_flask/static/upload/{filename}')
        upload_photo = f'/static/upload/{filename}'
        print("upload_photo", upload_photo)

        # img = cv2.imread(f'tgi102_flask/static/upload/{filename}')
        # print("img", img)

        photo_fromstring = np.fromstring(photo, np.uint8)
        print("photo_fromstring", photo_fromstring)
        photo_imdecode = cv2.imdecode(photo_fromstring, cv2.IMREAD_COLOR)[:, :, ::-1]
        # milk_model(photo_imdecode)
        result = milk_model(photo_imdecode)


        return redirect(url_for('uploaded_file', filename=result))
    return render_template('upload_search.html')

#
@app.route('/search_photo/<filename>')
def uploaded_file(filename):
    return render_template('result_2.html', filename=filename)

#
@app.route('/search', methods=['get', 'POST'])
def search():
    if request.method == 'POST':
        # 取出keyword
        keyword = request.form['keyword']
        print("keyword", keyword)
        # 對keyword使用結巴

        return redirect(url_for("search_results", query=keyword))
    else:
        return render_template('index-2.html')

@app.route('/search_results/<query>')
def search_results(query):

    config = {
        'host': 'projectdb.ckq7h3eivlb4.ap-northeast-1.rds.amazonaws.com',
        'user': 'admin',
        'password': 'tgi102aaa',
        'database': 'essential'
    }
    conn = mysql.connector.connect(**config)
    print("Connection established")
    cursor = conn.cursor()

    text = query
    letter = list(jieba.cut(text, cut_all=False, HMM=True))
    print("letter", letter)

    # SQL select & 處理回傳結果格式
    sql_cmd = f"""select pd.product_name, pr.price, pd.id, pd.product_pic_url from product pd join price pr on pd.id = pr.product_id where pd.product_name regexp '[{text}]' and pr.`date` = '2022-08-24'"""

    cursor.execute(sql_cmd)
    product = cursor.fetchall()
    print("product", product)
    product_list = []
    for row in product:
        row = list(row)
        product_list.append(row)
    print("product_list", product_list)

    # SQL查詢結果之商品名，需達到Jieba分詞結果之40%符合程度，才回傳該項商品資訊
    return_list = []
    for j in product_list:
        percent = len(letter) * 0.4
        # print("percent", percent)
        n = 0
        for i in letter:
            pattern0 = re.compile((letter[0]))
            # print(pattern0, "pattern0")
            compare0 = pattern0.search(j[0])
            # print("compare0", compare0)
            if compare0 is None:
                break
            else:
                pattern = re.compile((i))
                compare = pattern.search(j[0])
                if compare is not None:
                    if n >= percent and j not in return_list:
                        return_list.append(j)
                    n += 1


    # print("return_list", return_list)
    # print("return_list[0]", return_list[0][0])
    # print("return_list[0][1]", return_list[0][1])
    # print("return_list[0][2]", return_list[0][2])
    # print("return_list[0][3]", return_list[0][3])
    #
    #
    #
    # try:
    #     search_product_id1 = return_list[0][2]
    #     search_name1 = return_list[0][0]
    #     search_pic_url1 = return_list[0][3]
    #     search_price1 = return_list[0][1]
    #
    #     search_product_id2 = return_list[1][2]
    #     search_name2 = return_list[1][0]
    #     search_pic_url2 = return_list[1][3]
    #     search_price2 = return_list[1][1]
    #
    #     search_product_id3 = return_list[2][2]
    #     search_name3 = return_list[2][0]
    #     search_pic_url3 = return_list[2][3]
    #     search_price3 = return_list[2][1]
    #
    #     search_product_id4 = return_list[3][2]
    #     search_name4 = return_list[3][0]
    #     search_pic_url4 = return_list[3][3]
    #     search_price4 = return_list[3][1]
    # except:
    #     pass



    # 搜索结果返回给前端
    return render_template('search_results.html', query=query, return_list=return_list)

if __name__ == '__main__':
    app.run(debug=True)
