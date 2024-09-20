python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Solar.csv" --strategy-args '{"horizon":96}' --model-name "time_series_library.FiLM" --model-hyper-params '{"batch_size": 16, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 20, "patience": 20, "horizon": 96, "seq_len": 192, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Solar/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Solar.csv" --strategy-args '{"horizon":192}' --model-name "time_series_library.FiLM" --model-hyper-params '{"batch_size": 16, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 20, "patience": 20, "horizon": 192, "seq_len": 192, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Solar/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Solar.csv" --strategy-args '{"horizon":336}' --model-name "time_series_library.FiLM" --model-hyper-params '{"batch_size": 16, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 20, "patience": 20, "horizon": 336, "seq_len": 192, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Solar/FiLM"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "Solar.csv" --strategy-args '{"horizon":720}' --model-name "time_series_library.FiLM" --model-hyper-params '{"batch_size": 16, "dropout": 0.05, "factor": 3, "lr": 0.001, "moving_avg": 25, "num_epochs": 20, "patience": 20, "horizon": 720, "seq_len": 192, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "Solar/FiLM"

