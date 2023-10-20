# Data Collection

## How to collect?

1. 每一条数据分为3块内容 id + document + metadata
2. id是每条数据的唯一标识符（不能重复），尽量是这段document的标题，中心内容。请尽量保持简短
3. document是每条数据的主要内容，也是大语言模型的主要依据。这段内容在处理时尽量保持文本的纯度（就是一段文字中尽量是讲一部分的内容）
    同时，尽可能保证这段字数不要过长，
4. metadata是文本元数据（也就是标签），可以是这段文字的类别（简介/校史之类的）

## Data Source

1. wiki: https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6
2. wiki 中山大学校史：https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6%E6%A0%A1%E5%8F%B2
3. 中山大学 博物馆（校史馆）：https://bwgxsg.sysu.edu.cn/zh-hans/academics/topics
4. 中山大学 校史：http://www.sysutt.com/web/xs/column.html#
5. 中山大学 官网: https://www.sysu.edu.cn/xxg/zdjj1.htm
6. baidubaike: https://baike.baidu.com/item/%E4%B8%AD%E5%B1%B1%E5%A4%A7%E5%AD%A6/5672

# Model

1. qianfan: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/xlmokikxe
2. xinghuo: https://www.xfyun.cn/doc/spark/Web.html#_1-%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E
3. qianwen: https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk