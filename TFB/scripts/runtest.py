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

subprocess.run(command)
