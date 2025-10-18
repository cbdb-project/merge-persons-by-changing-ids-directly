import runpy
from pathlib import Path

import requests


class DummyResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self._payload = payload

    def json(self):
        return self._payload


def test_pair_list_generation(tmp_path, monkeypatch):
    script_path = Path(__file__).resolve().parent.parent / "1_create_pair_list.py"
    input_content = (
        "Reason A\t\t10\t20\t30(s1)\n"
        "Reason B\t\t5\t5\t40\n"
        "Reason C\t\t100\t50\n"
        "Reason D\t\t7\t200\n"
    )
    (tmp_path / "input_original.txt").write_text(input_content, encoding="utf-8")

    name_map = {
        10: "Primary",
        20: "Alt20",
        30: "Primary",
        5: "Five",
        40: "Forty",
        100: "Big",
        50: "Small",
        7: "Seven",
        200: "Two Hundred",
    }

    def fake_get(url):
        person_id = int(url.rstrip("/").split("/")[-1])
        if person_id in name_map:
            return DummyResponse(200, {"c_name_chn": name_map[person_id]})
        return DummyResponse(404, {})

    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.chdir(tmp_path)

    runpy.run_path(str(script_path), run_name="__main__")

    id_list_lines = (
        (tmp_path / "id_list.txt").read_text(encoding="utf-8").strip().splitlines()
    )
    assert id_list_lines == [
        "10\t30\ts1\tReason A",
        "10\t20\tNone\tReason A",
        "5\t40\tNone\tReason B",
        "50\t100\tNone\tReason C",
        "7\t200\tNone\tReason D",
    ]

    id_list_with_name_lines = (
        (tmp_path / "id_list_with_name_for_check.txt")
        .read_text(encoding="utf-8")
        .strip()
        .splitlines()
    )
    assert id_list_with_name_lines == [
        "10\tPrimary\t30\tPrimary\t\ts1\tReason A",
        "10\tPrimary\t20\tAlt20\tneed_check\tNone\tReason A",
        "5\tFive\t40\tForty\tneed_check\tNone\tReason B",
        "50\tSmall\t100\tBig\tneed_check\tNone\tReason C",
        "7\tSeven\t200\tTwo Hundred\tneed_check\tNone\tReason D",
    ]
