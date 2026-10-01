# Identificador de IPs
Script en Python que lee un archivo de direcciones IP y clasifica cada una como **pública** o **privada** según los rangos definidos en el RFC 1918.
## ¿Qué hace?
El script pide al usuario el nombre de un archivo de texto que contiene una IP por línea, luego:
- Clasifica como **privada** si la IP pertenece a uno de estos rangos:
  - `10.0.0.0/8` (empieza con `10.`)
  - `172.16.0.0/12` (segundo octeto entre 16 y 31)
  - `192.168.0.0/16` (empieza con `192.168.`)
- Clasifica como **pública** cualquier otra IP.
## ¿Cómo se usa?
1. Tener Python 3 instalado.
2. Colocar el archivo de IPs (por ejemplo, `ips.txt`) en la misma carpeta que el script.
3. Ejecutar desde la terminal:
```bash
python identificador_de_IPs.py
```
4. Cuando el script lo pida, escribir el nombre del archivo: `ips.txt`.
## Ejemplo de salida
```
10.0.0.1 es una IP privada.
192.168.1.5 es una IP privada.
172.20.5.10 es una IP privada.
172.15.5.10 es una IP publica.
172.32.5.10 es una IP publica.
8.8.8.8 es una IP publica.
```
## Conceptos aplicados
- Lectura de archivos línea por línea.
- Manipulación de strings (`startswith`, `split`, `rstrip`).
- Conversión de tipos (`int`).
- Condicionales encadenados (`if` / `elif` / `else`).
- Clasificación según rangos de red.
## Autor

Zelvaztian
