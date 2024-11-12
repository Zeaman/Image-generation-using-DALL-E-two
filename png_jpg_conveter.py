# Convert the generated PNG image to JPG format and save it with the specified name.
input_path_encouraging = '/png_source_file_path.png'
output_path_encouraging = '/output_jpg_file_path.jpg'

# Open the generated PNG image
img_encouraging = Image.open(input_path_encouraging)

# Convert to RGB and save as JPG
img_encouraging = img_encouraging.convert("RGB")
img_encouraging.save(output_path_encouraging, "JPEG")

output_path_encouraging
