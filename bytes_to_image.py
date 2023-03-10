from PIL import Image
import io

arr = []

with open("image_bytes.txt") as file:
    line = file.readline().strip()
    arr_str = line.split(",")
    for item in arr_str:
        arr.append(int(item))


image_bytes = bytes(arr)
img = Image.open(io.BytesIO(image_bytes))
img.show()
img.save("./python_image.png")