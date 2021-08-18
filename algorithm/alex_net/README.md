# 对舌的标签描述进行编码
    tongue['tongue_proper_color'] = 0  # 舌质颜色 淡红（正常）0 淡白1 红2 暗/紫3
    tongue['tongue_proper_shape_pang'] = 0  # 舌质形态 正常0 胖1  裂纹齿印(太少不用)
    tongue['tongue_proper_shape_neng'] = 0  # 舌质形态 正常0  嫩1
    tongue['tongue_proper_shape_chi'] = 0  # 舌质形态 正常0  有齿痕或齿印 1
    tongue['tongue_moss_color'] = 0  # 苔色白（正常）0 黄1
    tongue['tongue_moss_nature'] = 0  # 苔质 薄（正常）0  少1  腻2
# 文件夹说明
模型文件夹里面对应的6个子文件夹，就是与上方编码相互对应的，单行一个子模型进行单独任务的分类，其中：<br>
1、<font color=#FFDC35>tongue_proper_color</font>文件夹内的模型对【舌质颜色 淡红（正常）0 淡白1 红2 暗/紫3】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_proper_color</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_proper_color</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.945[train_loss: 0.314  val_accuracy: 0.945]<br>
2、<font color=#FFDC35>tongue_shape_pang</font>文件夹内的模型对【舌质形态 正常0 胖1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_pang</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_pang</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.947[train_loss: 0.193  val_accuracy: 0.947]<br>
3、<font color=#FFDC35>tongue_shape_neng</font>文件夹内的模型对【舌质形态 正常0 胖1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_neng</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_neng</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.965[train_loss: 0.179  val_accuracy: 0.965]<br>
4、<font color=#FFDC35>tongue_shape_chi</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_chi</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_chi</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.972[train_loss: 0.150  val_accuracy: 0.972]<br>
5、<font color=#FFDC35>tongue_moss_color</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_moss_color</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_moss_color</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.962[train_loss: 0.186  val_accuracy: 0.962]<br>
6、<font color=#FFDC35>tongue_moss_nature</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_moss_nature</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_moss_nature</font>进行[7:3]——训练集：测试集划分得到的，其中测试集上验证准确率为0.928[train_loss: 0.309  val_accuracy: 0.928]<br>

#标签提取与数据扩充
对舌的诊断描述（医生记录的一句话）提取的标签<br>
1、舌质颜色：<br>
提取出四个类别（四分类） ：（1）淡红（正常）；（2）淡白；（3）红；（4）暗/紫；<br>
扩充后各分类图片比例分布：【淡红：淡白：红：暗/紫】=【10010：10464：10395：10050】<br>
2、舌质形态是否为胖舌：<br>
提取出两个类别：（1）正常；（2）胖舌；<br>
扩充后各分类图片比例分布：【正常：胖舌】=【10904：10014】<br>
3、舌质形态是否为嫩舌：<br>
提取出两个类别：（1）正常；（2）嫩舌；<br>
扩充后各分类图片比例分布：【正常：嫩舌】=【10178：10030】<br>
4、舌质形态是否有齿痕齿印：<br>
提取出两个类别：（1）正常；（2）有齿痕/齿印；<br>
扩充后各分类图片比例分布：【正常：有齿痕/齿印】=【10353：10030】<br>
5、舌苔颜色：<br>
提取出两个类别：（1）白（正常）；（2）黄；<br>
扩充后各分类图片比例分布：【白：黄】=【9958：9933】<br>
6、苔质：<br>
提取出三个类别：（1）薄（正常）；（2）少；（3）腻；<br>
扩充后各分类图片比例分布：【薄：少：腻】=【10476：10200：10080】<br>
训练集与测试集划分比例为7:3<br>

#存在的问题
1、舌头跟口没有检测框出来，影响学习效果。<br>
2、数据不平衡，分类中少量的类的图片数量太少，准确率参考价值不大，得做数据扩充，后面再说。<br>
3、分类的舌苔等特征——疾病关联没有对应标签，标签为医生描述语句，只能从诊断描述中提取共性多的几个特征标签。<br>

#后期改进
1、加入舌头是否存在的检测、识别、分类。<br>
2、加入目标检测算法，将口舌区域框出来，缩小学习范围。<br>
3、胖舌、嫩舌、齿痕/齿印，三个特征不能合并为3个类别，因为其中各分类图片是有相互交集的关系，可能这几个特征会同时出现<br>