# pairwise-taa-jitter-reject

## 领域

游戏、图形与多媒体

## 主题

TAA 抖动与历史拒绝

## 说明

时间戳抖动、当帧运动矢量与深度权重。

初始状态下 `graphics/taa_jitter_reject.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
