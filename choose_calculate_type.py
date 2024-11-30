from calculate.calculate_models import calculate_models
from forms.plot_form import create_plot_form
def choose_calculate_type(is_write, is_plot):
        calculate_models(is_write, is_plot)
        if is_plot:
            create_plot_form()
    