# Quick Note Python

[![PyPI Version](https://img.shields.io/pypi/v/quick-note-python?style=flat-square)](https://pypi.org/project/quick-note-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/quick-note-python?style=flat-square)](https://pypi.org/project/quick-note-python/)
[![License](https://img.shields.io/pypi/l/quick-note-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/quick-note-python?style=flat-square)](https://pypi.org/project/quick-note-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/quick-note-python?style=flat-square)](https://github.com/mizoz/quick-note-python)

> A fast and simple Python CLI tool for capturing ideas and notes instantly from the command line.

## Features

- Quick note capture from command line
- Note organization with tags
- Search notes by content or tag
- Note editing and deletion
- Export notes to various formats
- Lightweight and fast

## Installation

### From PyPI

```bash
pip install quick-note-python
```

### From Source

```bash
git clone https://github.com/mizoz/quick-note-python.git
cd quick-note-python
pip install -e .
```

## Usage

### Command Line

```bash
# Create a new note
quick-note "My new idea"

# Create note with tags
quick-note "Meeting notes" --tag work meeting

# List all notes
quick-note list

# Search notes
quick-note search "idea"

# Delete a note
quick-note delete 1
```

### Python API

```python
from quick_note import QuickNote

notes = QuickNote()

# Add a note
notes.add("My new idea", tags=["idea"])

# List all notes
all_notes = notes.list()
print(all_notes)

# Search notes
results = notes.search("idea")
```

## CLI Options

| Option | Description |
|--------|-------------|
| `list` | List all notes |
| `search <query>` | Search notes |
| `delete <id>` | Delete a note by ID |
| `--tag` | Add tags to a note |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
