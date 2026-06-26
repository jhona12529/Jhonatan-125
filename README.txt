# Sistema de Registro de Notas de Estudiantes

## Descripción
Programa desarrollado en Python que permite registrar estudiantes con sus
notas, calcular el promedio automáticamente y determinar si aprobaron o
desaprobaron. Proyecto integrador del curso Fundamentos de Programación.

## Funcionalidades
- Registrar estudiantes con nombre y tres notas (rango 0–20)
- Calcular el promedio de cada estudiante
- Determinar el estado: Aprobado (promedio ≥ 11) o Desaprobado
- Mostrar la lista completa de estudiantes registrados
- Validación de entradas: rechaza valores fuera de rango y texto no numérico

## Requisitos
- Python 3.x

## Cómo ejecutar
- Git bash
- python registro_notas.py

## Estructura del código
- ingresar_nota() — valida y retorna una nota entre 0 y 20
- calcular_promedio() — calcula el promedio de tres notas
- determinar_estado() — retorna Aprobado o Desaprobado
- registrar_estudiante() — gestiona el registro completo de un estudiante
- mostrar_estudiantes() — muestra la lista de todos los registros
- mostrar_menu() — presenta el menú principal
- main() — controla el flujo general del programa

## Curso
Fundamentos de Programación — Universidad Privada del Norte
Tema N° 7: Proyecto Integrador
