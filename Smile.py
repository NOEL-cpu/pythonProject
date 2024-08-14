from PIL import Image, ImageDraw

def create_smiley(size=200):
    # Создание нового изображения с белым фоном
    image = Image.new("RGB", (size, size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Рисование желтого круга для лица
    draw.ellipse((10, 10, size-10, size-10), fill=(255, 255, 0), outline=(0, 0, 0))

    # Рисование глаз
    draw.ellipse((size*0.25, size*0.25, size*0.35, size*0.35), fill=(0, 0, 0))
    draw.ellipse((size*0.65, size*0.25, size*0.75, size*0.35), fill=(0, 0, 0))

    # Рисование рта
    draw.arc((size*0.25, size*0.55, size*0.75, size*0.85), start=0, end=180, fill=(0, 0, 0))

    # Сохранение изображения
    image.save("smiley.png")
