def format_label(class_id):
    label_map = {0: "Human", 1: "Vehicle"}
    return label_map.get(class_id, "Unknown")
