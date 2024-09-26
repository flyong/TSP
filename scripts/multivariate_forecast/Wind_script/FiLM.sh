python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Wind.csv" --strategy-args '{"horizon":96}' --model-name "time_series_library.FiLM" --model-hyper-params '{"d_ff": 64, "d_model": 32, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 15, "patience": 15, "horizon": 96, "seq_len": 336}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Wind/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Wind.csv" --strategy-args '{"horizon":192}' --model-name "time_series_library.FiLM" --model-hyper-params '{"d_ff": 64, "d_model": 32, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 15, "patience": 15, "horizon": 192, "seq_len": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Wind/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Wind.csv" --strategy-args '{"horizon":336}' --model-name "time_series_library.FiLM" --model-hyper-params '{"d_ff": 64, "d_model": 32, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 15, "patience": 15, "horizon": 336, "seq_len": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Wind/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Wind.csv" --strategy-args '{"horizon":720}' --model-name "time_series_library.FiLM" --model-hyper-params '{"dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 15, "patience": 15, "horizon": 720, "seq_len": 720, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Wind/FiLM"
