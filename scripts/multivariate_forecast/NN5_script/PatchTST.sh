python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NN5.csv" --strategy-args '{"horizon":24}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 8, "d_ff": 32, "d_model": 16, "dropout": 0.2, "e_layers": 3, "lr": 0.0025, "n_heads": 4, "num_epochs": 100, "patch_len": 24, "patience": 10, "horizon": 24, "seq_len": 104, "stride": 2}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "NN5/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NN5.csv" --strategy-args '{"horizon":36}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 8, "d_ff": 32, "d_model": 16, "dropout": 0.2, "e_layers": 3, "lr": 0.0025, "n_heads": 4, "num_epochs": 100, "patch_len": 24, "patience": 10, "horizon": 36, "seq_len": 104, "stride": 2}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "NN5/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NN5.csv" --strategy-args '{"horizon":48}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 8, "d_ff": 32, "d_model": 16, "dropout": 0.2, "e_layers": 3, "lr": 0.0025, "n_heads": 4, "num_epochs": 100, "patch_len": 24, "patience": 10, "horizon": 48, "seq_len": 104, "stride": 2}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "NN5/PatchTST"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NN5.csv" --strategy-args '{"horizon":60}' --model-name "time_series_library.PatchTST" --model-hyper-params '{"batch_size": 8, "d_ff": 32, "d_model": 16, "dropout": 0.2, "e_layers": 3, "lr": 0.0025, "n_heads": 4, "num_epochs": 100, "patch_len": 24, "patience": 10, "horizon": 60, "seq_len": 104, "stride": 2}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "NN5/PatchTST"
