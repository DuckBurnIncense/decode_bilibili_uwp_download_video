# 解密b站UWP最新版下载的视频  

## 闲话  

起因是我在b站发了一条用b站UWP下载b站视频的视频(禁止套娃)  

视频链接: https://www.bilibili.com/video/BV1WU4y1A7q1  

然后近日发现有反馈说下下来无法播放  

然后发现b站UWP版似乎从2.14.72.0起下载的视频就被加密了  

只有用它的播放器才能打开  

于是我就又发了一条视频教大家如何降级b站UWP  

然后又有人说降级后因微软商店的缘故会自动升级... 

我也懒得管了  

但这几天实在是无聊

就简单研究了一下它的加密算法  

发现加密方法就是在(下载下来的视频)头部添加三个十六进制的"FF" (反正恶心你的操作是达成了)  

(用WinHex即可轻松发现)  

于是为了满足b站小伙伴们的需求  

我就把用WinHex解密的方法发在了b站(审核还能过就离谱)  

视频链接: https://www.bilibili.com/video/BV1eS4y1U7LS  

然后又有人说不方便, 还有人说想要批量解密  

于是就有了这个工具  

## 文件说明  

```
bili.py                   #源码
快捷解密b站视频.exe        #编译后
WinHex_v20.4_x86_x64.exe  #调试工具WinHex(green版
README.md                 #就是你现在正在看的这个说明文件
```

## 使用说明  

https://www.bilibili.com/video/BV1cP4y1T7ou  

↑这是编译好那个exe的使用说明↑  

整体来说就是把需解密的(多个)视频拖到图标里打开  

命令行类似于这样子: 

```
快捷解密b站视频.exe "C:\\video1.mp4" "D:\\Videos\\2333.mp4" "E:\\path\\to\\the\\video.mp4"
```

## 源码说明  

莫得, 这么简单还要说明(￣ε(#￣)  

(不会真的有人无聊到把我的源码再编译一遍吧)  

## 更新记录  

2022-04-04: 创建项目;  

2022-04-05: 发现好像描述里的```UWP```手滑打成了```UPW```了 ＞︿＜;  

2022-04-07: 更新: 支持批量处理 (一次性拖入多个文件) .

 
