#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from numpy import mat, shape, ones, array, arange
from numpy.ma import exp


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))

    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))


# 梯度上升
def gradAscent(dataMatIn, classLabels):
    """
    :param dataMatIn: n行3列 样本
    :param classLabels: n行1列 标签
    :return: weights: 回归系数
    """
    # 转成矩阵类型
    dataMatrix = mat(dataMatIn)
    # 矩阵转置 n列1行
    labelMat = mat(classLabels).transpose()
    # 获取矩阵的行数与列数
    m, n = shape(dataMatrix)
    # 步长
    alpha = 0.0001
    # 迭代次数
    maxCycles = 500

    print "m:", m, "n:", n

    # 创建3行1列的单位矩阵
    weights = ones((n, 1))

    for k in range(maxCycles):
        # n行1列 使用sigmoid只是为了得到一个0～1之间的数值
        h = sigmoid(dataMatrix * weights)
        # 真实类别与预测类别的差值
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error

    return weights


def stocGradAscent0(dataMatrix, classLabels):
    m, n = shape(dataMatrix)
    alpha = 0.01
    # 生成包含n个1的一维数组
    weights = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]

    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []

    for i in range(n):
        # 分类为 1
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        # 分类为0
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')

    # x表示X1，y表示X2
    x = arange(-3.0, 3.0, 0.1)
    # x0 = 1，表达式为：
    # 0 = w0x0 + w1x1 + w2x2
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

