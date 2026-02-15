# Quick Note Python

A fast and simple note-taking CLI tool for capturing ideas instantly.

## Features

- Quick note capture from command line
- Note organization with tags
- Search notes by content or tag
- Note editing and deletion
- Export notes to various formats
- Lightweight and fast

## Installation

```bash
pip install quick-note-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/quick-note-python.git
cd quick-note-python
pip install -e .
```

## Usage

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

## Options

- `list` - List all notes
- `search <query>` - Search notes
- `delete <id>` - Delete a note by ID
- `--tag` - Add tags to a note

## License

MIT License

## Author

mizoz
