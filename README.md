# Flappy Bird
![Imagen insertada](https://user-images.githubusercontent.com/73842931/203234278-72dc4c28-0542-475e-8b0a-a64993b7f79b.png)

![Estado](https://img.shields.io/badge/estado-finalizado-red)

## Indice

1. [Desripcion](#Descripcion)
2. [Indice](#Indice)
3. [Pre-requisitos](#Pre-requisitos)
4. [Instalacion](#Instalacion)
5. [Pruebas](#Ejecutando-las-pruebas)
6. [Tecnologias utilizadas](#Tecnologias)
7. [Contribuidores](#Contribuidores)
8. [Desarrollador Principal](#Desarrollador-Principal)
9. [Wiki](#Wiki)
10. [Licencia](#licencia)


## Descripcion
El objetivo del juego es guiar a un pájaro a través de tuberías sin chocar contra ellas.
El jugador controla el pájaro tocando la pantalla para hacerlo volar más alto y debe evitar que caiga al suelo o toque las tuberías.

✅ Jugabilidad sencilla: toca para saltar.

✅ Dificultad progresiva: las tuberías se mueven más rápido a medida que avanza el juego.

✅ Detección de colisiones: si el pájaro toca una tubería o el suelo → Game Over.

✅ Sistema de puntuación: suma un punto por cada tubería superada.

✅ Pantalla de reinicio para volver a jugar.

## Pre-requisitos

Para instalar esta aplicacion, hace falta tener instalado el sistema operativo al que va orientado, se recomienda el uso de android, aunque existen diferentes opciones.

## Instalación
Su instalacion es realmente sencilla, ya que no hace falta configurar nada, para hacerlo nos basta con ir a la tienda de aplicaciones de nuestro dispositivo, buscarla y descargarla desde ahi.

Tambien existe la posibilidad de que tengamos el archivo de otra manera, en ese caso simplemente ejecutamos el codigo y ya lo tendriamos.


## Ejecutando las pruebas

Dentro de los archivos subidos a GitHub existe una carpeta llamada Tests que dentro contienen diferentes Tests relacionados con diferentes temas, en caso de fallo y de no ser capaces de solucionar el/los errores se recomienda reinstalar el programa.

## Y las pruebas de estilo de codificación ⌨️

Algunas de las pruebas que nos podemos encontrar dentro de esos archivos son del estilo:

```java
import static org.junit.Assert.*;
import org.junit.Test;

public class GameEngineTest {

    @Test
    public void birdCollisionWithPipe_triggersGameOver() {
        // Crear pájaro y tubería que se superponen
        Bird bird = new Bird(50, 100, 30, 30);
        Pipe pipe = new Pipe(60, 110, 50, 200);

        GameEngine engine = new GameEngine();
        engine.checkCollision(bird, pipe);

        // Verificar que el juego terminó
        assertTrue(engine.isGameOver());
    }

    @Test
    public void birdWithoutCollision_noGameOver() {
        // Crear pájaro y tubería que NO se tocan
        Bird bird = new Bird(0, 0, 30, 30);
        Pipe pipe = new Pipe(200, 200, 50, 200);

        GameEngine engine = new GameEngine();
        engine.checkCollision(bird, pipe);

        // Verificar que el juego sigue
        assertFalse(engine.isGameOver());
    }
}
```

Estos test de ejemplo prueban si el juego se termina correctamente y unicamente en el momento que un jugador falle.

Y que no tenga bugs para terminar en cualquier otro momento del mismo.


## Tecnologias

[Android Studio](https://developer.android.com/studio?hl=es-419)

[Java](https://www.java.com/es/)

[SurfaceView](https://www.surfaceview.co.uk/#:~:text=Effective%2030/04/2024%20Surface,commitment%20to%20quality%20and%20creativity.) para la animación

## Contribuidores

Este programa esta hecho por la empresa .Gears.

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.


## Desarrollador Principal

Este proyecto fue iniciado por Nguyen Hà Đông, encargado de la direccion del mismo durante todo su desarrollo.

## Wiki 

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://wikiindie.fandom.com/es/wiki/Flappy_Bird)

## Licencia 

Este proyecto está bajo la Licencia (Licencia Privada Flappy Bird) - mira el archivo [LICENSE.md](LICENSE.md) para detalles


