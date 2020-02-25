# 采集产品开发
1. 启动（仅限本机）
    - 前端npm run dev
    - 后端crawl_product文件夹下执行python manage.py runserver(后端服务的架子基本上搭好)
    - 爬取服务jd_asyicb文件夹下执行python jd_template2_sep.py

2. 所需依赖（主要是vue）
    - element-ui
    - vue-json-viewer [教程](https://github.com/chenfengjw163/vue-json-viewer/blob/master/README_CN.md#%E5%AE%89%E8%A3%85)
    - axios
    - sass [Vue2.x一定是这个教程，否则采坑](https://blog.csdn.net/HH18700418030/article/details/101035561)

3. 页面
    - 在project/src/components中contains.vue文件是详情页的页面
    - 在project/src/components中userUse.vue文件是工作台的页面

4. 库
    - crawl_product/ddls.txt 是创建mysql的语句







