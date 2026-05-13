# que es Node? 
* es un entorno de ejecucion para javascrip fuera del navegador , construido sobre V8

    Ryan Dhal crea node js 
    V8 motor de javascrip desarrolado por google 
    sincrono - ejecuta conforme fueron hechos los documentos- documento 1 - documento 2 
    node pakadege, es multiplataforma, que se puede utilizar en cualquier dispostivo 

- Node.js no es un lenguaje y un servidor web por si mismo 

* Limitacion: No es ideal para tareas muy *CPU intensivas

 ## que es un runtime environment? 
un runtime es el entorno que provee todas las herramientas para ejecutar un lenguaje. En los navegadores, el entorno incluye objetos como window o dcument. Node.js, el entorno incluye objetos como globla, process, fs (file system), http, etc

## Event lopp y asincronia 
node.js funciona con un unico hilo de ejecucion (single-thread) pero gracias a event Lopp puede manejar multiples tareas concurrentes

asincronico 
va en order logico, 

sincronico 
va de que otma la orden y espera a que este el pedido para llevarlo 

## Argumentos en la linea de comandos 
## Que es process.argv ? 
es un arreglo de strings que Node.js llenna automaticamente cuando ejecutas un script desde la terminal 



```js

```
NOTA  **todos** los elementos de process.argv 




## el obejto global en Node.js y navegfadores - windows, 


en navegadores: `gobalThis === window` 
en node.js: `goblarThis === glabol`

## ESTENSIONES `.cjs`, `.mjs` y `.js` en Node.js - que son, diferencias 


- .cjs siempre se interpreta como CommonJS (CJS)
- .mjs siempre se interpreta como  ES Modules (ESM)
- .js depende de la configuracion del proyecto 

## dos sistemas de modulos en Node.js 
(CJS (historico))















