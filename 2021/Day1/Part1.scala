import scala.io.Source



object test {
  def main(args: Array[String]): Unit = {
    val filename = "input.txt"
    for (line <- Source.fromFile(filename).getLines) {
        println(line)
    }
  }
}