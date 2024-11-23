# Urban Grocers - QA Project

## Descripción
Este proyecto automatiza las pruebas de la API de creación de kits en la aplicación Urban Grocers. Las pruebas están diseñadas para validar las restricciones del campo `name`en la solicitud de creación de kits.

## Autor
- Nombre: [Ignacia_Alarcon]
- Sprint: Séptimo

## Requisitos
- **Python 3.9+**
- **Dependencias**: Instálalas con:
  pip install -r requirements.txt

## Instalación
Clona el repositorio:
git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git

Ve al directorio del proyecto:
cd qa-project-Urban-Grocers-app-es

Ejecuta las pruebas con Pytest:
pytest create_kit_name_kit_test.py

Pruebas Implementadas
El proyecto incluye 9 pruebas según la lista de comprobación proporcionada:

#	Descripción	Resultado Esperado

1	Nombre con 1 carácter: {"name": "a"}	Código: 201, el nombre coincide

2	Nombre con 511 caracteres: {"name": "a"*511}	Código: 201, el nombre coincide

3	Nombre vacío: {"name": ""}	Código: 400

4	Nombre con más de 512 caracteres: {"name": "a"*512}	Código: 400

5	Nombre con caracteres especiales: {"name": "№%@,"}	Código: 201, el nombre coincide

6	Nombre con espacios: {"name": " A Aaa "}	Código: 201, el nombre coincide

7	Nombre con números: {"name": "123"}	Código: 201, el nombre coincide

8	Nombre no incluido en la solicitud: {}	Código: 400

9	Nombre con tipo incorrecto (número): {"name": 123}	Código: 400
