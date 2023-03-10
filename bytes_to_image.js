const fs = require("fs")


const arr = fs.readFileSync("image_bytes.txt", "utf-8").split(",").map(str_num => Number(str_num))

const image_bytes = new Uint8Array(arr);
console.log(image_bytes)

fs.writeFileSync("node_image.png", Buffer.from(image_bytes))
