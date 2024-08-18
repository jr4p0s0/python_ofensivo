# Diferencias entre python2 y python3 y PIP2 y PIP3

## Python 2

- Python 2.7 es la última versión de Python 2.
- Python 2.7 no tiene soporte oficial desde el 1 de enero de 2020.
- Python 2.7 no recibe actualizaciones de seguridad.

Hay varias diferencias en cuanto al tratamiento de operaciones y funciones entre Python 2 y Python 3. Algunas de las diferencias más notables son:

- En Python 2, `print` es una declaración, mientras que en Python 3 es una función.
- En Python 2, `range()` devuelve una lista, mientras que en Python 3 devuelve un objeto de rango.
- En Python 2, `input()` evalúa la entrada como una expresión, mientras que en Python 3, `input()` siempre devuelve una cadena.
- En python 2, una operacion de division entre dos enteros devuelve un entero, mientras que en python 3 devuelve un float.
- En Python 2, `xrange()` se utiliza para generar un rango de valores, mientras que en Python 3, `xrange()` se ha eliminado y `range()` se utiliza para generar un rango de valores.
- En Python 2, `unicode` es una función incorporada, mientras que en Python 3, `unicode` se ha eliminado y `str` se utiliza para representar cadenas de texto.

## Python 3

- Python 3 es la versión actual de Python.
- Python 3 es el futuro de Python y se recomienda su uso para nuevos proyectos.
- Python 3 tiene un soporte activo y continuo.
- Python 3 es más eficiente y tiene más características que Python 2.

## PIP2 y PIP3

- PIP2 es el administrador de paquetes para Python 2.
- PIP3 es el administrador de paquetes para Python 3.
- PIP2 y PIP3 se pueden instalar en el mismo sistema y se pueden usar juntos sin problemas.
- PIP2 y PIP3 se pueden usar para instalar paquetes específicos de Python 2 y Python 3, respectivamente.
- PIP2 y PIP3 se pueden usar para instalar paquetes globales o locales en un entorno virtual.

Presentan algunas diferencias en cuanto a la forma de instalar paquetes y la forma de especificar los paquetes a instalar. Algunas de las diferencias más notables son:

```bash
# Instalar un paquete en Python 2
pip2 install nombre_paquete

# Instalar un paquete en Python 3
pip3 install nombre_paquete
```
