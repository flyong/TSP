python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "time_series_library.iTransformer" --model-hyper-params '{"factor": 3, "horizon": 14, "lr": 0.001, "seq_len": 104, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 5  --num-workers 1  --timeout 60000  --save-path "ILI/iTransformer"&

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "time_series_library.iTransformer" --model-hyper-params '{"d_ff": 2048, "d_model": 512, "lr": 0.001, "horizon": 21, "seq_len": 104}' --adapter "transformer_adapter"  --gpus 5  --num-workers 1  --timeout 60000  --save-path "ILI/iTransformer"&

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "time_series_library.iTransformer" --model-hyper-params '{"factor": 3, "horizon": 28, "lr": 0.001, "seq_len": 104, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 5  --num-workers 1  --timeout 60000  --save-path "ILI/iTransformer"&

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "time_series_library.iTransformer" --model-hyper-params '{"factor": 3, "horizon": 36, "lr": 0.001, "seq_len": 104, "d_ff": 2048, "d_model": 512}' --adapter "transformer_adapter"  --gpus 5  --num-workers 1  --timeout 60000  --save-path "ILI/iTransformer"&




