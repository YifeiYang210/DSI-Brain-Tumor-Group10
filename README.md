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



|      | 模型                       | epoch | val_loss     | val_accuracy  |
| ---- | -------------------------- | ----- | ------------ | ------------- |
| 分类 | VGG                        | 20    | 0.2813       | 0.941         |
|      | VGG                        | 50    | 0.3201       | 0.943         |
|      | VGG(+pretrain)             | 15    | 0.2335       | 0.954         |
|      | ResNet50V2                 | ?     | ?            | 0.994         |
|      |                            |       |              |               |
|      |                            | epoch | val_accuracy | test_accuracy |
| 分割 | Unet                       | 25    | 87.68        | 82.00         |
|      | Unet(VGG19+ImageNet)       | 68    | 93.58        | **82.29**     |
|      | Unet(ResNet152V2+ImageNet) | 28    | 91.58        | 82.08         |
|      | Unet++(4depth)             | 15    | 78.65        | 68.02         |
|      | Unet++(4depth+ResNet50)    | 25    | 65.98        | 69.56         |
|      | Unet++(4depth+ResNet50V2)  | 26    | 82.51        | 73.24         |
|      | Unet++(5depth)             | 30    | 94.03        | 71.38         |
|      | Unet+++(5depth+vgg19)      | 73    | 90.11        | 81.86         |



### 3.**代码环境**



------



代码配置环境：tensorflow >= 2.3.0

我的配置环境(仅供参考)：python3.6，tensorflow(gpu)版本2.1.0，cuda10.1，cudnn8.0



------

### 4.**鸣谢**

Imperial College London, [ZJU-GiveLab](https://github.com/ZJUGiveLab/UNet-Version),[keras-unet-collection](https://github.com/yingkaisha/keras-unet-collection)