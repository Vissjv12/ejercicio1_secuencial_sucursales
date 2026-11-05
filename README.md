## consulta secuencial de sucursales

Se simula una consulta cinco sucursales una por una. La idea es que cada consulta empeiza despues de la anterior y al final se suman los tiempos

Ejecutar con Docker Compose:

```bash
docker compose -f docker-compose.extras.yml run --rm consulta-sucursales
```

Ejecutar sin Docker despues de ejecucion manual:

```bash
python 06_consulta_secuencial_sucursales.py
```
