import os
import re
import shutil

# Verzeichnisse definieren
posts_dir = r"D:\Program Files\Obsidian\vaults\my-second-brain\My Second Brain\posts"
attachments_dir = r"D:\Program Files\Obsidian\vaults\my-second-brain\My Second Brain\attachements"
static_images_dir = r"D:\GitHub\mysecondbrain\static\images"

# Schritt 1: Markdown-Dateien im Post-Verzeichnis verarbeiten
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Schritt 2: Alle Bild-Links im Format [[Pasted image ... .png]] finden
        images = re.findall(r'\[\[([^\]]*\.png)\]\]', content)

        # Schritt 3: Bild-Links ersetzen und sicherstellen, dass URLs korrekt formatiert sind
        for image in images:
            # Markdown-kompatiblen Link mit %20 für Leerzeichen vorbereiten
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)

            # Schritt 4: Bild in das Hugo static/images Verzeichnis kopieren, falls es existiert
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Schritt 5: Aktualisierten Inhalt zurück in die Markdown-Datei schreiben
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown-Dateien verarbeitet und Bilder erfolgreich kopiert.")