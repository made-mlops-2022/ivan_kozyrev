from dataclasses import dataclass


@dataclass()
class ModelParam:
    path_2_raw_data_input: str
    path_2_ready_model: str

    model_name: str
    test_size: float
    random_state: int
    max_iter: int
    max_depth: list[int]
    grid: bool
