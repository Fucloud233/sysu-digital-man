# 中大介绍官

本项目是在[Fay](https://github.com/TheRamU/Fay)开源数字人项目的基础上开发而成的，
针对LLM部分进行了修改和优化，重构了调用不同LLM的逻辑，并引入了向量数据库，
因此实现一个全自动的24小时在线的中大介绍官。

## 使用说明

### 1. 安装依赖

请使用一下指令安装Fay项目所需要的原来。

``` bash
$ pip install -r requirement.txt
```

同时，为了调用LLM增强部分的内容，请安装以下额外依赖。

* pandas: 用于导入csv数据
* openai: 用于调用ChatGPT的API
* chroma: 向量数据库
* sentence-transformers: Sentence Embedding模型

> 由于依赖管理较乱，可能会安装多余的库，或少安装了某些库，
> 请根据实际情况进行调整。

### 2. 配置密钥

由于本项目调用了很多云服务，所以需要配置好调用API所需要的key。

复制项目根目录下的`system.example.conf`中的内容到`system.conf`，
并按照需求填写对应的key即可。

注意事项：

1. 如果填写了ali的ASR密钥，TTS部分也会调用ali的api
2. LLM部分只实现了`chatgpt`, `rwkv_api`, `qianfan`

### 3. 运行

若想完全启动本项目的全功能，还需要配合UE5使用，在此就不提供使用方法了。
以下，我们提供提供了控制器运行和CLI运行两种方式。

#### (1) 控制器运行

在该模式下，不仅可以对话，还可以启动TTS服务。

1. 输入 `python main.py`
2. 点击窗口左下角的链接按钮
3. 若左上角提示链接成功，则说明运行成功
4. 在右边的聊天框中输入问题，并按`Ask`发送

#### (2) CLI运行

我们也提供了一个直接调用LLM模块的接口，
以此方便调试LLM模块的功能。

1. 输入 `python src/test_gpt.py`
2. 直接输入问题，并回车
3. 输入`exit` 退出