# Estas son las funciones necesarias para el editor de imágenes
# Pegarlas DESPUÉS de agregar los botones

def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Abrir imagen", "", "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_name:
            self.current_image = Image.open(file_name).convert("RGB")
            self.display_image(self.current_image)

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

    def grises_image(self, img):
        pass

    def sepia_image(self, img):
        pass

    def rotar_der_imagen(self, img):
        pass

    def rotar_izq_imagen(self, img):
        pass

    def stickers(self, img):
        pass
