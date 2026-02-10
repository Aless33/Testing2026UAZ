``` python
python3 -m doctest "NombreTest.txt" -v
```

`-m`: Es la abreviatura de **"module-name"**. Le dice a Python que busque un módulo en su librería y lo ejecute como un script principal.
`doctest`: Es el nombre del **módulo** que estás llamando. Su función es buscar pedazos de código dentro de texto, ejecutarlos y verificar que el resultado coincida.
`-v`: Significa **"verbose" (verboso)**. Obliga al comando a mostrarte todo lo que sucede, incluso si las pruebas salen bien.

Doctest sirve principalmente para probar los códigos mediante un conjunto de instrucciones o scripts puede ser el caso de que queramos probar una funcionalidad, método o parte del código con distintos escenarios.  El comando DOCTEST nos servirá muchísimo.
