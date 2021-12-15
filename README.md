# 懂车帝新能源汽车销量分析

### 项目所使用库文件

> - requests
> - ThreadPoolExecutor
> - pyquery
> - pymysql
> - pyecharts
> - os
> - webbrowser



### 项目目录结构

> |- dcdRequest.py
>
> |- analysis.py
>
> |- dataStorage.py
>
> |- draw.py
>
> |____display
>
> ​	   |- show.html
>
> |____SQL
>
> ​	   |- car_info.sql
>
> ​	   |- score.sql
>
> |- start.py

- dcdRequest.py：负责对页面数据进行请求。
- analysis.py：负责对`dcdRequest.py`请求成功的数据进行解析成为自己所需要的数据。
- dataStorage.py：负责对`analysis.py`解析好的数据进行存储，并提供了`queryData`方法，方便后续`draw.py`调用该方法获得数据库数据。
- draw.py：通过在该文件中调用`pyecharts`库文件实现相关的数据展示的HTML文件生成。
- display：在该目录中存放的是由`draw.py`生成的数据展示HTML文件。
- SQl：在该目录中存放的是对应的数据库SQL文件。
- start.py：文件入口，在该文件中负责全局代码的调用，在该文件中运用了多线程技术对页面信息进行请求。

### 项目运行方式

1. 使用 `pip install <库名>`安装好对应的库文件

2. 在本地`mysql`中创建数据库，运行`SQL`目录下的sql文件

3. 将`dataStorage.py`中的数据库用户名和密码改为自己本地mysql的。

   ```python
   import pymysql
   
   host = "127.0.0.1"
   user = "root"
   password = "xxxxx" #修改为自己的mysql密码
   database = "dongchedi" #修改为自己的数据库
   ```

4. 直接运行`start.py`即可以运行项目
