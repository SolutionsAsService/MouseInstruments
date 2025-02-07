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
    "string_hole": (0, 0, 0),      # Black for string instrument holes
    "accordion_keys": (255, 255, 255),  # White for accordion keys
    "accordion_bellows": (0, 0, 0)  # Black for accordion bellows
}

def draw_pixel(draw, x, y, color):
    draw.rectangle([x, y, x + 1, y + 1], fill=color)

def draw_accordion(draw):
    base_x, base_y = 12, 16
    # Draw the main body of the accordion
    for x in range(40):
        for y in range(20):
            draw_pixel(draw, base_x + x, base_y + y, instrument_colors["accordion"])
    # Draw the keys
    for x in range(10, 30, 2):
        for y in range(5):
            draw_pixel(draw, base_x + x, base_y + y, instrument_colors["accordion_keys"])
    # Draw the bellows
    for y in range(20):
        if y % 2 == 0:
            draw_pixel(draw, base_x + 5, base_y + y, instrument_colors["accordion_bellows"])
            draw_pixel(draw, base_x + 35, base_y + y, instrument_colors["accordion_bellows"])

def draw_guitar(draw):
    base_x, base_y = 18, 28
    # Draw the body of the guitar
    for x in range(28):
        for y in range(24):
            if 4 < x < 24 and 0 < y < 20:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["guitar"])
            elif 10 < x < 18 and 8 < y < 16:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])
    # Draw the neck of the guitar
    for x in range(8):
        for y in range(20):
            draw_pixel(draw, base_x + 10 + x, base_y - 20 + y, instrument_colors["guitar"])

def draw_violin(draw):
    base_x, base_y = 18, 30
    # Draw the body of the violin
    for x in range(28):
        for y in range(20):
            if 4 < x < 24 and 0 < y < 16:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["violin"])
            elif 10 < x < 18 and 6 < y < 10:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])
    # Draw the neck of the violin
    for x in range(8):
        for y in range(20):
            draw_pixel(draw, base_x + 10 + x, base_y - 20 + y, instrument_colors["violin"])

def draw_banjo(draw):
    base_x, base_y = 20, 20
    # Draw the body of the banjo
    for x in range(24):
        for y in range(24):
            if 4 < x < 20 and 4 < y < 20:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["banjo"])
            elif 10 < x < 14 and 10 < y < 14:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["string_hole"])
    # Draw the neck of the banjo
    for x in range(4):
        for y in range(20):
            draw_pixel(draw, base_x + 10 + x, base_y - 20 + y, instrument_colors["banjo"])

def draw_flute(draw):
    base_x, base_y = 12, 30
    # Draw the body of the flute
    for x in range(40):
        for y in range(5):
            draw_pixel(draw, base_x + x, base_y + y, instrument_colors["flute"])
            if x % 5 == 0:
                draw_pixel(draw, base_x + x, base_y + 2, instrument_colors["string_hole"])

def draw_drum(draw):
    base_x, base_y = 12, 20
    # Draw the body of the drum
    for x in range(40):
        for y in range(40):
            if (x - 20) ** 2 + (y - 20) ** 2 <= 400:
                draw_pixel(draw, base_x + x, base_y + y, instrument_colors["drum"])
            if 15 < (x - 20) ** 2 + (y - 20) ** 2 <= 400 and (x - 20) % 5 == 0:
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
