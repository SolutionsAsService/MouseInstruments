from PIL import Image, ImageDraw

# Define image size
width, height = 64, 64  # Size for the instrument sprite

# Define colors for different instruments
instrument_colors = {
    "accordion": (255, 0, 0),      # Red for accordion
    "guitar": (139, 69, 19),       # Brown for guitar
    "violin": (160, 82, 45),       # Darker brown for violin
    "banjo": (205, 133, 63),       # Light brown for banjo
    "flute": (192, 192, 192),      # Silver for flute
    "drum": (139, 69, 19),         # Brown for drum
    "string_hole": (0, 0, 0)       # Black for string instrument holes
}

def draw_pixel(draw, x, y, color):
    draw.rectangle([x, y, x + 1, y + 1], fill=color)

def draw_accordion(draw):
    base_x, base_y = 16, 12
    for x in range(32):
        for y in range(40):
            if x % 8 < 4 and y % 8 < 4:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["accordion"])
            elif x % 8 >= 4 and y % 8 >= 4:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["accordion"])
            else:
                draw_pixel(draw, base_x + x, base_y + y, (255, 255, 255))

def draw_guitar(draw):
    base_x, base_y = 18, 10
    for x in range(28):
        for y in range(44):
            if (x > 4 and x < 24 and y > 8 and y < 36):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["guitar"])
            elif (x > 10 and x < 18 and y > 20 and y < 28):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])

def draw_violin(draw):
    base_x, base_y = 18, 15
    for x in range(28):
        for y in range(34):
            if (x > 4 and x < 24 and y > 6 and y < 28):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["violin"])
            elif (x > 10 and x < 18 and y > 14 and y < 20):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])

def draw_banjo(draw):
    base_x, base_y = 18, 18
    for x in range(28):
        for y in range(28):
            if (x > 4 and x < 24 and y > 4 and y < 24):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["banjo"])
            elif (x > 10 and x < 18 and y > 10 and y < 18):
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])

def draw_flute(draw):
    base_x, base_y = 12, 30
    for x in range(40):
        for y in range(5):
            draw_pixel(draw, base_x + x, base_y + y, instrument_colors["flute"])
            if x % 5 == 0:
                draw_pixel(draw, base_x + x, base_y + 2, instrument_colors["string_hole"])

def draw_drum(draw):
    base_x, base_y = 12, 20
    for x in range(40):
        for y in range(30):
            draw_pixel(draw, base_x + x, base_y + y, instrument_colors["drum"])
            if y % 10 == 0:
                draw_pixel(draw, base_x + x, base_y + y, (0, 0, 0))

def generate_instrument_images():
    images = []
    draw_functions = [draw_accordion, draw_guitar, draw_violin, draw_banjo, draw_flute, draw_drum]

    for draw_function in draw_functions:
        image = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(image)
        draw_function(draw)
        images.append(image)

    return images

# Generate and save the images for testing
if __name__ == '__main__':
    images = generate_instrument_images()

    for idx, image in enumerate(images):
        image.show()  # Opens the generated image in the default image viewer
        image.save(f"instrument_{idx + 1}.png")  # Saves the generated image to a file
