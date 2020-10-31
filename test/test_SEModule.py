import torch
import torch.nn as nn
from glasses.nn.att import SpatialChannelSE, ChannelSE, SpatialSE, ECAModule

def test_att():
    x = torch.rand(1,48,8,8)

    se = SpatialSE(x.shape[1])
    res = se(x)

    assert res.shape == x.shape

    se = SpatialSE(x.shape[1], reduced_features=10)

    assert se.att.fc1.out_features == 10

    se = ChannelSE(x.shape[1])
    res = se(x)

    assert res.shape == x.shape

    se = SpatialChannelSE(x.shape[1])
    res = se(x)

    assert res.shape == x.shape
 

    eca = ECAModule(x.shape[1])

    res = se(x)
    assert res.shape == x.shape
    
