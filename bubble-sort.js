ex1 = [5, 8, 1, 10, 7];
ex2 = [2, 6, 8, 13, 18, 19];
ex3 = [0, -23, 10];
ex4 = [90, -22, -20, 1];
// console.log(ex3);

const bubbleSort = (arr) => {
  let len = arr.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (arr[j] > arr[j + 1]) {
        let result = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = result;
      }
    }
  }
  return arr;
};

console.log(bubbleSort(ex4));
