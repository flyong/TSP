
exit 0
# python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "time_series_library.TimesNet" --model-hyper-params '{"d_ff": 768, "d_model": 768, "factor": 3, "horizon": 14, "seq_len": 36, "top_k": 5}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TimesNet"

# python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "time_series_library.TimesNet" --model-hyper-params '{"d_ff": 768, "d_model": 768, "factor": 3, "horizon": 21, "seq_len": 36, "top_k": 5}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TimesNet"

# python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "time_series_library.TimesNet" --model-hyper-params '{"d_ff": 768, "d_model": 768, "factor": 3, "horizon": 28, "seq_len": 104, "top_k": 5}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TimesNet"

# python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "time_series_library.TimesNet" --model-hyper-params '{"d_ff": 768, "d_model": 768, "factor": 3, "horizon": 36, "seq_len": 36, "top_k": 5}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TimesNet"


