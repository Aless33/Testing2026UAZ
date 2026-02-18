Es un [comando](Comandos/DOCTEST) para ejecutar un conjunto de pruebas escritas en otro documento, principalmente en un documento de texto, el cual seguirá las instrucciones que tendrá el documento en su interior.

#### Ejemplo

Un ejemplo de un Doctest seria a continuación lo siguiente

``` python
Estas son pruebas para verificar si es o no polindromo.
Se realiza primero una verificacion en el que la palabra tiene
que ser paralela a la mitad de la otra.
Esto se realiza con un for en donde el inicio y el final de la palabra
se van comparando hasta llegar a la mitad, en donde si fueron igual soltara un true,
si no sera un false. Se ignoran mayúsculas, espacios y acentos.

>>> from es_polindromo import es_palindromo

>>> es_palindromo('oso')
True

>>> es_palindromo('Oso')
True

>>> es_palindromo('Oso ')
True

>>> es_palindromo('Oso a')
False

>>> es_palindromo('Oso a osO')
True

>>> es_palindromo('Oso a osO')
True

>>> es_palindromo("Anita lava la tina")
True

>>> es_palindromo("A mamá Roma le aviva el amor a mamá")
True

>>> es_palindromo("Hola mundo")
False

>>> es_palindromo("No 'X' in Nixon")
True

>>> es_palindromo("Ánita lava la tiña")
False

>>> es_palindromo("")
True

>>> es_palindromo("A")
True

>>> es_palindromo("Dábale arroz a la zorra el abad")
True

```

Se caracteriza principalmente por tener un subconjunto de comandos los cuales pueden realizar pruebas que se ejecutan mediante `>>>` con el objetivo de ejecutar ese comando en lenguaje python.