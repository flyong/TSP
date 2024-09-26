# -*- coding: utf-8 -*-
from ts_benchmark.evaluation.strategy.fixed_forecast import FixedForecast
from ts_benchmark.evaluation.strategy.rolling_forecast import RollingForecast

# 这是一个指向固定/滚动预测的模型入口的字典
STRATEGY = {
    "fixed_forecast": FixedForecast,
    "rolling_forecast": RollingForecast,
}
