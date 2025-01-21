# Proyecto de Simulación de Puertas Lógicas

Este proyecto es una aplicación en Python que permite simular el comportamiento de puertas lógicas utilizando argumentos de línea de comandos.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tu_usuario/tu_proyecto.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd tu_proyecto
   ```
3. Asegúrate de tener Python instalado (versión 3.x recomendada).
4. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando en la terminal:

```bash
python app.py entrada1 entrada2
```

### Ejemplos de uso:

- Para simular una puerta lógica que requiere dos entradas (por ejemplo, AND, OR, XOR):
  ```bash
  python app.py 0 0
  python app.py 0 1
  python app.py 1 0
  python app.py 1 1
  ```

- Para simular una puerta lógica que requiere solo una entrada (por ejemplo, NOT):
  ```bash
  python app.py 0
  python app.py 1
  ```


## Contribuciones

Si deseas contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu mejora (`git checkout -b feature-nueva`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añade nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature-nueva`).
5. Abre un Pull Request.
