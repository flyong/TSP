python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "darts.RNNModel" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/RNN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "darts.RNNModel" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/RNN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "darts.RNNModel" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/RNN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "darts.RNNModel" --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/RNN"

