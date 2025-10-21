import os

def test_qr_generated():
    # Run your script to generate a QR code
    os.system("python main.py --url https://github.com/ArthNangar/assignment7_qr_codemaker")

    # Check if the 'qr_codes' folder has any PNG files
    assert any(f.endswith(".png") for f in os.listdir("qr_codes")), "❌ No QR code generated!"
