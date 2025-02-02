import subprocess
import shutil
import os


def compress_pdf(input_pdf, output_pdf):
    # Проверяем, установлен ли Ghostscript
    if not shutil.which("gs"):
        print("Ошибка: Ghostscript не установлен или недоступен.")
        return

    # Проверяем, существует ли входной PDF-файл
    if not os.path.exists(input_pdf):
        print(f"Ошибка: Файл '{input_pdf}' не найден.")
        return

    # Параметры сжатия Ghostscript
    gs_command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook",  # Использование среднего уровня сжатия
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf
    ]

    try:
        # Выполняем команду и перехватываем ошибки
        result = subprocess.run(gs_command, capture_output=True, text=True)

        if result.returncode == 0:
            print("Сжатие завершено успешно!")
        else:
            print(f"Ошибка при сжатии PDF: {result.stderr}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пути к файлам (замени на свои)
input_pdf = " "  # Путь к входному PDF
output_pdf = " "  # Путь к выходному PDF

# Вызов функции сжатия
compress_pdf(input_pdf, output_pdf)