"""SCAN-IDS configuration: taxonomy, ECU attribution, severity and generation parameters."""

SEED = 12345

ECU_CATEGORIES = [
    "Engine", "Transmission", "ABS", "ADAS", "Steering",
    "Body", "Battery", "Bus", "Wheel", "Airbag", "Unknown"
]

ATTACK_CLASSES = [
    "Normal", "DoS Attack", "Fuzzy Attack", "Replay Attack",
    "RPM Spoofing", "Gear Spoofing", "Brake Spoofing",
    "Steering Spoofing", "Speed Spoofing", "Sensor Flooding"
]

SEVERITY_MAP = {
    "Normal": "Low",
    "DoS Attack": "Critical",
    "Fuzzy Attack": "Medium",
    "Replay Attack": "Medium",
    "RPM Spoofing": "High",
    "Gear Spoofing": "Critical",
    "Brake Spoofing": "Critical",
    "Steering Spoofing": "Critical",
    "Speed Spoofing": "High",
    "Sensor Flooding": "High",
}

SEVERITY_ORDER = {"Low": 0, "Medium": 1, "High": 2, "Critical": 3}

FRAME_COUNTS = {
    "Normal": 250000,
    "DoS Attack": 30000,
    "Fuzzy Attack": 30000,
    "Replay Attack": 30000,
    "RPM Spoofing": 30000,
    "Gear Spoofing": 30000,
    "Brake Spoofing": 25000,
    "Steering Spoofing": 25000,
    "Speed Spoofing": 25000,
    "Sensor Flooding": 25000,
}

CAN_ID_ECU = {
    0x0080: "Airbag", 0x00A0: "ABS", 0x00C0: "ABS",
    0x0100: "Engine", 0x0120: "Engine", 0x0130: "Engine",
    0x0140: "Steering", 0x0160: "Transmission", 0x0180: "Transmission",
    0x01A0: "Battery", 0x01C0: "Battery",
    0x0200: "Body", 0x0220: "Body",
    0x0240: "Wheel", 0x0260: "ADAS", 0x0280: "ADAS",
}

NORMAL_IDS = tuple(CAN_ID_ECU.keys())
DOS_ID = 0x0000

ECU_BASELINE = {
    "Engine":       [0x10, 0x8A, 0x32, 0x00, 0x64, 0x00, 0xFF, 0x00],
    "Transmission": [0x20, 0x01, 0x02, 0x03, 0x40, 0x80, 0x00, 0x00],
    "ABS":          [0x30, 0x00, 0x64, 0x64, 0x00, 0x00, 0xAA, 0xBB],
    "ADAS":         [0x40, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77],
    "Steering":     [0x50, 0x80, 0x00, 0x7F, 0x00, 0x00, 0x10, 0x20],
    "Body":         [0x60, 0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0xFF],
    "Battery":      [0x70, 0x64, 0x00, 0xC8, 0x00, 0x00, 0x00, 0x00],
    "Bus":          [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    "Wheel":         [0x30, 0x32, 0x32, 0x32, 0x32, 0x00, 0x00, 0x00],
    "Airbag":        [0x60, 0xFF, 0x00, 0xFF, 0x00, 0xFF, 0x00, 0xFF],
    "Unknown":       [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
}

SPOOF_RULES = {
    "RPM Spoofing": {"byte_idx": [2, 3], "value": [0xFF, 0xFF]},
    "Gear Spoofing": {"byte_idx": [1], "value": [0xFF]},
    "Brake Spoofing": {"byte_idx": [2, 3], "value": [0x00, 0x00]},
    "Steering Spoofing": {"byte_idx": [1, 2], "value": [0xFF, 0x00]},
    "Speed Spoofing": {"byte_idx": [4], "value": [0xFF]},
    "Sensor Flooding": {"byte_idx": [0, 1, 2, 3], "value": [0xFF]*4},
}

TIMING = {
    "Normal": 0.01, "DoS Attack": 0.001, "Fuzzy Attack": 0.005,
    "Replay Attack": 0.01, "RPM Spoofing": 0.01, "Gear Spoofing": 0.02,
    "Brake Spoofing": 0.01, "Steering Spoofing": 0.01,
    "Speed Spoofing": 0.01, "Sensor Flooding": 0.002,
}
