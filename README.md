# Challenge-Python-L1
Prueba Técnica Zinobe

## Dependencias

* [Flask](https://palletsprojects.com/p/flask/)
* [requests](https://requests.readthedocs.io/en/master/)
* [pandas](https://pandas.pydata.org/)

## Instalación [Linux]

Luego de clonar el repositorio, ubiquese en la carpeta del proyecto y cree un entorno virtual:

```
python3 -m venv venv
```

Una vez creado, active el entorno virtual:

```
. venv/bin/activate
```

Posteriormente, instale las dependencias:

```
pip install -e .
```

## Ejecución [Linux]

Cuando haya concluido el proceso de instalación, configure las variables de entorno de Flask:

```
export FLASK_APP=zinobechallenge
export FLASK_ENV=development
```

Inicialice la Base de datos con el comando:

```
flask init-db
```

Y finalmente corra la aplicación:

```
flask run
```

La aplicación corre en el puerto 5000

# Acceso

Para comprobar la funcionalidad, ingrese en su navegador a la [url](http://localhost:5000/) de la aplicación.

# Descripción

La aplicación implementa un sencillo modelo de Flask, utilizando un endpoint para presentar la información solicitada.

![Zinobe_convocatoria](https://user-images.githubusercontent.com/39559138/109478708-95d59000-7a47-11eb-80ff-86cfdf88c902.png)

Se requirio procesar la información propuesta en el [primer enlace](https://rapidapi.com/apilayernet/api/rest-countries-v1), dado que el único endpoint que nos proporcionaba las regiones, nos traita la información en una lista de paises bastante extensa. Se proceso la información compilando todas las diferentes Regiones en la respuesta, y se descartaron campos con cadenas vacías.

El tiempo transcurrido para la obtención de cada set de datos se empieza a calcular. Posteriormente, con dichas regiones como entrada, se llama la lista de paises de cada región del [segundo endpoint](https://restcountries.eu/). Se selecciona un país al azar, y se procesan los datos de interes del objeto de respuesta, encriptando el lenguaje en SHA1 como es solicitado. Una vez se termina de realizar cada iteración por cada región, se concluye el conteo de tiempo para cada una.

Se crea el dataframe, se computan las estadísticas solicitadas y se insertan los resultados en la base de datos. Finalmente, se genera el archivo data.json.

![zinobe_diagrama_flujo](https://user-images.githubusercontent.com/39559138/109479046-fcf34480-7a47-11eb-9d0b-5c531b734c3d.png)

Por cuestiones de tiempo, no se alcanzó a realizar las pruebas unitarias.
