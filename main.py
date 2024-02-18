from PIL import Image

# ASCII char used to build the ASCII art 
ASCII_CHAR  = ["@" , "#" , "S", "%", "?", "*", "+", ";", ":", ",", "."]


# resize the img :
def resize_img(image , new_width = 100) :
    width , height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width , new_height))
    return resized_img

# pixel to grayscale ( grayscale => https://fr.wikipedia.org/wiki/Niveau_de_gris )
def pixel_to_grayscale(image):
    grayscale_img = image.convert("L") #https://pillow.readthedocs.io/en/stable/reference/Image.html
    return grayscale_img

# pixel to ascii
def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHAR[pixel//25] for pixel in pixels)
    return characters

# function to open the image 
def main(new_width = 100):
    path = input("Enter the path of the image : \n")
    try : 
        image = Image.open(path)
    except Exception as e:
        print(f'{path} is not a valid path !')
        print(e)
        return
    
    # image to ascii
    grayscale_image = pixel_to_grayscale(resize_img(image))
    new_image_data = pixel_to_ascii(grayscale_image)

    pixel_nb = len(new_image_data)
    ascii_img = "\n".join(new_image_data[i:i+new_width] for i in range(0 , pixel_nb , new_width))

    print(ascii_img)
    try : 
        with open("asciiArt.txt" , "w") as c : 
            try: 
                c.write(ascii_img)
            except Exception as e:
                print(f"Error while writing on the file: {e}")
    except Exception as e: 
        print(f"Error while opening the file: {e}")

main()
