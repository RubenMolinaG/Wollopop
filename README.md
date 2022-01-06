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

El ejemplo anterior hará un <ins>scrap de la web durante 10 minutos.</ins> Mientras hace el scroll de la web, añade los productos a una lista, la cual luego <ins>se volcará dentro de un fichero JSON.</ins>

**Ejemplo de fichero JSON**
```json
[
    {
        "NOMBRE": "Tuerto, maldito y enamorado",
        "PRECIO": "8",
        "DESC": "Libro en perfecto estado Autora Rosa Huertas Editorial Edelvives",
        "ENLACE": "https://es.wallapop.com/item/tuerto-maldito-y-enamorado-726901782"
    },
    {
        "NOMBRE": "Likundú",
        "PRECIO": "8",
        "DESC": "Libro Likundú en perfecto estado Autor Heinz Delam Editorial Bruño",
        "ENLACE": "https://es.wallapop.com/item/likundu-726898111"
    },
    {
        "NOMBRE": "La dama del Alba",
        "PRECIO": "8",
        "DESC": "Libro La dama del Alba en perfecto estado Autor Alejandro Casona Editorial Vicens Vives",
        "ENLACE": "https://es.wallapop.com/item/la-dama-del-alba-726896115"
    },
    {
        "NOMBRE": "bolsa de viaje michael kors",
        "PRECIO": "160",
        "DESC": "original con etiqueta y certificado..muy chulo",
        "ENLACE": "https://es.wallapop.com/item/bolsa-de-viaje-michael-kors-725925734"
    },
]
```
