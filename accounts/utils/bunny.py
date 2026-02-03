import uuid
import requests

# 🔴 Hard-coded Bunny credentials (NOT recommended for production)
BUNNY_STORAGE_ZONE = "resumes-jobportal"
BUNNY_STORAGE_PASSWORD = "41d59899-fe28-48cd-afd4e603db33-7195-4204"
BUNNY_PULL_ZONE_URL = "https://resume-jobportal.b-cdn.net"


def upload_pdf_to_bunny(file_obj):
    file_name = f"resumes/{uuid.uuid4()}.pdf"

    upload_url = (
        f"https://storage.bunnycdn.com/"
        f"{BUNNY_STORAGE_ZONE}/{file_name}"
    )

    headers = {
        "AccessKey": BUNNY_STORAGE_PASSWORD,
        "Content-Type": "application/pdf",
    }

    response = requests.put(
        upload_url,
        headers=headers,
        data=file_obj.read()
    )

    if response.status_code not in (200, 201):
        raise Exception(
            f"Bunny upload failed: {response.status_code} - {response.text}"
        )

    file_obj.seek(0)

    return f"{BUNNY_PULL_ZONE_URL}/{file_name}"
