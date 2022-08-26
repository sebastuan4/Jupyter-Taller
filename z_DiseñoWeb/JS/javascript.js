//Crear variables con javascript
var x=5;//Puede ser declarado muchas veces y se puede modificiar
let y=5;//Se puede modificar pero no declarar multiples veces
const z=5;//No se puede modificar y se deben inizializar
var x//Las variables no inicializadas tendran el valor de "undefined"
//Operadores
let numUno = 1
let numDos = 2
let suma = 1+2
let resta = 1-2
let multiplicacion = 1*2
let division = 1/2
let exponente = 1**2
let modulo = 1%2
document.getElementById("suma").innerHTML = "El resultado de la suma fue: "+suma
document.getElementById("resta").innerHTML = "El resultado de la resta fue : "+resta
document.getElementById("multiplicacion").innerHTML = "El resultado de la multiplicacion fue : "+multiplicacion
document.getElementById("division").innerHTML = "El resultado de la division fue : "+division
document.getElementById("exponente").innerHTML = "El resultado de la exponente fue : "+exponente
document.getElementById("modulo").innerHTML = "El resultado de la modulo fue : "+modulo
//Funciones
function funcionSuma(numUno,numDos){
    return numUno+numDos
}
document.getElementById("Funcion").innerHTML="El resultado de la funcion suma fue: "+funcionSuma(1,2)
//Objetos
var car = {tipo:"Fiat", modelo:"500", color:"blanco"};
document.getElementById("forma1").innerHTML=car.tipo
document.getElementById("forma2").innerHTML=car["tipo"]
//Eventos
/*
onchange Una parte html fue cambiada
onclick	Se le da click al elemento
onmouseover	El raton esta sobre el elemento
onmouseout	El raton sale del elemento
onkeydown	Se preciona una tecla del teclado
onload	Cuando el navegador finaliza de cargar la bagina
*/ 

//Loops
/*
Tipos de for
for loop sobre un bloque x cantidad de veces
for/in loop que se ejecuta x cantidad de veces sobre las propiedades de un objeto
for/of loop sobre los valores de un objeto iterable
*/
var car_list = ["Carro1","Carro2","Carro3"]
function For (){
    for (let i = 0; i<10; i++){
        document.getElementById("FOR").innerHTML=i
    }
}
function Forin(){
    for (let autos in car_list){
        document.getElementById("FOR").innerHTML=autos
    }
}
function Forof(){
    for (let autos of car_list){
        document.getElementById("FOR").innerHTML=autos
    }
}
/* 
Tipos de bucle While
While repite las acciones hasta que la condicion sea falsa
Do while
*/
function While(){
    let i=0
    while (i<10){
        i++
        document.getElementById("While").innerHTML=i
    }
}
function Dowhile(){
    let i=0
    do{
        i++
        document.getElementById("While").innerHTML=i
    }
    while (i==10);
}
function Break(){
    let i=0
    while (true){
        document.getElementById("While").innerHTML="El codigo llega aqui"
        break
        document.getElementById("While").innerHTML="Pero no aqui"
    }
}








