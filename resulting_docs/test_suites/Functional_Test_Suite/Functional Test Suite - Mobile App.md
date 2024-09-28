#### **Nombre del Test Suite:**

Functional Test Suite - Registro y Login App Móvil

#### **Descripción del Test Suite:**

Este test suite cubre las pruebas funcionales del registro y login en la versión móvil de la Fan App. Incluye casos de prueba para verificar el registro exitoso, manejo de errores, validación de identidad, y sincronización de datos entre la aplicación móvil y la web.

#### **Objetivo del Test Suite:**

El objetivo de este test suite es asegurar que el proceso de registro y login en la versión móvil funcione correctamente bajo diversas condiciones.

#### **Alcance:**

- Registro de usuarios en la App Móvil
- Login de usuarios
- Validación de identidad (documento, rostro)
- Manejo de errores para intentos fallidos de registro y login
- Sincronización de datos entre la aplicación móvil y web
- Recuperación de contraseña

#### **Casos de prueba incluidos:**

| **ID del Caso de Prueba** | **Descripción**                                                                                           | **Prioridad** | **Estado**   |
| ------------------------- | --------------------------------------------------------------------------------------------------------- | ------------- | ------------ |
| TC_MOB_FUNC_001           | Verificar que el registro con datos válidos es exitoso en la app móvil                                    | Alta          | No ejecutado |
| TC_MOB_FUNC_002           | Verificar que el registro falla si el usuario ya existe con el mismo correo                               | Alta          | No ejecutado |
| TC_MOB_FUNC_003           | Verificar que el login es exitoso con credenciales válidas en la app móvil                                | Alta          | No ejecutado |
| TC_MOB_FUNC_004           | Verificar que el login falla con una contraseña incorrecta                                                | Alta          | No ejecutado |
| TC_MOB_FUNC_005           | Verificar que el login falla si el usuario no ha completado el registro                                   | Alta          | No ejecutado |
| TC_MOB_FUNC_006           | Verificar que se muestra un mensaje de error si los campos de email y contraseña están vacíos             | Media         | No ejecutado |
| TC_MOB_FUNC_007           | Verificar que el mensaje de bienvenida aparece correctamente para usuarios nuevos                         | Alta          | No ejecutado |
| TC_MOB_FUNC_008           | Verificar que el usuario puede seleccionar sus equipos favoritos durante el registro                      | Media         | No ejecutado |
| TC_MOB_FUNC_009           | Verificar que los equipos favoritos seleccionados se sincronizan correctamente con la versión web         | Alta          | No ejecutado |
| TC_MOB_FUNC_010           | Verificar que el login falla si la validación de identidad (documento/rostro) no se completa              | Alta          | No ejecutado |
| TC_MOB_FUNC_011           | Verificar que un usuario no puede registrarse con el mismo correo en dos cuentas                          | Alta          | No ejecutado |
| TC_MOB_FUNC_012           | Verificar que la app móvil maneja correctamente el envío de SMS para la validación del número de teléfono | Alta          | No ejecutado |

#### **Requisitos previos:**

- Cuentas de prueba (usuarios nuevos, usuarios registrados, usuarios con registro incompleto).
- Acceso al entorno de staging de la App Móvil.
- Configuración de dispositivos móviles (Android e iOS).

#### **Entorno de pruebas:**

- **Entorno**: Staging
- **Dispositivos móviles**: Android (última versión), iOS (última versión)
- **Navegadores móviles**: N/A (aplicación nativa)

#### **Pasos de ejecución:**

1. Configurar el entorno de pruebas y verificar que la App Móvil sea accesible en los dispositivos.
2. Ejecutar los casos de prueba en el orden especificado.
3. Registrar los resultados y documentar cualquier defecto encontrado.

#### **Criterios de aprobación/fallo:**

- **Aprobación**: Todos los casos de prueba de alta prioridad deben pasar exitosamente.
- **Fallo**: Si alguna funcionalidad crítica relacionada con el registro o login falla.