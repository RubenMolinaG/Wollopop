# Wollopop

## Descripción
Wollopop es una API que te permite obtener los productos de su web y almacenarlos dentro de un fichero JSON.
La aplicación necesitará que se le pase la URL y el tiempo en minutos como argumentos.

## Ejecución de la aplicación
```console
python lanzador.py URL TIME
```
**Ejemplo**
```console
python lanzador.py "https://es.wallapop.com/app/search?longitude=-3.6827461&latitude=40.4893538" 10
```

El ejemplo anterior hará un scrap de la web durante 10 minutos. Mientras hace el scroll de la web, añade los productos a una lista, la cual luego se volcará dentro de un fichero JSON.

