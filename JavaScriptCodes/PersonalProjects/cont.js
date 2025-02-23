var x = 5
var y = Math.floor(Math.random() * 11)
var z = y + x
if (z == 10) {
    console.log("perfeito")
    console.log(z)
} else if (z < 10) {
    console.log("menor")
    console.log(z)
} else if (z > 10) {
    console.log("maior")
    console.log(z)
}