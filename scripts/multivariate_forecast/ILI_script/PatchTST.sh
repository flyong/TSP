python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 32, "d_model": 512, "e_layers": 4, "factor": 3, "n_headers": 4, "horizon": 14, "seq_len": 104, "d_ff": 2048}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 32, "d_model": 512, "e_layers": 4, "factor": 3, "n_headers": 4, "horizon": 21, "seq_len": 104, "d_ff": 2048}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 32, "d_model": 512, "e_layers": 4, "factor": 3, "n_headers": 4, "horizon": 28, "seq_len": 104, "d_ff": 2048}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 32, "d_model": 512, "e_layers": 4, "factor": 3, "n_headers": 16, "horizon": 36, "seq_len": 104, "d_ff": 2048}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/PatchTST"

