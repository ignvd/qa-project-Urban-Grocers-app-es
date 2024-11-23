BASE_KIT_BODY = {"name": ""}

KIT_BODIES = {
    "valid_min_length": {"name": "a"},
    "valid_max_length": {"name": "a" * 511},
    "too_short": {"name": ""},
    "too_long": {"name": "a" * 512},
    "special_chars": {"name": "№%@,"},
    "spaces": {"name": " a "},
    "numbers": {"name": "123"},
    "missing_name": {}
}
