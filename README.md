# web-seguridad

Catálogo NEXO Seguridad — ejemplo para clase de IA.

Abre `dist/index.html` en un navegador. El archivo contiene HTML, CSS, JavaScript y todas las ilustraciones SVG. Funciona sin instalar dependencias y sin conexiones externas.

## Estructura

Inicio → catálogo con búsqueda y filtros → sobre nosotros y servicios → formulario de solicitud → pie de página.

## Personalización

La marca NEXO es ficticia. Las especificaciones son ejemplos de productos genéricos, no fichas de fabricantes. Reemplaza el nombre, identidad visual, productos y textos con los datos de la empresa antes de su uso comercial.

El formulario permite preparar y copiar una solicitud. No transmite ni almacena datos. No tiene WhatsApp conectado porque falta el número real de la empresa.

Para editar el archivo terminado, modifica `dist/index.html`. Para regenerarlo, edita `plantilla.html` y los productos en `generar.py`, y ejecuta `python generar.py`. Regenerar sobrescribe el HTML terminado.

El resumen de los diez productos está en `PRODUCTOS.md`.

## Verificación

Ejecuta `node verificar.cjs`. Comprueba la estructura, el JavaScript, filtros, búsqueda y preparación de la solicitud. Estas comprobaciones no sustituyen una revisión visual en navegador.
