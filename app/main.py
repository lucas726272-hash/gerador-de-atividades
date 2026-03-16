from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

from app.generator import generate_worksheet
from app.models import Worksheet, WorksheetRequest

app = FastAPI(title="Gerador de Atividades em Português")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/generate", response_model=Worksheet)
def generate(payload: WorksheetRequest) -> Worksheet:
    return generate_worksheet(payload.grade, payload.topic, payload.difficulty, payload.seed)


@app.post("/api/export-pdf")
def export_pdf(worksheet: Worksheet) -> StreamingResponse:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 2 * cm
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(2 * cm, y, worksheet.title)

    y -= 1 * cm
    pdf.setFont("Helvetica", 11)
    pdf.drawString(2 * cm, y, f"Aluno(a): ______________________    Data: ____/____/______")

    y -= 1 * cm
    pdf.drawString(2 * cm, y, f"Instruções: {worksheet.instructions}")

    y -= 1 * cm
    pdf.drawString(
        2 * cm,
        y,
        f"Ano: {worksheet.grade.value}  | Tema: {worksheet.topic.value}  | Nível: {worksheet.difficulty.value}",
    )

    y -= 1 * cm
    for index, exercise in enumerate(worksheet.exercises, start=1):
        if y < 3 * cm:
            pdf.showPage()
            y = height - 2 * cm
            pdf.setFont("Helvetica", 11)
        line = f"{index}. {exercise}"
        for chunk in split_text(line, 96):
            pdf.drawString(2 * cm, y, chunk)
            y -= 0.6 * cm

    y -= 0.4 * cm
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(2 * cm, y, "Desafio Final")
    y -= 0.7 * cm
    pdf.setFont("Helvetica", 11)
    for chunk in split_text(worksheet.final_challenge, 96):
        pdf.drawString(2 * cm, y, chunk)
        y -= 0.6 * cm

    y -= 0.5 * cm
    pdf.setFont("Helvetica", 16)
    pdf.drawString(2 * cm, y, " ".join(worksheet.illustrations))

    pdf.save()
    buffer.seek(0)

    filename = f"atividade-{worksheet.topic.value}.pdf".replace(" ", "-")
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return StreamingResponse(buffer, media_type="application/pdf", headers=headers)


def split_text(text: str, max_chars: int) -> list[str]:
    words = text.split(" ")
    lines: list[str] = []
    current = ""
    for word in words:
        next_line = f"{current} {word}".strip()
        if len(next_line) <= max_chars:
            current = next_line
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines
