# Laboratorio de Sistemas Distribuidos 3

Este repositorio contiene el código desarrollado como parte del laboratorio de Sistemas Distribuidos, específicamente en la implementación de Sockets tanto en Java como en Python. El propósito de este laboratorio fue explorar y entender el funcionamiento de la comunicación entre procesos a través de redes, utilizando los conceptos de sockets, el equipo de trabajo está compuesto por:

- Caceres Apaza Jherald Huren 
- Perez Torres Luis Rodrigo
- Huanaco Hallasi Diego Edgardo
- Vilca Suelo Giovanni Gabriel 

## Descripción del Laboratorio:

En este laboratorio, se abordaron los siguientes puntos sobre la implementación de sockets:

1. **Implementación en Java:**
   - Se desarrolló un servidor y un cliente en Java utilizando la clase `ServerSocket` para el servidor y la clase `Socket` para el cliente.
   - El servidor fue capaz de aceptar múltiples conexiones de clientes, gestionando la comunicación bidireccional entre ellos a través de la lectura y escritura de datos en los sockets.

2. **Implementación en Python:**
   - También se implementó un servidor y un cliente en Python utilizando el módulo `socket`.
   - Se exploraron diferentes enfoques para la comunicación cliente-servidor en Python, incluyendo la serialización de datos y la gestión de conexiones múltiples.

3. **Interacción y Pruebas:**
   - Se realizaron pruebas de interacción entre los clientes y el servidor tanto en Java como en Python, verificando la correcta transmisión y recepción de mensajes.
   - Se probó la capacidad del servidor para gestionar múltiples conexiones de clientes de manera eficiente, manteniendo un flujo de comunicación fluido y sin interrupciones.

4. **Documentación y Reporte:**
   - Se documentaron los pasos de implementación, configuración y ejecución de los programas en Java y Python.
   - Se elaboró un reporte que describe la estructura del código, las decisiones de diseño tomadas y los resultados obtenidos durante las pruebas de funcionamiento.