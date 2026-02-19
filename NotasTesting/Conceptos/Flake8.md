
Es el encargado de verificar el código escrito, para esto tiene varios parámetros que verifica, como puede ser la identacion, los espacios, el tamaño de una linea, nombres de variables correctas, etc.

#### ¿Que es lo que contiene?

Principalmente contiene 3 herramientas importantes:

- **PyFlakes:** Busca errores de programación (como variables que nunca usaste o funciones mal escritas).
    
- **pycodestyle:** Revisa que sigas la guía de estilo **PEP 8** (espacios, nombres de variables, longitud de líneas).
    
- **McCabe:** Revisa la "complejidad" de tu código (si tienes demasiados `if` anidados, te avisará que tu función es un laberinto).

#### ¿Como se usa?

Principalmente se utiliza el comando mas el nombre, con eso estará listo para indicar los errores un ejemplo que seria el resultado que nos da Flake8 en el codigo de fecha_texto.

``` bash
PS C:\workspace\Testing2026UAZ> python -m flake8 .\fechatexto\fechatexto.py
.\fechatexto\fechatexto.py:10:80: E501 line too long (84 > 79 characters)
.\fechatexto\fechatexto.py:14:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:16:33: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:17:27: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:18:27: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:19:31: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:22:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:34:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:35:80: E501 line too long (96 > 79 characters)
.\fechatexto\fechatexto.py:40:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:41:14: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:42:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:43:78: W291 trailing whitespace
.\fechatexto\fechatexto.py:44:24: E128 continuation line under-indented for visual indent
.\fechatexto\fechatexto.py:47:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:48:78: W291 trailing whitespace
.\fechatexto\fechatexto.py:49:21: E128 continuation line under-indented for visual indent
.\fechatexto\fechatexto.py:50:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:51:34: W291 trailing whitespace
.\fechatexto\fechatexto.py:55:80: E501 line too long (87 > 79 characters)
.\fechatexto\fechatexto.py:57:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:58:16: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:59:15: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:60:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:61:78: W291 trailing whitespace
.\fechatexto\fechatexto.py:62:22: E128 continuation line under-indented for visual indent
.\fechatexto\fechatexto.py:62:80: E501 line too long (94 > 79 characters)
.\fechatexto\fechatexto.py:63:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:66:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:72:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:73:16: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:74:17: E701 multiple statements on one line (colon)
.\fechatexto\fechatexto.py:75:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:78:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:84:1: W293 blank line contains whitespace
.\fechatexto\fechatexto.py:90:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:93:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:95:19: E128 continuation line under-indented for visual indent
.\fechatexto\fechatexto.py:95:80: E501 line too long (87 > 79 characters)
.\fechatexto\fechatexto.py:98:1: E302 expected 2 blank lines, found 1
.\fechatexto\fechatexto.py:103:9: F841 local variable 'dia' is assigned to but never used
.\fechatexto\fechatexto.py:104:9: F841 local variable 'mes' is assigned to but never used
.\fechatexto\fechatexto.py:105:9: F841 local variable 'anio' is assigned to but never used
.\fechatexto\fechatexto.py:110:16: W292 no newline at end of file
```

#### ¿Qué significan sus errores?

- **E501**: es un error que se ocasiona cuando las líneas de código son muy largas, estas no deben superar los 79 caracteres para comodidad si es que tienes mas de 1 archivo abiertos.
- **E302**: es un error basado en la distancia entre funciones, esto causa que si una función esta mas pegada a otra se puede malinterpretar a la hora de leer, lo recomendable es separar por dos líneas de código cuando finalice una función y cuando inicie una nueva.
- **E701**: es un error cuando tienes varias funciones, condiciones o bucles en una sola lineal, se soluciona simplemente separando por linea cada función, condición o bucle para que el código tenga claridad.
- **F841**: Este error es cuando tienes una variable inicializada pero nunca la usas, esto se puede arreglar usando esta misma variable o borrándola si es que en verdad no esta siendo usada.
