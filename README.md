# Pytest + Playwright Framework (Python)

Simple and scalable Playwright automation framework using:

- Python
- Pytest
- Playwright
- `.env` secrets management

---

# Project Structure

```text
project/
│
├── tests/
│   ├── TC-RM-PKG
│   └── TC-RM-PMR
│
├── conftest.py
├── config.py
├── .env
├── pytest.ini
├── requirements.txt
└── README.md
```

# Environment Variables

Create `.env`

```env
BASE_URL=https://example:7503/mmmWeb/login
BASE_UNAME=ADMIN
PASSWORD=ADMIN

HEADLESS=false
TIMEOUT=30000

PKG_CONFIG=EXAMPLE_ACCT_V1
PKG_TRANS=EXAMPLE_ACCT_V2
REL_MMGT=REL_PKG
```

---

# Variable Description

| Variable     | Description                                 |
| ------------ | ------------------------------------------- |
| `BASE_URL`   | Application login URL                       |
| `BASE_UNAME` | Login username                              |
| `PASSWORD`   | Login password                              |
| `HEADLESS`   | Run browser in headless mode (`true/false`) |
| `TIMEOUT`    | Default timeout in milliseconds             |
| `PKG_CONFIG` | Package configuration name                  |
| `PKG_TRANS`  | Package transaction name                    |
| `REL_MMGT`   | Release management package name             |

# Running Test Cases

---

# Run All Test Cases

```bash
pytest
```

---

# Run in Headed Mode (Visible Browser)

```bash
pytest --headed
```

---

# Run Specific Test File

```bash
pytest tests/TC-RM-PKG-001 — Create new Configuration Package.py
```

---

# Run Specific Test Function

```bash
pytest tests/TC-RM-PKG-001 — Create new Configuration Package.py::test_example
```

---

# Ignore HTTPS / SSL Errors

Useful for self-signed certificates.

```bash
pytest --ignore-https-errors
```

---

# Reinstall Playwright Browsers

```bash
playwright install
```
