BASE_KIT_BODY = {"name": ""}

Corregido para evitar problemas con librerías y asegurar datos consistentes:

```python
user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

KIT_BODIES = {
    "valid_min_length": {"name": "a"},
    "valid_max_length": {"name": "a" * 511},
    "too_short": {"name": ""},
    "too_long": {"name": "a" * 512},
    "special_chars": {"name": "№%@,"},
    "spaces": {"name": " A Aaa "},
    "numbers": {"name": "123"},
    "missing_name": {},
    "invalid_type": {"name": 123},
}
