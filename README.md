# 共享误差分块条件化与协方差读回

`data/record.json` 是 共享误差分块条件化与协方差读回 使用的本地合成交换样本。数组按 JSON 的下标顺序排列。本文的坐标、单位和枚举约定与该记录配套。记录中如果有 `scale` 或 `limits`，对应同一输入协议的部署规格。

precision 和 information 表示局部密度 exp(-xᵀJx/2 + hᵀx) 的 J 及 h，半正定因子允许。观测是所列变量加高斯噪声，noise 是误差的协方差矩阵，mask=0 代表测量时该分量缺失。exact 表示直接约束变量取值。remove_factor 按稳定因子 ID 撤离该项，包括此前识别为等价重传的副本。查询前两列指定所需边缘及交叉项，末列为第一变量的方差限值。只在查询变量能唯一确定时给出均值和协方差，固定变量的协方差为零。 source 是发布因子的标定工位，稳定因子 ID 以发布清单为准。reverse_reads 用已应用的 operations 项数定位观测集合，梯度张量按 query 所列变量的顺序排列。

## 读取样本

使用 Python 3.11 或 3.12，并在虚拟环境安装锁定依赖。读取入口返回原始记录。作为命令运行时，它会列出各顶层输入项目以及 NumPy 版本。

```sh
python -m pip install -r requirements.txt
python -m separator_gaussian_input
python -m unittest discover -s tests -v
```

测试读取交换样本，核对其中的张量尺寸、标识与数据约定。
