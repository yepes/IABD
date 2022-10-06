const start = Date.now();

/**
 * Permuta todos los números de un array
 * 
 * @param {int[]} nums 
 * @returns {[int[]]}
 */
function permute(nums) {
  let result = [];
  if (nums.length === 0) return [];
  if (nums.length === 1) return [nums];
  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    const remainingNums = nums.slice(0, i).concat(nums.slice(i + 1));
    const remainingNumsPermuted = permute(remainingNums);
    for (let j = 0; j < remainingNumsPermuted.length; j++) {
      const permutedArray = [currentNum].concat(remainingNumsPermuted[j]);

      result.push(permutedArray);
    }
  }
  return result;
}

/**
 * Imprime el array en formato tabla
 * 
 * @param {int[][]} state 
 */
function printTable(state) {
  const copy = [...Array.from(state)].map(d => d);
  for (let i = 0; i < copy.length; i++) {
    for (let j = 0; j < i; j++) {
      const tmp = copy[i][j];
      copy[i][j] = copy[j][i];
      copy[j][i] = tmp;
    }
  }
  console.table(copy)
}

/**
 * Parte el array de entrada en columnas
 * 
 * @param {[int[]]} data 
 * @returns 
 */
function createTable(data) {
  return [
    data.slice(0, 3),
    data.slice(3, 6),
    data.slice(6)
  ]
}

/**
 * Comprueba si una columa es válida
 * 
 * @param {int[]} col 
 * @returns 
 */
function checkColumnImpossibleState(col) {

  const sum = col.reduce((prev, cur) => {
    return prev + cur
  }, 0)

  if (sum === 0)
    return true;

  return col.every((x, i) => i === 0 || x >= col[i - 1]);

}

/**
 * Comprueba si el estado es válido.
 * Un estado es válido cuando todas las columnas son válidas
 * 
 * @param {int[][]} state 
 * @returns {boolean}
 */
function isStateValid(state) {
  return checkColumnImpossibleState(state[0]) &&
    checkColumnImpossibleState(state[1]) &&
    checkColumnImpossibleState(state[2])
}

const initialState = [1, 2, 3, 0, 0, 0, 0, 0, 0];
const permutedState = permute(initialState);
/**
 * La idea es tener todas las posiciones del tablero (3 filas y 3 columnas, 9)
 * en un array unidimensional, siendo cada 3 posiciones una columna, es decir,
 * las tres primeras posiciones serán la primera columna. Los 0s representan espacios en blanco
 * Con todo esto:
 * 1 - Permutamos el array para obtener todas las posibles variaciones del mismo (posiciones)
 * 2 - Creamos un set para eliminar los repetidos (ya que muchas veces se permutan los 0). La forma 
 * más rápida de comparar dos arrays que he encontrado es pasarlos a cadena y compararlos.
 * 3 - Pasamos la cadena a array de nuevo
 * 4 - Creamos la tabla (array de dos dimensiones)
 * 5 - Comprobamos que cada tabla generada es válida
 * 6 - Imprimimos los resultados válidos
 */
const result = [...new Set(permutedState.map(d => JSON.stringify(d)))]
  .map(d => JSON.parse(d))
  .map(d => createTable(d))
  .filter(d => isStateValid(d))


const end = Date.now();
result.forEach(d => printTable(d));

console.log(`Total resultados válidos: ${result.length}`);
console.log(`Tiempo transcurrido: ${end - start} ms`);
