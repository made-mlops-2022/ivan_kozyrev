from dataclasses import dataclass


@dataclass()
class PredictParam:
    path_2_model: str
    path_2_data: str
    path_2_predict: str
