def detect_risks(text):

    text = text.lower()

    risks = []

    checks = {
        "Vendor": ["vendor"],
        "Vendee": ["vendee", "buyer", "purchaser"],
        "Sale Price": ["rs.", "price", "consideration"],
        "Registration Number": ["registration"],
        "Property Address": ["property", "schedule"],
        "Witness": ["witness"],
        "Signature": ["signature", "signed"]
    }

    for field, keywords in checks.items():

        found = False

        for keyword in keywords:
            if keyword in text:
                found = True
                break

        if not found:
            risks.append(f"{field} is Missing")

    return risks