# 跑团简易信息界面

> A little tool for COC-Trpg's kp. 

一个自己带 COC 面团时为了方便而编的一个小玩意，简而言之就是把 **日期、星期几、时间、NPC立绘、场景** 集成在一个屏幕区域内。使用时在电脑端编译运行 *main.py*，再利用 拓展屏 or 手机平板上的远程控制软件 将其展示给其他玩家。

前置库需要有 PyQt5. 图片控件的大部分功能参考自 *risemeup/pyside2View*.

**人物** 和 **地点** 选择文件夹后会自动读取文件夹中所有的图片（人物立绘可以用 png 格式），选择好之后按 **APPLY** 键将其应用到右端屏幕上。由于水平所限，如果要取得较好的效果，立绘的长宽比尽量在 1.15 左右，并且如果立绘是 PNG 格式的话，请手动在立绘图的上下左右四个角落点一个不起眼的黑点（否则在图片自动缩放时程序很容易自行忽略掉一部分透明的区域，使用效果会很差）。

**注**：**人物** 文件夹中可以放置一个名叫 *keeper.png/jpg/jpeg* 的立绘图，按 **kp** 键会自动切换成这个默认立绘。立绘图和背景图需有能力的 kp 自行准备。

示例截图：

![QQ截图20220202193835](https://user-images.githubusercontent.com/40653343/152146805-8e7b893c-d100-4d86-b1e1-ee3d07b08afa.jpg)
