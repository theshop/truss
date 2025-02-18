from typing import Any, Dict, List

from model.dalle_mini_model import DallEModel


class Model:
    def __init__(self, **kwargs) -> None:
        self._data_dir = kwargs["data_dir"]
        self._config = kwargs["config"]
        self._model = None

    def load(self):
        # Load model here and assign to self._model.
        self._model = DallEModel()

    def predict(self, model_input: Any) -> Dict[str, List]:
        model_output = {}
        # Invoke model and calculate predictions here.
        model_output["predictions"] = self._model.predict(model_input)
        return model_output
