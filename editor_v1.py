# copia esta función 
def display_image(self, img):
    img = img.convert("RGB")
    max_width, max_height = self.image_label.width(), self.image_label.height()
    img = img.copy()
    img.thumbnail((max_width, max_height), Image.LANCZOS)
    data = img.tobytes("raw", "RGB")
    w, h = img.size
    qimg = QImage(data, w, h, w * 3, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(qimg)
    self.image_label.setPixmap(pixmap)
