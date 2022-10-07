from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


def generate_certificate(data):
    try:
        print(BASE_DIR)
        # adjust the position according to
        # your sample
        text_y_position = 700

        # opens the image
        img = Image.open(BASE_DIR / 'c.png', mode='r')

        # gets the image width
        image_width = img.width

        # creates a drawing canvas overlay
        # on top of the image
        draw = ImageDraw.Draw(img)

        # gets the font object from the
        # font file (TTF)
        font = ImageFont.truetype(
            str(BASE_DIR / 'calibrib.ttf'),
            75  # change this according to your needs
        )

        # fetches the text width for
        # calculations later on
        text_width, _ = draw.textsize(data["name"], font=font)

        # name on certificate
        draw.text(
            (
                930,    # x-pos
                1100,   # y-pos
            ),
            data["name"],
            font=font,
            fill="#000")

        # Course name on certificate
        draw.text(
            (
                1800,    # x-pos
                1245,    # y-pos
            ),
            data["course"],
            font=font,
            fill="#000")

        # Course start date on certificate
        draw.text(
            (
                1290,    # x-pos
                1680,    # y-pos
            ),
            data["course"],
            font=font,
            fill="#000")

        # Course start date on certificate
        draw.text(
            (
                1750,    # x-pos
                1680,    # y-pos
            ),
            data["course"],
            font=font,
            fill="#000")
        # saves the image in png format
        # img.save(BASE_DIR / 'certificates/{}.png'.format(name))
        return img

    except Exception as e:
        print(e)
