# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Brand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=20)  # Field name made lowercase.
    product_count = models.IntegerField(db_column='PRODUCT_COUNT')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'brand'


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'category'


class FRC(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    food = models.ForeignKey('Food', models.DO_NOTHING, db_column='FOOD_ID')  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='CATEGORY_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'f_r_c'


class Food(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=40)  # Field name made lowercase.
    nutri = models.ForeignKey('Nutrition', models.DO_NOTHING, db_column='NUTRI_ID')  # Field name made lowercase.
    brand = models.ForeignKey(Brand, models.DO_NOTHING, db_column='BRAND_ID')  # Field name made lowercase.
    score = models.ForeignKey('NutriScore', models.DO_NOTHING, db_column='SCORE_ID')  # Field name made lowercase.
    creator = models.ForeignKey('User', models.DO_NOTHING, db_column='CREATOR_ID')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'food'


class NutriScore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    r = models.CharField(db_column='R', max_length=5)  # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nutri_score'


class Nutrition(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    carbohydrate = models.FloatField(db_column='CARBOHYDRATE')  # Field name made lowercase.
    sugar = models.FloatField(db_column='SUGAR')  # Field name made lowercase.
    protein = models.FloatField(db_column='PROTEIN')  # Field name made lowercase.
    fat = models.FloatField(db_column='FAT')  # Field name made lowercase.
    energy_kcal = models.FloatField(db_column='ENERGY_KCAL')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'nutrition'


class User(models.Model):
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', unique=True, max_length=20)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30)  # Field name made lowercase.
    register_time = models.DateField(db_column='REGISTER_TIME')  # Field name made lowercase.
    role = models.IntegerField(db_column='ROLE')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'
