import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def logica(saborInput, porcionInput):
    # Identificación de variables nítidas:
    sabor = ctrl.Antecedent(np.arange(0, 100, 1), 'sabor')
    porcion = ctrl.Antecedent(np.arange(0, 100, 1), 'porcion')
    precio = ctrl.Consequent(np.arange(40, 340, 1), 'precio')

    # Identificación de variables lingüísticas
    # https://pythonhosted.org/scikit-fuzzy/api/skfuzzy.membership.html
    # Pythonic API

    # Variable lingüística: Sabor
    # Sabor Preferente
    # Cantidad de comida
    sabor['dulce'] = fuzz.trimf(sabor.universe, [0, 0, 25])  # Medio Trapezoidal
    sabor['agridulce'] = fuzz.trapmf(sabor.universe, [5, 20, 35, 50])  # Trapezoidal
    sabor['picante'] = fuzz.trapmf(sabor.universe, [30, 45, 60, 75])  # Trapezoidal
    sabor['salado'] = fuzz.trimf(sabor.universe, [65, 100, 100])  # Medio Trapezoidal

    # Variable lingüística: Porcion
    # Cantidad de comida
    porcion['chica'] = fuzz.trimf(porcion.universe, [0, 0, 40])  # Triangular
    porcion['mediana'] = fuzz.trapmf(porcion.universe, [20, 35, 65, 75])  # Trapezoidal
    porcion['grande'] = fuzz.trimf(porcion.universe, [70, 100, 100])  # Trapezoidal

    # Variable lingüística: Precio
    # Precio recomendado para vender
    precio['barato'] = fuzz.trimf(precio.universe, [10, 40, 100])  # Triangular
    precio['regular'] = fuzz.trapmf(precio.universe, [90, 130, 170, 210]) # Triangular
    precio['costoso'] = fuzz.trapmf(precio.universe, [180, 215, 250, 275])  # Triangular
    precio['muy costoso'] = fuzz.trimf(precio.universe, [260, 300, 340])  # Medio Trapezoide

    #sabor.view()
    #plt.show()

    regla1 = ctrl.Rule(porcion['chica'] | sabor['dulce'], precio['barato'])
    regla2 = ctrl.Rule(sabor['agridulce'] | porcion['mediana'], precio['regular'])
    regla3 = ctrl.Rule(porcion['mediana'] | sabor['picante'], precio['costoso'])
    regla4 = ctrl.Rule(sabor['salado'] | porcion['grande'], precio['muy costoso'])

    #regla1.view()
    #plt.show()

    precio_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4])
    precioRES = ctrl.ControlSystemSimulation(precio_ctrl)

    precioRES.input['sabor'] = saborInput
    precioRES.input['porcion'] = porcionInput

    precioRES.compute()

    global precioFinal
    precioFinal = round(precioRES.output['precio'])
    return precioFinal
