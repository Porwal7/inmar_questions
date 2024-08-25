//Question #6) The Scala code provided below is meant to calculate the sum of squares of all the
//elements in a list. There are errors though. Fix the code so it works as expected.
//def calcSumOfSquares(n: List[Int]): Int = {
//var sum = 0
//for (num <- n) {
//square = num * num
//sum += square
//}
//sum



def calcSumOfSquares(n: List[Int]): Int = {
  var sum = 0
  for (num <- n) {
    val square = num * num
    sum += square
  }
  sum
}

/* Two issue in code square variable not initialize and bracket not closed */