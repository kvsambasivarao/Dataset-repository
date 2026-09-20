"""Generate the SCAN-IDS simulated CAN dataset."""
import argparse, csv, random
from pathlib import Path
from .config import *
from .utils import seed_everything, make_payload, format_can_id

FIELDS = ["Timestamp","CAN_ID","ECU","DLC"] + [f"DATA{i}" for i in range(8)] + [
    "Binary_Label","Flag","Severity"
]

def normal_frame(rng, timestamp):
    cid = rng.choice(NORMAL_IDS)
    ecu = CAN_ID_ECU[cid]
    payload = make_payload(ECU_BASELINE[ecu], rng, 5)
    return timestamp, cid, ecu, payload

def build_rows(rng):
    normal_cache = []
    timestamp = 0.0
    for _ in range(FRAME_COUNTS["Normal"]):
        dt = round(rng.uniform(0.0005, 0.01), 6)
        timestamp = round(timestamp + dt, 6)
        ts, cid, ecu, payload = normal_frame(rng, timestamp)
        normal_cache.append((ts,cid,ecu,payload))
        yield record("Normal", ts, cid, ecu, payload)

    for label, count in FRAME_COUNTS.items():
        if label == "Normal": continue
        for _ in range(count):
            dt = round(rng.uniform(0.0005, 0.01), 6)
            timestamp = round(timestamp + dt, 6)
            if label == "DoS Attack":
                cid, ecu, payload = DOS_ID, "Bus", [0]*8
            elif label == "Fuzzy Attack":
                cid, ecu, payload = rng.randint(0,65535), "Unknown", [rng.randint(0,255) for _ in range(8)]
            elif label == "Replay Attack":
                _, cid, ecu, payload = rng.choice(normal_cache)
                payload = list(payload)
            else:
                spoof_ids = {
                    "RPM Spoofing":0x0100, "Gear Spoofing":0x0160,
                    "Brake Spoofing":0x00A0, "Steering Spoofing":0x0140,
                    "Speed Spoofing":0x0120, "Sensor Flooding":0x0200
                }
                cid = spoof_ids[label]
                ecu = CAN_ID_ECU[cid]
                payload = make_payload(ECU_BASELINE[ecu], rng, 5)
                rule = SPOOF_RULES[label]
                for idx,val in zip(rule["byte_idx"], rule["value"]):
                    payload[idx] = val
            yield record(label, timestamp, cid, ecu, payload)

def record(label, ts, cid, ecu, payload):
    return {
        "Timestamp": ts, "CAN_ID": format_can_id(cid), "ECU": ecu, "DLC": 8,
        **{f"DATA{i}": int(payload[i]) for i in range(8)},
        "Binary_Label": 0 if label == "Normal" else 1,
        "Flag": label, "Severity": SEVERITY_MAP[label]
    }

def generate(output, sample=False, seed=SEED):
    rng = seed_everything(seed)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        rows = build_rows(rng)
        for i,row in enumerate(rows,1):
            if sample and i > 1000: break
            w.writerow(row)
    return output

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="data/scan_ids.csv")
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()
    generate(args.output, args.sample, args.seed)
