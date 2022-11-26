from dataclasses import dataclass
from .data_param import InputDataParam
from .model_param import ModelParam


@dataclass()
class MainParam:
    path_2_raw_data_input: str
    path_2_eda_file: str
    path_2_ready_model: str

    test_size: int
    random_state: int

    param_4_input_data: InputDataParam
    model: ModelParam
