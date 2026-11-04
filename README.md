# web-seguridad

Catálogo NEXO Seguridad — ejemplo para clase de IA.

Abre `dist/index.html` en un navegador. El archivo contiene HTML, CSS, JavaScript y todas las ilustraciones SVG. Funciona sin instalar dependencias y sin conexiones externas.

## Estructura

Inicio → catálogo con búsqueda y filtros → sobre nosotros y servicios → formulario de solicitud → pie de página.

## Personalización

La marca NEXO es ficticia. Las especificaciones son ejemplos de productos genéricos, no fichas de fabricantes. Reemplaza el nombre, identidad visual, productos y textos con los datos de la empresa antes de su uso comercial.

El formulario permite preparar y copiar una solicitud. No transmite ni almacena datos. No tiene WhatsApp conectado porque falta el número real de la empresa.

Para editar el archivo terminado, modifica `dist/index.html`. Para regenerarlo, edita `plantilla.html`, el tema en `tema.css` y los productos en `generar.py`, y ejecuta `python generar.py`. Regenerar sobrescribe el HTML terminado.

El estilo de esta práctica usa azul #004ba5, celeste #47bfe9 y blanco, inspirado en la paleta pública de competencia.com.ec. Conserva la marca ficticia NEXO y las ilustraciones originales del ejercicio.

El resumen de los diez productos está en `PRODUCTOS.md`.

## Publicación en Vercel

El archivo `vercel.json` indica que la carpeta pública es `dist`. No se necesita instalar dependencias ni ejecutar un build. En Vercel, la raíz del proyecto debe ser la raíz del repositorio. Cada push a `main` inicia una publicación si la integración de GitHub está activa.

## Comprobación local

Ejecuta `node verificar.cjs`. Comprueba la estructura, el JavaScript, filtros, búsqueda y preparación de la solicitud. Estas comprobaciones no sustituyen una revisión visual en navegador.
