# faceswap

基于这个项目：

[https://github.com/matthewearl/faceswap](https://github.com/matthewearl/faceswap)


我只是做了一个页面demo。


客户端用`vue`做的，切换到client目录，`npm install` 然后 `npm run dev`就能跑了。

服务端用`bottle.py`做的，可以使用pip安装，切换到server目录，执行`server.py`。


`faceswap.py`的模块依赖可以参考原始项目的说明，opencv和numpy用pip安装就好了，dlib稍微麻烦一点。

印象中ubuntu需要这样

```
sudo apt install build-essential cmake
sudo apt install libgtk-3-de
sudo apt install libboost-all-devstep
sudo -H pip install dlib
```
