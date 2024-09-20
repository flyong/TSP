python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "gt.csv" --strategy-args '{"horizon":24}' --model-name "time_series_library.DLinear" --model-hyper-params '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/DLinear"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "gt.csv" --strategy-args '{"horizon":24}' --model-name "time_series_library.DLinear" --model-hyper-params '{"batch_size": 16, "d_ff": 512, "d_model": 256, "lr": 0.01, "horizon": 24, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/DLinear"

