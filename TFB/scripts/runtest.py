# -*- coding: utf-8 -*-
import subprocess

command = [
    "python", "./TFB/scripts/run_benchmark.py",
    "--config-path", "rolling_forecast_config.json",
    "--data-name-list", "gt.csv",
    "--strategy-args", '{"horizon":60}',
    "--model-name", "self_impl.VAR_model",
    "--gpus", "0",
    "--num-workers", "1",
    "--timeout", "60000",
    "--save-path", "ILI/VAR"
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
    '{"horizon":24}',
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

subprocess.run(command2)

# subprocess.run(command)
