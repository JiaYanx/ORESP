# ORESP
ORESP：基于有序回归的软件缺陷严重程度预测方法

该方法首先使用基于Spearman的特征选择方法来尝试移除数据集内的冗余特征，然后利用基于比例优势模型（proportional odds model）的神经网络[2]对软件项目中模块的严重程度进行预测，该模型将比例优势模型[3]引入到神经网络的输出层，一方面可以保留神经网络模型多分类的优势，另一方面因为比例优势模型中累计和的思想，可通过阈值的限定考虑标签间的次序性。

与之前研究工作的不同点在于对软件缺陷严重程度的预测不仅考虑到分类且考虑到类别间的次序。

[2]	 Gutierrez P A, Perezortiz M, Sanchezmonedero J, et al. Ordinal regression methods: survey and experimental study[J]. IEEE Transactions on Knowledge and Data Engineering, 2016, 28(1): 127-146.

[3]	 McCullagh, P.: Regression models for ordinal data (with discussion). Journal of the Royal Statistical Society 42(2), 109–142 (1980).
