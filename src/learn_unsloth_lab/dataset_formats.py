ALLOWED_ROLES = {"system", "user", "assistant"}


def detect_format(record):
    if {"instruction", "output"} <= set(record):
        return "alpaca"
    if "messages" in record:
        return "chatml"
    if "conversations" in record:
        return "sharegpt"
    raise ValueError("Unknown dataset record format")


def normalize_record(record):
    source_format = detect_format(record)
    if source_format == "alpaca":
        prompt = record["instruction"]
        if record.get("input"):
            prompt = f"{prompt}\n\n{record['input']}"
        messages = [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": record["output"]},
        ]
    elif source_format == "chatml":
        messages = [
            {"role": item["role"], "content": item["content"]}
            for item in record["messages"]
        ]
    else:
        role_map = {"human": "user", "gpt": "assistant", "system": "system"}
        messages = [
            {"role": role_map.get(item["from"], item["from"]), "content": item["value"]}
            for item in record["conversations"]
        ]
    return {"messages": messages}
