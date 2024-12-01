import fitz  # PyMuPDF
from app.models.data.models import Viaggio
from app.schemas import ViaggioCreate
from sqlalchemy.orm import Session
from typing import List
from app.services.ai_tool import analyze_image_with_llama_vision
from datetime import date

class FileToViaggioService:

    def __init__(self, db: Session):
        self.db = db

    def process_pdf(self, pdf_file_path: str) -> List[Viaggio]:
        # Apri il PDF
        document = fitz.open(pdf_file_path)
        viaggi = []

        # Itera su ogni pagina del PDF
        for page_number in range(len(document)):
            page = document.load_page(page_number)

            # Converte la pagina in un'immagine
            pix = page.get_pixmap()
            img_bytes = pix.tobytes()

            # Utilizza Llama Vision per analizzare l'immagine della pagina
            viaggio_info = analyze_image_with_llama_vision(img_bytes)

            if viaggio_info:
                # Creazione dell'oggetto Viaggio in base alle informazioni estratte
                nuovo_viaggio = ViaggioCreate(
                    destinazione=viaggio_info['destinazione'],
                    data_partenza=viaggio_info['data_partenza'],
                    data_arrivo=viaggio_info['data_arrivo'],
                    stato="PIANIFICATO"
                )
                db_viaggio = Viaggio(**nuovo_viaggio.dict())
                self.db.add(db_viaggio)
                viaggi.append(db_viaggio)

        # Commit dei viaggi creati
        self.db.commit()
        return viaggi