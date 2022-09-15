from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

def generate_certificate(name):
    try:
        print(BASE_DIR)
        # adjust the position according to 
        # your sample
        text_y_position = 700 
    
        # opens the image
        img = Image.open(BASE_DIR / 'c.png', mode ='r')
            
        # gets the image width
        image_width = img.width
            
        # creates a drawing canvas overlay 
        # on top of the image
        draw = ImageDraw.Draw(img)

        # gets the font object from the 
        # font file (TTF)
        font = ImageFont.truetype(
            str(BASE_DIR / 'Satisfy-Regular.ttf'),
            150 # change this according to your needs
        )

        # fetches the text width for 
        # calculations later on
        text_width, _ = draw.textsize(name, font = font)

        draw.text(
            (
                # this calculation is done 
                # to centre the image
                (image_width - text_width) / 2,
                text_y_position,
            ),
            name,
            font = font,
            fill="#000"        )
    
            # saves the image in png format
        # img.save(BASE_DIR / 'certificates/{}.png'.format(name)) 
        return img

    except Exception as e:
        print(e)