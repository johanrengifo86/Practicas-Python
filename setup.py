from setuptools import setup

setup(
    name='paquetecalculos',
    version = '1.0',
    description='Paquete de redondeo y potencia',
    author='J.Rengifo',
    author_email='wrengifo@unicauca.edu.co',
    url = 'wrengifo.com',
    packages=['c11_Paquetes','calculos','calculos.redondeo_potencia']

# en cmd de windows <C:\Users\Stark\Documents\PracticasPython> python setup.py sdist>
# crea dos carpetas -<dist> y <paquetescalculos.egg-info> en la raiz 
#====================================
# Instalacion del paquete
# ===================================
# Nos ubicamos en la carpeta dist
#     - C:\Users\Stark\Documents\PracticasPython>cd dist
# C:\Users\Stark\Documents\PracticasPython\dist>pip install paquetecalculos-1.0.tar.gz
# Para Desisntalar se usa el comando <pip uninstall 'nombre del paquete'>
)