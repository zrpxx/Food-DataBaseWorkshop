# Food-DataBaseWorkshop
# 外包项目
## 1. 爬虫部分
### 根目录文件下打开spider/open_food_facts,这个文件夹是爬虫scrapy的根文件夹，下面food.json内存储的是爬下来的json文件，目录open_food_facts内是爬虫工程文件
### open_food_facts/spiders/food_spider内为爬虫文件，其他不用管.
### food_spider内def start_requests 是启动url，就爬了七页可以加，parse是解析，解析使用scrapy自带的css解析器，要重新爬的话在spider/open_food_facts目录内命令行输入scrapy crawl food -O food.json，自动爬取
## 2. 导入数据
### 根目录下import_data.py是导入数据脚本，初始数据导入使用数据集，有二十多G，一起发上来了 ***（导入脚本可以删除），数据库dump出的sql语句已经发过来了，直接在命令行或ide中输入即可，由于有外键影响，导入顺序可能要看一下
## 3. django服务端
### 本项目采取前后端分离，后端使用django实现，主要功能为为前端vue提供api，与数据库交互
### django具体教程参见django文档 https://docs.djangoproject.com/en/3.2/ 先startproject server 再startapp api
### 重点要修改的是把django_server/server/server/settings.py内的数据库改为自己的mysql数据库信息，因为django适合的是绿色初始项目，对已有数据库的项目需要检测创造模型，django_server/server目录下执行py manage.py inspectdb，再执行py manage.py inspectdb > models.py 命令得到model，代替目录api中的models.py
### 前后端分离项目后端主要为前端发送api，所有views中接受到的request返回的response都包含json数据文件
### django启动命令为py manage.py runserver 默认127.0.0.1:8000端口，vue接收也在这个端口
## 4. Vue客户端
### 依赖安装后，在frontend目录下执行quasar dev运行前端服务，默认地址为127.0.0.1:8080
### 前端主要使用Vue框架，Quasar UI框架，axios为网络库
## 5. 依赖安装
###  前端: 安装Nodejs环境，frontend目录下执行npm install
###  后端：安装conda环境，执行conda env create -f food_env.yaml
