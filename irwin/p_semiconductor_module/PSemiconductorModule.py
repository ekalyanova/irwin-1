from irwin.ApplicationModule import ApplicationModule
from irwin.p_semiconductor_module.callbacks.CalculationOperator import CalculationOperator
from irwin.p_semiconductor_module.callbacks.DonorEnergyCallBackOperator import DonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.SemiconductorMaterialOperator import SemiconductorMaterialOperator
from irwin.p_semiconductor_module.callbacks.TemperatureCallBackOperator import TemperatureCallbackOperator


class PSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            TemperatureCallbackOperator(),
            DonorEnergyCallbackOperator(),
            SemiconductorMaterialOperator(),
            CalculationOperator(),
            # TODO: AcceptorConcentrationCallBackOperator
            # TODO: AcceptorEnergyCallBackOperator
            # ...
            # TODO: Сделать всё аналогично + поправить баг, на  значения не те, что в GUIParameters указаны
        ]

    def __init__(self):
        self.window = None

    def run(self, main_window):
        self.main_window = main_window
        self.connect_all_callbacks()
