from PIL import Image, ImageDraw

# Define image size
width, height = 64, 64  # Size for the instrument sprite

# Define colors for different instruments
instrument_colors = {
    "accordion": (255, 0, 0),  # Red for accordion
    "guitar": (139, 69, 19),   # Brown for guitar
    "violin": (160, 82, 45),   # Darker brown for violin
    "banjo": (205, 133, 63),   # Light brown for banjo
    "flute": (192, 192, 192),  # Silver for flute
    "drum": (255, 255, 0)      # Yellow for drum
}

def draw_accordion(draw):
    x, y = 10, 10
    draw.rectangle([x, y, x + 30, y + 40], fill=instrument_colors["accordion"], outline="black")
    draw.line([x + 5, y, x + 5, y + 40], fill="black", width=2)
    draw.line([x + 25, y, x + 25, y + 40], fill="black", width=2)
    draw.line([x, y + 10, x + 30, y + 10], fill="black", width=2)
    draw.line([x, y + 30, x + 30, y + 30], fill="black", width=2)

def draw_guitar(draw):
    x, y = 15, 10
    draw.rectangle([x, y, x + 10, y + 35], fill=instrument_colors["guitar"], outline="black")
    draw.ellipse([x - 5, y + 20, x + 15, y + 40], fill=instrument_colors["guitar"], outline="black")
    draw.line([x + 5, y, x + 5, y - 10], fill="black", width=2)

def draw_violin(draw):
    x, y = 15, 15
    draw.ellipse([x, y, x + 20, y + 30], fill=instrument_colors["violin"], outline="black")
    draw.line([x + 10, y, x + 10, y - 10], fill="black", width=2)

def draw_banjo(draw):
    x, y = 15, 15
    draw.ellipse([x, y, x + 20, y + 20], fill=instrument_colors["banjo"], outline="black")
    draw.rectangle([x + 8, y - 20, x + 12, y], fill=instrument_colors["banjo"], outline="black")
    draw.line([x + 10, y - 20, x + 10, y], fill="black", width=2)

def draw_flute(draw):
    x, y = 10, 30
    draw.rectangle([x, y, x + 40, y + 5], fill=instrument_colors["flute"], outline="black")
    for i in range(1, 8):
        draw.ellipse([x + i * 5, y + 1, x + i * 5 + 3, y + 4], fill="black", outline="black")

def draw_drum(draw):
    x, y = 10, 20
    draw.ellipse([x, y, x + 40, y + 30], fill=instrument_colors["drum"], outline="black")
    draw.line([x, y + 15, x + 40, y + 15], fill="black", width=2)

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
