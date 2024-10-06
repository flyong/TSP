#!/bin/bash

# Directory containing the bash scripts
SCRIPT_DIR="/home/vsc/TSP/scripts/multivariate_forecast/ILI_script"

# Loop through each bash script in the directory and execute it
for script in "$SCRIPT_DIR"/*.sh; do
    
    echo "Running $script..."
    bash "$script"
done