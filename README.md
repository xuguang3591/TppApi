1、准备：安装mysql redis
2、创建数据库TppApi: create database TppApi charset='utf8';
3、安装项目依赖：pip install -r request.txt
4、打开项目，执行：
   1 初始化：python manager.py db init
   2 迁移： python manager.py db migrate
   3 更新到数据库：python manager.py db upgrade
5、启动项目: python manager.py runserver
