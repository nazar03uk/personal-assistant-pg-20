import pickle
from pathlib import Path
from addressbook import AddressBook
from notes import NotesBook

# Зберігаємо у домашній папці користувача
APP_DIR = Path.home() / ".personal_assistant"
APP_DIR.mkdir(parents=True, exist_ok=True)

ABOOK_FILE = APP_DIR / "addressbook.pkl"
NOTES_FILE = APP_DIR / "notes.pkl"


# --- Адресна книга ---

def save_addressbook(book: AddressBook) -> None:
    with ABOOK_FILE.open("wb") as f:
        pickle.dump(book, f)


def load_addressbook() -> AddressBook:
    if ABOOK_FILE.exists():
        with ABOOK_FILE.open("rb") as f:
            return pickle.load(f)
    return AddressBook()


# --- Нотатки ---

def save_notes(notes: NotesBook) -> None:
    with NOTES_FILE.open("wb") as f:
        pickle.dump(notes, f)


def load_notes() -> NotesBook:
    if NOTES_FILE.exists():
        with NOTES_FILE.open("rb") as f:
            return pickle.load(f)
    return NotesBook()
