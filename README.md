# Chroma 向量数据库测试

## 依赖

本程序需要以下依赖。

* pandas: 用于导入csv数据
* openai: 用于调用ChatGPT的API
* chroma: 向量数据库
* sentence-transformers: 中文Sentence Embedding

> 前面两个可以使用conda安装，后面两个需要用pip安装
> 
> 在第一次运行时，会自动下载所需要的中文Embedding模型从 

## 配置密钥

由于需要调用ChatGPT的API，所以我需要配置密钥。

配置方法：请在项目的根目录下创建文件`config.json`，并输入以下内容

```json
{
    "api-key": "sk-xxx"
}
```

## 启动

在项目根目录下在命令行中输入以下指令即可运行
```bash
python3 src/main.py
```
