python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/VAR"


