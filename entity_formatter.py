import re


def is_valid_entity(word):
    """
    Check whether the extracted entity is valid.
    """

    invalid = ["&", ".", ",", "(", ")", "-", ":", ";"]

    word = word.strip()

    if word in invalid:
        return False

    if len(word) <= 1:
        return False

    return True


def organize_entities(entities, text):

    result = {
        "Person": [],
        "Organization": [],
        "Location": [],
        "Money": [],
        "Date": []
    }

    # -----------------------------
    # BERT NER
    # -----------------------------

    for entity in entities:

        label = entity["entity_group"]
        word = entity["word"].strip()

        if not is_valid_entity(word):
            continue

        if label == "PER":
            if word not in result["Person"]:
                result["Person"].append(word)

        elif label == "ORG":
            if word not in result["Organization"]:
                result["Organization"].append(word)

        elif label == "LOC":
            if word not in result["Location"]:
                result["Location"].append(word)

    # -----------------------------
    # REGEX FOR MONEY
    # -----------------------------

    money_pattern = r"Rs\.?\s?[\d,]+/?-?"

    money = re.findall(money_pattern, text)

    for m in money:
        if m not in result["Money"]:
            result["Money"].append(m)

    # -----------------------------
    # REGEX FOR DATE
    # -----------------------------

    date_pattern = r"\d{1,2}(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?[A-Za-z]+,\s+\d{4}"

    dates = re.findall(date_pattern, text)

    for d in dates:
        if d not in result["Date"]:
            result["Date"].append(d)

    return result
