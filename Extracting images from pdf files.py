import fitz
import PIL.Image
import io

pdf = fitz.open(r"C:\Users\Cash\Downloads\testing.pdf")

counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        path = r"C:\Users\Cash\Documents\pruebas_python\proyectos\pdf"
        y = "/"
        image_name = f"image{counter}.{extension}"
        image_path = f"{path}{y}{image_name}"
        img.save(open(f"{image_path}", "wb"))
        counter  = counter +1
