python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":14}' --model-name "darts.TCNModel" --model-hyper-params '{"input_chunk_length": 512, "n_epochs": 100, "output_chunk_length": 96}' --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TCN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":21}' --model-name "darts.TCNModel" --model-hyper-params '{"input_chunk_length": 104, "n_epochs": 10, "output_chunk_length": 36}' --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TCN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":28}' --model-name "darts.TCNModel" --model-hyper-params '{"input_chunk_length": 104, "n_epochs": 10, "output_chunk_length": 48}' --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TCN"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "TSA1-26.csv" --strategy-args '{"horizon":36}' --model-name "darts.TCNModel" --model-hyper-params '{"input_chunk_length": 104, "n_epochs": 10, "output_chunk_length": 60}' --gpus 0  --num-workers 1  --timeout 60000  --save-path "ILI/TCN"

