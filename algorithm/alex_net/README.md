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
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_proper_color</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.797[train_loss: 0.610  val_accuracy: 0.797]<br>
2、<font color=#FFDC35>tongue_shape_pang</font>文件夹内的模型对【舌质形态 正常0 胖1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_pang</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_pang</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.901[train_loss: 0.266  val_accuracy: 0.901]<br>
3、<font color=#FFDC35>tongue_shape_neng</font>文件夹内的模型对【舌质形态 正常0 胖1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_neng</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_neng</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.963[train_loss: 0.134  val_accuracy: 0.963]<br>
4、<font color=#FFDC35>tongue_shape_chi</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_shape_chi</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_shape_chi</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.980[train_loss: 0.090  val_accuracy: 0.980]<br>
5、<font color=#FFDC35>tongue_moss_color</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_moss_color</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_moss_color</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.910[train_loss: 0.383  val_accuracy: 0.910]<br>
6、<font color=#FFDC35>tongue_moss_nature</font>文件夹内的模型对【舌质形态 正常0  有齿痕或齿印 1】进行分类，训练测试数据来自于<font color=#FFDC35>tongue_image_train_test_set // tongue_moss_nature</font>文件夹，
它是由原始增广文件夹<font color=#FFDC35>tongue_image_data_set // tongue_moss_nature</font>进行[8:2]——训练集：测试集划分得到的，其中测试集上验证准确率为0.825[train_loss: 0.435  val_accuracy: 0.825]<br>

#存在的问题
1、舌头跟口没有切割出来，影响学习效果
2、数据不平衡，分类中少量的类的图片数量太少，准确率参考价值不大，得做数据扩充，后面再说
3、分类的舌苔等特征——疾病关联没有对应标签