from PIL import Image

# Definimos una lista de caracteres ASCII que utilizaremos para el arte
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Cambia el tamaño de la imagen
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convierte la imagen a escala de grises
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convierte cada píxel a un carácter ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

# Función principal para convertir una imagen a arte ASCII
def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Dividir el string de caracteres ASCII en líneas para que se ajuste al ancho de la imagen
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

# Función para mostrar el arte ASCII en la consola
def main():
    image_path = input("Enter the path to the image file: ")
    ascii_art = image_to_ascii(image_path)
    if ascii_art:
        print(ascii_art)

if __name__ == "__main__":
    main()
