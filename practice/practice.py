from darts.datasets import WeatherDataset
from darts.models import TCNModel

series = WeatherDataset().load()

target = series["p (mbar)"][:100]

past_cov = series["rain (mm)"][:100]

model = TCNModel(
    input_chunk_length=12,
    output_chunk_length=6,
    n_epochs=20,
)

model.fit(target, past_covariates=past_cov)

pred = model.predict(6)
print(pred.values())
