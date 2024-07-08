import os
import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn
import torch.optim as optim
import torchvision
from torchvision import transforms, models, datasets
from torch.utils.data import Dataset, DataLoader

import time
import warnings
from torch import nn
from torch.nn import functional as F

warnings.filterwarnings("ignore")
import random
import sys
import copy
import json
from PIL import Image





class ResBlk(nn.Module):
    """
    resnet block
    """

    def __init__(
        self,
        in_channels,
        out_channels,
        stride=[1, 1, 1],
        padding=[0, 1, 0],
        first=False,
    ) -> None:
        """

        :param in_channels:
        :param out_channels:
        """
        super(ResBlk, self).__init__()
        self.bottleneck = nn.Sequential(
            nn.Conv2d(
                in_channels,
                out_channels,
                kernel_size=1,
                stride=stride[0],
                padding=padding[0],
                bias=False,
            ),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(
                out_channels,
                out_channels,
                kernel_size=3,
                stride=stride[1],
                padding=padding[1],
                bias=False,
            ),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(
                out_channels,
                out_channels * 4,
                kernel_size=1,
                stride=stride[2],
                padding=padding[2],
                bias=False,
            ),
            nn.BatchNorm2d(out_channels * 4),
        )
        self.shortcut = nn.Sequential()
        if first:
            self.shortcut = nn.Sequential(
                nn.Conv2d(
                    in_channels,
                    out_channels * 4,
                    kernel_size=1,
                    stride=stride[1],
                    bias=False,
                ),
                nn.BatchNorm2d(out_channels * 4),
            )

    def forward(self, x):
        out = self.bottleneck(x)
        out += self.shortcut(x)
        out = F.relu(out)
        return out


class ResNet50(nn.Module):
    def __init__(self, ResBlk, num_classes=20):
        super(ResNet50, self).__init__()
        self.in_channels = 64
        self.conv1 = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
        )
        # conv2
        self.conv2 = self._make_layer(ResBlk, 64, [[1, 1, 1]] * 3, [[0, 1, 0]] * 3)

        # conv3
        self.conv3 = self._make_layer(
            ResBlk, 128, [[1, 2, 1]] + [[1, 1, 1]] * 3, [[0, 1, 0]] * 4
        )

        # conv4
        self.conv4 = self._make_layer(
            ResBlk, 256, [[1, 2, 1]] + [[1, 1, 1]] * 5, [[0, 1, 0]] * 6
        )

        # conv5
        self.conv5 = self._make_layer(
            ResBlk, 512, [[1, 2, 1]] + [[1, 1, 1]] * 2, [[0, 1, 0]] * 3
        )

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(2048, num_classes)



    def _make_layer(self, block, out_channels, strides, paddings):
        layers = []
        # 用来判断是否为每个block层的第一层
        flag = True
        for i in range(0, len(strides)):
            layers.append(
                block(
                    self.in_channels, out_channels, strides[i], paddings[i], first=flag
                )
            )
            flag = False
            self.in_channels = out_channels * 4
        return nn.Sequential(*layers)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.conv5(out)

        out = self.avgpool(out)
        out = out.reshape(x.shape[0], -1)
        out = self.fc(out)

        return out


model_ft = ResNet50(ResBlk)
