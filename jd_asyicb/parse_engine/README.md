# Parse-Conf

## 项目简介

本项目基于 Python，通过配置符合规范的模板文件后，实现对 HTML、JSON、JSONP 内容的各字段解析。

## 项目依赖

lxml

## 模板示例

```conf
[url]
#JSON#data/tradeContract/pay/*/url

[icons]
#ENCODE#UTF-8,GBK
#HTML#//div[@class="bob"]/p[@id=!cid]/text()

[skuid]
#RE#Y#@#IM#skuid: ?(\d+),@id

[asda]
#HTML#//div[@class="bob"]/p
#UNQUOTE#
#RE#Y#@#im#skuid: ?(\d+),@id
```

## 模板规范

- 配置模板按行读取，每行有两种属性：``字段`` 或者 ``规则``。首先定义一个字段名，接下来一行或者多行是为解析此字段配置的规则列表。
- 字段用 `[` 以及 `]` 包裹。
- 规则每一行第一部分是用两个 `#` 包裹的，指定解析引擎。后面的内容根据引擎不同而含义不同。
- 规则为多行时，前一行的输出会作为后一行的输入，链式处理。
- 如果前一行的输出为列表，则下一行会对列表中的每一个对象进行处理。
- 输出为列表时，若列表为空则返回None，若列表只有一个元素则直接返回这个元素。

### 字段

`[keyword]`

需要解析的字段用 `[` 以及 `]` 包裹

### HTML 解析引擎

`#HTML#//div[@class="bob"]/p[@id=!cid]/text()`

使用 xpath 对 HTML 内容进行解析，所以书写满足 xpath 的规范即可。

扩充方法：`!` 用于传参

### JSON/JSONP 解析引擎

`#JSON#data/articles/*/!articleId/author/`

| 标识符 | 含义                      |
| ------ | ------------------------- |
| /      | 下一级的key               |
| *      | 遍历list或者dict的所有key |
| !      | 传参                      |

### 正则 解析引擎

`#RE#Y#@#IM#skuid: ?(\d+),@id`

 #RE#指定解析引擎，Y 指自定义传参标识，@是自定义的传参第五部分书写须满足正则规范。

第二部分可取`Y`、`N`，意为是否开启传参。如果取`Y`，则默认用`!`传参，或者自己在第三部分指定，比如示例中用的`@`；取`N`为不传参；

第三部分仅在开启传参时有效，置空则默认为`!`，或者自己指定参数标识。

第四部分是匹配外部规则，比如`I`忽略大小写，`M`多行匹配等。

第五部分是匹配逻辑，书写须满足正则规范。

### 编码 引擎

`#ENCODE#UTF-8,GBK`

先按 `UTF-8` encode，然后 `GBK` decode。逗号分割。

### URL unquote引擎

`#UNQUOTE#`

会把数据用unquote处理。

### HRML unescape引擎

`#UNESCAPE#`

将数据用html parse中的unescape处理