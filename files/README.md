# 对舌的标签描述进行编码
    tongue['tongue_proper_color'] = 0  # 舌质颜色 淡红（正常）0 淡白1 红2 暗/紫3
    tongue['tongue_proper_shape_pang'] = 0  # 舌质形态 正常0 胖1  裂纹齿印(太少不用)
    tongue['tongue_proper_shape_neng'] = 0  # 舌质形态 正常0  嫩1
    tongue['tongue_proper_shape_chi'] = 0  # 舌质形态 正常0  有齿痕或齿印 1
    tongue['tongue_moss_color'] = 0  # 苔色白（正常）0 黄1
    tongue['tongue_moss_nature'] = 0  # 苔质 薄（正常）0  少1  腻2
# 文件说明
1、<font color=#46A3FF>tongue_all_features.csv</font>是他们根据原始表格数据整理出的舌像图——编号对应表格，与之对应的文件夹未知<br>
2、<font color=#46A3FF>tongue_all_features_aug.csv</font>是根据（1）原始表格进行数据增广扩充得到的，与之对应的舌像文件夹为<font color=#FFDC35>tongueimage_aug</font>，
其中增广列为<font color=#53FF53>[tongue_proper_color、tongue_proper_shape_pang、tongue_proper_shape_neng、tongue_proper_shape_chi、tongue_moss_nature]</font>
其中与本表无关列，即非增广列为<font color=#AE57A4>[tongue_moss_color]</font><br>
3、<font color=#46A3FF>moss_all_features_aug.csv</font>是根据（1）原始表格对<font color=#53FF53>[tongue_moss_color]</font>列进行增广得到的，与其对应的图像文件夹为<font color=#FFDC35>moss_aug</font>，其他列<font color=#AE57A4>[tongue_proper_color、tongue_proper_shape_pang、tongue_proper_shape_neng、tongue_proper_shape_chi、tongue_moss_nature]</font>是与本表无关的列，即非增广列<br>
# 文件夹说明
4、<font color=#FFDC35>tongueimage_aug</font>与上方1说明对应<br>
5、<font color=#FFDC35>moss_aug</font>与上方2说明对应<br>
6、<font color=#FFDC35>tongue_image_data_set</font>是标签描述编码对应的文件夹分类，内含6个子文件夹类别，与上方编码6行相互对应<br>
7、<font color=#FFDC35>tongue_image_train_test_set</font>是标签描述编码对应的文件夹分类（再次进行训练集、测试集划分得到的，即6对应的训练集、测试集划分），内含6个子文件夹类别，与上方编码6行相互对应<br>