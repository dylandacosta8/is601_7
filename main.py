import os
import qrcode
import logging
import re
from datetime import datetime
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file, if available
load_dotenv()

# Set environment variables with defaults if not specified
qr_data_url = os.getenv("QR_DATA_URL", "https://github.com/dylandacosta8/is601_7")
qr_code_dir = os.getenv("QR_CODE_DIR", "data")
fill_color = os.getenv("FILL_COLOR", "blue")
back_color = os.getenv("BACK_COLOR", "yellow")
env = os.getenv("ENV", "prod").lower()

print(qr_code_dir)

# Configure logging directory and file
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, "qr.log")

# Configure logging based on environment
log_level = logging.WARNING
if env == "dev":
    log_level = logging.DEBUG
elif env == "uat":
    log_level = logging.INFO

logging.basicConfig(
    level=log_level,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler(log_file_path)  # Log to file
    ]
)

# Ensure the directory for QR code images exists
os.makedirs(qr_code_dir, exist_ok=True)

# Generate timestamped filename
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
domain = re.sub(r'\W+', '_', qr_data_url)
filename = f"{timestamp}_{domain}.png"
file_path = os.path.join(qr_code_dir, filename)
normalized_file_path = os.path.normpath(file_path)

# Log the environment settings
logging.debug(f"Environment: {env}")
logging.debug(f"QR Code Directory: {qr_code_dir}")
logging.debug(f"Fill Color: {fill_color}")
logging.debug(f"Back Color: {back_color}")
logging.info(f"Generating QR code for URL: {qr_data_url}")

# Create and customize QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(qr_data_url)
qr.make(fit=True)

# Generate the QR code image with specified colors
img = qr.make_image(fill_color=fill_color, back_color=back_color)

# Save the QR code image
img.save(file_path)
logging.info(f"QR code saved at {normalized_file_path}")

# Display the QR code
img.show()
