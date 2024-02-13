import subprocess
import os

def take(url, filename="screenshot.jpg", full_page=False):
    result = subprocess.run(
        ["node", "screenshot.js", url, str(full_page)],
        capture_output=True,
        text=True,  # Ensures output is in text form, not bytes
        check=True  # Raises an exception if the command exits with a non-zero status
    )
    if result.returncode == 0:
        print("Screenshot taken successfully!")
    else:
        print(f"Error taking screenshot: {result.stderr}")

    if filename != "screenshot.jpg":
        os.rename("screenshot.jpg", filename)

    return filename
