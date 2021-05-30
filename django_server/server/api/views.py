from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from .models import User, Brand, Nutrition, NutriScore, Category, FRC, Food
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def login(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))

    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong Username"
        return HttpResponse(json.dumps(dic))
    if user.password != password:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))
    else:
        dic['status'] = "Success"
        dic['user_id'] = user.uid
        dic['user_role'] = user.role
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def register(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        username = post_content['username']
        password = post_content['password']
        role = post_content['role']
        user = User.objects.get(username=username)
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Success"
        now = datetime.datetime.now()
        newUser = User(username=username, password=password, role=role, register_time=now)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))


# sample
# {
#     "uid": "1",
#     "food_name": "food_sample_5",
#     "carbohydrate": 1.,
#     "fat": 1.,
#     "sugar": 1.,
#     "energy": 1.,
#     "protein": 1.,
#     "brand": "brand_sample_5",
#     "categories": ["category_sample_1", "category_sample_2", "category_sample_3", "category_sample_4"]
#     "score": 3
# }
@csrf_exempt
def create(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        creator = post_content['uid']
        food_name = post_content['food_name']
        nutrition_carbohydrate = post_content['carbohydrate']
        nutrition_fat = post_content['fat']
        nutrition_sugar = post_content['sugar']
        nutrition_energy = post_content['energy']
        nutrition_protein = post_content['protein']
        brand = post_content['brand']
        categories = post_content['categories']
        score_id = post_content['score']

        isBrand = True
        # get brand id
        try:
            br = Brand.objects.get(name=brand)
        except Brand.DoesNotExist:
            isBrand = False
        if isBrand is False:
            newBrand = Brand(None, brand, 0)
            newBrand.save()
        br = Brand.objects.get(name=brand)
        brand_id = br.id

        # create nutrition
        newNutrition = Nutrition(None,
                                 nutrition_carbohydrate,
                                 nutrition_sugar,
                                 nutrition_protein,
                                 nutrition_fat,
                                 nutrition_energy)
        newNutrition.save()

        # get nutrition id
        nutri = Nutrition.objects.last()
        nutrition_id = nutri.id

        # create food
        newFood = Food(None, food_name, nutrition_id, brand_id, score_id, creator)
        newFood.save()

        # get food
        fo = Food.objects.last()

        # create relation
        for category in categories:
            isCat = True
            try:
                cat = Category.objects.get(name=category)
            except Category.DoesNotExist:
                isCat = False
            if isCat is False:
                newCat = Category(name=category)
                newCat.save()
            cat = Category.objects.get(name=category)
            newFRC = FRC(food=fo, category=cat)
            newFRC.save()

        # brand product count +1
        br.product_count = br.product_count + 1
        br.save()

        dic['status'] = "Success"

    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"

    return HttpResponse(json.dumps(dic))


# sample
# {
#     "uid": "1",
#     "food_id": "105111"
# }
@csrf_exempt
def delete(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        uid = post_content['uid']
        food_id = post_content['food_id']
        food = Food.objects.get(id=food_id)

        uid = int(uid)

        if food.creator.uid != uid:
            dic['status'] = "Failed"
            dic['message'] = "No Permission"
            return HttpResponse(json.dumps(dic))

        # delete all relations
        FRC.objects.filter(food=food).delete()

        # brand product count -1
        br = food.brand
        br.product_count = br.product_count - 1
        br.save()

        # get nutrition id
        nutri_id = food.nutri.id

        # delete food
        Food.objects.get(id=food_id).delete()

        # delete nutrition
        Nutrition.objects.get(id=nutri_id).delete()
        dic['status'] = "Success"
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
    except Food.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "No Food"
    except FRC.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Unknown Error"

    return HttpResponse(json.dumps(dic))


# sample
# {
#     "uid": 1,
#     "food_id": 105106,
#     "carbohydrate": 1.2,
#     "fat": 1.2,
#     "sugar": 1.2,
#     "energy": 1.2,
#     "protein": 1.2,
#     "score": 4,
# }
@csrf_exempt
def update(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        post_content = json.loads(request.body)
        uid = post_content['uid']
        food_id = post_content['food_id']
        nutrition_carbohydrate = post_content['carbohydrate']
        nutrition_fat = post_content['fat']
        nutrition_sugar = post_content['sugar']
        nutrition_energy = post_content['energy']
        nutrition_protein = post_content['protein']
        score_id = post_content['score']

        food = Food.objects.get(id=food_id)
        uid = int(uid)

        # update score
        new_score = NutriScore.objects.get(id=score_id)
        food.score = new_score
        food.save()

        # update nutrition
        nutri = food.nutri
        nutri.carbohydrate = nutrition_carbohydrate
        nutri.fat = nutrition_fat
        nutri.sugar = nutrition_sugar
        nutri.energy_kcal = nutrition_energy
        nutri.protein = nutrition_protein
        nutri.save()
        dic['status'] = "Success"
        if food.creator.uid != uid:
            dic['status'] = "Failed"
            dic['message'] = "No Permission"
            return HttpResponse(json.dumps(dic))
    except (KeyError, json.decoder.JSONDecodeError):
        dic['status'] = "Failed"
        dic['message'] = "No Input"
    except Food.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "No Food"
    except FRC.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Unknown Error"
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def fuck(request):
    dic = {'id': [], 'name': []}
    lis = Food.objects.all()
    for li in lis:
        dic['id'].append(li.id)
        dic['name'].append(li.name)
    return HttpResponse(json.dumps(dic))


@csrf_exempt
def query(request, food_start):
    dic = {'food_id': [], 'food_name': [], 'food_brand': [], 'food_categories': [], 'food_score': []}
    try:
        food_list = Food.objects.all()[food_start: food_start + 20]
        for food_li in food_list:
            _Id = food_li.id

            _Name = food_li.name

            br = food_li.brand
            _Brand = br.name

            relations = FRC.objects.filter(food=_Id)
            _Cat = []
            for relation in relations:
                cat = relation.category
                _Cat.append(cat.name)

            sco = food_li.score
            _Score = sco.r

            dic['food_id'].append(_Id)
            dic['food_name'].append(_Name)
            dic['food_brand'].append(_Brand)
            dic['food_categories'].append(_Cat)
            dic['food_score'].append(_Score)
        dic['status'] = "Success"
    except Food.DoesNotExist:
        dic['status'] = "Failed"

    return HttpResponse(json.dumps(dic))


@csrf_exempt
def product(request, food_id):
    dic = {}
    try:
        food = Food.objects.get(id=food_id)
        dic['food_id'] = food.id
        dic['food_name'] = food.name
        dic['food_brand'] = food.brand.name
        dic['food_brand_id'] = food.brand.id
        dic['food_brand_product_count'] = food.brand.product_count
        dic['food_score'] = food.score.r
        dic['food_score_desc'] = food.score.des
        dic['food_creator'] = food.creator.uid
        dic['categories_id'] = []
        dic['categories_name'] = []

        relations = FRC.objects.filter(food=food)
        for relation in relations:
            dic['categories_id'].append(relation.category.id)
            dic['categories_name'].append(relation.category.name)
        dic['status'] = "Success"
    except (Food.DoesNotExist, FRC.DoesNotExist):
        dic['status'] = "Failed"

    return HttpResponse(json.dumps(dic))


