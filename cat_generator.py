from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(img)

# Draw cat head (ellipse)
draw.ellipse((50, 50, 150, 150), fill='lightgray')

# Draw ears (triangles)
draw.polygon([(60, 50), (75, 30), (90, 50)], fill='lightgray')
draw.polygon([(110, 50), (125, 30), (140, 50)], fill='lightgray')

# Draw eyes (circles)
draw.ellipse((75, 75, 85, 85), fill='black')
draw.ellipse((115, 75, 125, 85), fill='black')

# Draw nose (triangle)
draw.polygon([(95, 95), (100, 105), (105, 95)], fill='pink')

# Draw mouth (arc)
draw.arc((90, 105, 110, 115), start=0, end=180, fill='black', width=2)

# Draw whiskers (lines)
draw.line((50, 95, 75, 90), fill='black', width=2)
draw.line((50, 100, 75, 100), fill='black', width=2)
draw.line((125, 90, 150, 95), fill='black', width=2)
draw.line((125, 100, 150, 100), fill='black', width=2)

# Save the image as BMP
img.save('New Bitmap image.bmp')