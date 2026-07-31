import re

def extract_information(text):

    info = {
        "Document Type": None,
        "Vendor": None,
        "Vendee": None,
        "Registration Number": None,
        "Property Area": None,
        "Sale Price": None
    }

    if "SALE DEED" in text.upper():
        info["Document Type"] = "Sale Deed"

    return info