## Bienvenido a Netflix-pin-hack

Este es un cript creado para poder acceder a cuentas de netflix con bloqueo de PIN.

Este es un script de fuerza bruta que se aprovecha de la falla de Netflix, que al no tener un limite de intentos en los pines, se puede aplicar fuerza bruta. Este script se puede ejecutar tanto en Windows como en Linux. Claramente los usuarios Linux tienen una ventaja mayor, ya que al poder ejecutar el script en bash son capaces de poder obtener un margen de posibles pines correctos.

Además para los usuarios linux, cuando el pin correcto acirte, ingresaran a la cuenta de netflix y como en la mayorias de las veces, se reproduce un trailer. Al salir el sonido por los parlantes el script en bash lo detecta y cierra el programa arrojando los ultimos 5 pines antes de el sonido. Por lo que el PIN correcto se encuentra en alguno de ellos.

Inicie el programa y espere 5 segundos, durante esos 5 segundos debe colocar el cursor y hacer clik sobre la casilla del pin y los pines comenzaran a ingresarse. MUY IMPORTANTE no moverse ni hacer click en ninguna otra ventana que no sea la de Netflix

## Ejecución

<p align="center">
	<img src="https://i.imgur.com/XtUtLAK.gif" width="90%" height="90%" align="">
</p>


### Usuario Windows:

Ejecute el script en python index.py y este atento en que PIN la cuenta se desbloquea.

### Usuario Linux:

Ejecuten el script en bash netflix_pin.sh y vallan a tomar una taza de café :)

<p align="center">
	<img src="https://i.imgur.com/OvOlLKz.jpg" width="100%" height="100%" align="">
</p>

### Instalación:

Primero instalaremos la libreria pyautogui

```markdown
pip install pyautogui
```

## Manual de uso usuarios Linux

### Permisos:

Cambiamos los permisos de ejecución

```markdown
git clone https://github.com/Alcatraz2033/netflix-pin-hack.git

cd netflix-pin-hack

chmod +x *
```

### Ejecución:

Ejecutamos el scrpt en bash agregandole el rango de numero inicial y final a iterar.

```markdown
./netflix_pin.sh 0000 9999
```

## Manual de uso usuarios Windows

### Ejecución:

Ejecutamos el script en python agregandole el rango de numero inicial y final a iterar.

```markdown
python index.py -s 0000 -e 9999
```
