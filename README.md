# EAT (Easy Automation Test)
## 第一阶段 —— 接口自动化测试平台
## 引导

1. 确保已经安装了Python 2版本.
2. 确保已经安装Node.js
3. 启动项目

```
# 安装项目需要的python依赖模块
pip install -r requirements.txt

# 安装node下的依赖前端模块
npm install

# 全局安装Gulp 4 CLI工具
npm install gulpjs/gulp-cli -g

# 第一行命令可能会报错，不要紧接着执行下一条命令 
python ./manage.py migrate account
python ./manage.py migrate
python ./manage.py loaddata sites
python ./manage.py runserver
```