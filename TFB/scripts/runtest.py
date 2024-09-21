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

command2 = [
    "python", "./TFB/scripts/run_benchmark.py",
    "--config-path", "rolling_forecast_config.json",
    "--data-name-list", "gt.csv",
    "--strategy-args", '{"horizon":24}',
    "--model-name", "time_series_library.TimesNet",
    "--model-hyper-params", '{"d_ff": 768, "d_model": 768, "factor": 3, "horizon": 24, "seq_len": 36, "top_k": 5}',
    "--adapter", "transformer_adapter",
    "--gpus", "0",
    "--num-workers", "1",
    "--timeout", "60000",
    "--save-path", "ILI/TimesNet"
]

subprocess.run(command2)

# subprocess.run(command)
