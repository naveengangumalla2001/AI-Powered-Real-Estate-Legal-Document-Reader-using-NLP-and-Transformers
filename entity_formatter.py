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


def organize_entities(entities):

    result = {
        "Person": [],
        "Organization": [],
        "Location": [],
        "Money": [],
        "Date": []
    }

    for entity in entities:

        label = entity["entity_group"]
        word = entity["word"].strip()

        # Skip invalid entities
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

        elif label == "MONEY":
            if word not in result["Money"]:
                result["Money"].append(word)

        elif label == "DATE":
            if word not in result["Date"]:
                result["Date"].append(word)

    return result