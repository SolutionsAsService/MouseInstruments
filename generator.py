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

def draw_accordion(draw):
    base_x, base_y = 16, 12
    # Draw the main body of the accordion
    for x in range(32):
        for y in range(40):
            if x % 8 < 4 and y % 8 < 4:
                draw.point((base_x + x, base_y + y), fill=instrument_colors["accordion"])
            elif x % 8 >= 4 and y % 8 >= 4:
                draw.point((base_x + x, base_y + y), fill=instrument_colors["accordion"])
            else:
                draw.point((base_x + x, base_y + y), fill=(255, 255, 255))

def draw_guitar(draw):
    base_x, base_y = 18, 10
    # Draw the body of the guitar
    for x in range(28):
        for y in range(44):
            if (x > 4 and x < 24 and y > 8 and y < 36):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["guitar"])
            elif (x > 10 and x < 18 and y > 20 and y < 28):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["string_hole"])
    # Draw the neck of the guitar
    for x in range(5):
        for y in range(10):
            draw.point((base_x + 12 + x, base_y - 10 + y), fill=instrument_colors["guitar"])

def draw_violin(draw):
    base_x, base_y = 18, 15
    # Draw the body of the violin
    for x in range(28):
        for y in range(34):
            if (x > 4 and x < 24 and y > 6 and y < 28):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["violin"])
            elif (x > 10 and x < 18 and y > 14 and y < 20):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["string_hole"])
    # Draw the neck of the violin
    for x in range(5):
        for y in range(10):
            draw.point((base_x + 12 + x, base_y - 10 + y), fill=instrument_colors["violin"])

def draw_banjo(draw):
    base_x, base_y = 20, 18
    # Draw the body of the banjo
    for x in range(24):
        for y in range(24):
            if (x > 4 and x < 20 and y > 4 and y < 20):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["banjo"])
            elif (x > 10 and x < 14 and y > 10 and y < 14):
                draw.point((base_x + x, base_y + y), fill=instrument_colors["string_hole"])
    # Draw the neck of the banjo
    for x in range(5):
        for y in range(20):
            draw.point((base_x + 10 + x, base_y - 20 + y), fill=instrument_colors["banjo"])

def draw_flute(draw):
    base_x, base_y = 12, 30
    # Draw the body of the flute
    for x in range(40):
        for y in range(5):
            draw.point((base_x + x, base_y + y), fill=instrument_colors["flute"])
            if x % 5 == 0:
                draw.point((base_x + x, base_y + 2), fill=instrument_colors["string_hole"])

def draw_drum(draw):
    base_x, base_y = 12, 20
    # Draw the body of the drum
    for x in range(40):
        for y in range(30):
            draw.point((base_x + x, base_y + y), fill=instrument_colors["drum"])
            if y % 10 == 0:
                draw.point((base_x + x, base_y + y), fill=(0, 0, 0))

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
