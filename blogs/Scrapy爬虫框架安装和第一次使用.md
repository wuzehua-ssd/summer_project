@[Toc]

# 一、Scrapy安装
windows10系统下可以直接用命令：**pip install Scrapy**进行安装，但我安装的时候碰到了lxml安装下载超时的问题，查阅了有关博客后发现可以自己手动下载相关包，然后再install，问题即可解决
原博客地址如下：[](https://blog.csdn.net/chongxing8779/article/details/100867187)

# 二、第一个爬虫项目
在想要创建项目的文件目录下启动终端，使用命令：**scrapy startproject xxx（项目名）** 即可新建项目，项目结构如下：

xxx（项目名）
--scrapy.cfg  #部署配置文件

--xxx（项目名）#python模块，代码存放在该目录下
----spiders #爬虫存放目录
------_init_.py

----_init_.py
----item.py #项目项定义文件
----middlewares.py # 中间件定义
----pipelines.py #项目管道文件
----settings.py #项目设置文件

## 创建第一个爬虫
在spiders目录下面创建第一个爬虫quotes_spider.py
```
# 引入库
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

def parse(self,response):
    page = response.url.splite("/")[-2]
    fliename = 'quotes-%s.html' % page
    with open(fliename,'wb') as f:
        f.write(response.body)
    self.log('Saved file %s' % fliename)
```

其中，各块代码含义如下：
-name：标识爬虫，不同的爬虫不能有相同的name；
-start_requests()：必须返回一个迭代的Requests（你可以返回请求列表或写一个生成器函数），Spider将开始抓取。后续请求将从这些初始请求连续生成；
-parse()：将被调用来处理为每个请求下载的响应的方法。 response参数是一个TextResponse保存页面内容的实例，并且具有更多有用的方法来处理它。
 该parse()方法通常解析响应，提取抓取的数据作为词典，并且还找到要跟踪的新网址并从中创建新的请求（Request）。
 
 编写完成后在工作目录下打开终端，输入：scrapy crawl quotes即可运行爬虫。