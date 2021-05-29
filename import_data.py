import jsonlines
import pymysql


def judge_pure_english(keyword):
    return all(ord(c) < 128 for c in keyword)


def judge_pure_english_list(key_list):
    for li in key_list:
        # print("li:", li)
        if judge_pure_english(li) is False:
            return False
    return True


if __name__ == '__main__':
    # conn = pymysql.connect(host='182.92.96.183', user='food', password='2p3mY6n87J4Mwp6p', db='food')
    conn = pymysql.connect(host='localhost', user='root', password='123', db='temp')
    cursor = conn.cursor()
    creator_uid = 1
    # sql = "SELECT ID FROM BRAND WHERE NAME=%s"
    # cursor.execute(sql, "hhh")
    # d = cursor.fetchall()
    # print(len(d))
    # sql = "SELECT PASSWORD FROM USER WHERE USERNAME=%s"
    # cursor.execute(sql, "administrator")
    # datas = cursor.fetchone()
    # print(datas[0])

    with jsonlines.open("E:/garbage/openfoodfacts-products.jsonl") as jsonfile:
        for line in jsonfile.iter(type=dict, skip_invalid=True):
            try:
                carbohydrate = line["nutriments"]["carbohydrates_100g"]
                protein = line["nutriments"]["proteins_100g"]
                fat = line["nutriments"]["fat_100g"]
                energy_kcal = line["nutriments"]["energy-kcal_100g"]
                sugar = line["nutriments"]["sugars_100g"]
                categories = line["categories_tags"]
                brand = line["brands_tags"][0]
                nutriscore = line["nutriscore_grade"]

                name = line["product_name"]

                # print(name, nutriscore, brand, categories)
                # print(judge_pure_english(name))
                # print(judge_pure_english(brand))
                # print(judge_pure_english_list(categories))
                # filter unknown char
                if judge_pure_english(name) is False \
                        or judge_pure_english(brand) is False \
                        or judge_pure_english_list(categories) is False:
                    # print("finish")
                    continue
                # product food can not duplicate
                sql = "SELECT ID FROM FOOD WHERE NAME=%s"
                cursor.execute(sql, name)
                judge = cursor.fetchall()

                if len(judge) != 0:
                    continue

                # fetch brand id
                sql = "SELECT ID FROM BRAND WHERE NAME=%s"
                cursor.execute(sql, brand)
                brand_ids = cursor.fetchall()
                if len(brand_ids) == 0:
                    sql = "INSERT INTO BRAND (NAME, PRODUCT_COUNT) VALUE (%s, 0)"
                    cursor.execute(sql, brand)
                    sql = "SELECT ID FROM BRAND ORDER BY ID DESC LIMIT 1"
                    cursor.execute(sql)
                    brand_ids = cursor.fetchall()
                brand_id = brand_ids[0][0]

                # fetch nutriscore id
                nutriscore_id = chr(ord(nutriscore) - ord('a') + ord('1'))
                # create nutrition
                # print("hh")
                sql = "INSERT INTO nutrition(CARBOHYDRATE, SUGAR, PROTEIN, FAT, ENERGY_KCAL) VALUE (%s, %s, %s, %s, %s)"
                cursor.execute(sql, [carbohydrate, sugar, protein, fat, energy_kcal])

                # fetch nutrition id
                sql = "SELECT id FROM nutrition ORDER BY id DESC LIMIT 1"
                cursor.execute(sql)
                nutrition_id = cursor.fetchone()[0]
                # create food
                sql = "INSERT INTO FOOD (NAME, NUTRI_ID, BRAND_ID, SCORE_ID, CREATOR_ID) VALUE (%s, %s, %s, %s, %s)"
                cursor.execute(sql, [name, nutrition_id, brand_id, nutriscore_id, creator_uid])
                # fetch food id
                sql = "SELECT ID FROM FOOD ORDER BY ID DESC LIMIT 1"
                cursor.execute(sql)
                food_id = cursor.fetchone()[0]
                # create relation
                for category in categories:
                    sql = "SELECT ID FROM CATEGORY WHERE NAME=%s"
                    cursor.execute(sql, category)
                    cats = cursor.fetchall()
                    if len(cats) == 0:
                        # create category
                        sql = "INSERT INTO CATEGORY (NAME) VALUE (%s)"
                        cursor.execute(sql, category)
                        sql = "SELECT ID FROM CATEGORY ORDER BY ID DESC LIMIT 1"
                        cursor.execute(sql)
                        cats = cursor.fetchall()
                    category_id = cats[0][0]
                    sql = "INSERT INTO F_R_C(FOOD_ID, CATEGORY_ID) VALUE (%s, %s)"
                    cursor.execute(sql, [food_id, category_id])
                print("finish")
                conn.commit()
            except Exception as e:
                pass

    cursor.close()
    conn.commit()
    conn.close()
