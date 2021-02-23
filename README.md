# DSI brain tumor task (Group10)

### **1.分工**



------



时间 | 2021年2月23日结题

参与人员 |  李春一、李国耀、李瑞珊、王雅娟、韦婉笛、薛玮嘉、杨逸飞 （字母序）



任务A. 答辩(包括PPT和presentation以及演讲稿撰写等)

任务B. 分类任务,跑通现有代码 (有服务器同学可以尝试1预训练模型/2ResNet/3DenseNet)

任务C. 分割任务,创新 (有服务器同学可以尝试分割任务最新模型，使用源码/复现论文)



补充：

- 1.对于分类任务，我们的工作可以是：尝试了工业界比较稳定的上线业务方案，实验结果证明，对于任何分类任务都很有效（仅参考）
- 2.对于分割任务，我们的工作可以是：通过尝试改进原有模型分割，使用了XXX/提出了XXX，实验证明是很有效的（仅参考）
- 3.使用了一些tricks作为辅助：何凯明的初始化方法，增强数据集（可选）

 

------



| **任务** | **分工**               |      |
| -------- | ---------------------- | ---- |
| **A**    | 李春一，薛玮嘉         |      |
| **B**    | 李瑞珊，王雅娟         |      |
| **C**    | 韦婉笛，杨逸飞，李国耀 |      |



### **2.实验结果(随时更新)**



------



|      | Model                     | epoch | val_accuracy | test_accuracy |
| ---- | -------------------------- | ----- | ------------ | ------------- |
| 分类 | VGG16                      | 20    | 94.1 | 90       |
|      | VGG16                      | 50    | 94.3 | 90       |
|      | VGG16(+pretrain)           | 15    | 95.4 | 90       |
|      | ResNet50V2                 | 100   | **99.4** (?) | 89       |
| | **VGG19(+aug)** | 30 | 94.6 | **92** |
|      |                            |       |              |               |
|      |                            | epoch | val_accuracy | test_accuracy |
| 分割 | Unet                       | 25    | 82.00   | **80**   |
|      | Unet(VGG19+ImageNet)       | 68    | **82.29** | 78 |
|      | Unet(ResNet152V2+ImageNet) | 28    | 82.08   | 78            |
|      | Unet++(4depth)             | 15    | 68.02   | 71       |
|      | Unet++(4depth+ResNet50)    | 25    | 69.56   | 75       |
|      | Unet++(4depth+ResNet50V2)  | 26    | 73.24   | 77      |
|      | Unet++(5depth)             | 30    | 71.38   | 76      |
|      | Unet+++(5depth+vgg19)      | 73    | 81.86   | 78       |



### 3.**代码环境**



------



代码配置环境：tensorflow >= 2.3.0

我的配置环境(仅供参考)：python3.6，tensorflow(gpu)版本2.1.0，cuda10.1，cudnn8.0



------

### 4.**鸣谢**

Imperial College London, [ZJU-GiveLab](https://github.com/ZJUGiveLab/UNet-Version),[keras-unet-collection](https://github.com/yingkaisha/keras-unet-collection)