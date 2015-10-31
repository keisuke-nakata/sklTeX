# -*- encoding: utf-8 -*-
from string import Template

from sklearn import linear_model
import latex

DOCUMENTCLASS = r"article"
TEMPLATE = Template(
    r"\documentclass{" + DOCUMENTCLASS + r"}"
    r"\begin{document}"
    r"$your_model"
    r"\end{document}"
)

class ModelNotYetFittedError(Exception):
    pass


def skl2tex(model):
    model_type = {
        'ordinary_linear_regression': False,
        'fit_intercept': False
    }

    if isinstance(model, linear_model.LinearRegression):
        if hasattr(model, 'coef_') and (not model.fit_intercept or hasattr(model, 'intercept_')):
            model_type['ordinary_linear_regression'] = True
            model_type['fit_intercept'] = model.fit_intercept
        else:
            raise ModelNotYetFittedError('Cannot find coefficients of your model.')

    latex_model = 'y = '
    if model_type['ordinary_linear_regression']:
        coef_fmt = '{:+.3f}'
        for i, c in enumerate(model.coef_):
            latex_model += (coef_fmt.format(c) + r'x_{' + str(i) + r'}')
        if model_type['fit_intercept']:
            latex_model += coef_fmt.format(model.intercept_)

    your_model = r'$' + latex_model + r'$'
    latex_all = TEMPLATE.substitute(your_model=your_model)

    pdf = latex.build_pdf(latex_all)
    pdf.save_to('temp.pdf')
