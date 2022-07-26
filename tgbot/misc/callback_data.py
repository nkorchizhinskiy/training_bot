from aiogram.dispatcher.filters.callback_data import CallbackData


class ExerciseCallbackData(CallbackData, prefix="training_data"):
    training: str


class ChartCallbackData(CallbackData, prefix="chart_data"):
    chart: str

class ExercisePaginationCallbackData(CallbackData, prefix="exercise_pagination_data"):
    page_number: int

