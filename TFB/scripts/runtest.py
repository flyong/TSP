# -*- coding: utf-8 -*-
import subprocess

command = [
    "python",
    "./TFB/scripts/run_benchmark.py",
    "--config-path",
    "rolling_forecast_config.json",
    "--data-name-list",
    "gt.csv",
    "--strategy-args",
    '{"horizon":60}',
    "--model-name",
    "self_impl.VAR_model",
    "--gpus",
    "0",
    "--num-workers",
    "1",
    "--timeout",
    "60000",
    "--save-path",
    "ILI/VAR",
]

command1=[
    "python", "./TFB/scripts/run_benchmark.py",
    "--config-path", "fixed_forecast_config_daily.json",
    "--data-name-list", "gt.csv",
    "--strategy-args", '{"horizon":60}',
    "--model-name", "self_impl.VAR_model",
    "--gpus", "0",
    "--num-workers", "1",
    "--timeout", "60000",
    "--save-path", "ILI/VAR"
]
path = "./TFB/scripts/run_benchmark.py"

command2 = [
    "python",
    "./TFB/scripts/run_benchmark.py",
    "--config-path",
    "rolling_forecast_config.json",
    "--data-name-list",
    "gt.csv",
    "--strategy-args",
    '{"horizon":45}',
    "--model-name",
    "time_series_library.NLinear",
    "--model-hyper-params",
    '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 36}',
    "--adapter",
    "transformer_adapter",
    "--gpus",
    "0",
    "--num-workers",
    "1",
    "--timeout",
    "60000",
    "--save-path",
    "FRED/NLinear",
]

command3 = [
    "python",
    "./TFB/scripts/run_benchmark.py",
    "--config-path",
    "rolling_forecast_config.json",
    "--data-name-list",
    "gt.csv",
    "--strategy-args",
    '{"horizon":24}',
    "--model-name",
    "time_series_library.NLinear",
    "--model-hyper-params",
    '{"k": 2, "horizon": 96, "seq_len": 336, "d_ff": 64, "d_model": 8,"num_nodes":11, "learning_rate":0.0005, "batch_size":256, "gpu":6, "patch_size_list":[[42, 24, 12, 16],[42, 28, 16, 12], [16, 28, 12, 42]]}',
    "--adapter",
    "transformer_adapter",
    "--gpus",
    "0",
    "--num-workers",
    "1",
    "--timeout",
    "60000",
    "--save-path",
    "FRED/NLinear",
]

subprocess.run(command)

# subprocess.run(command)
