from src.config import ATTACK_CLASSES, FRAME_COUNTS, SEVERITY_MAP
def test_taxonomy():
    assert len(ATTACK_CLASSES) == 10
    assert sum(FRAME_COUNTS.values()) == 500000
    assert set(SEVERITY_MAP) == set(ATTACK_CLASSES)
