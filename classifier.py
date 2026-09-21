"""Простой классификатор обращений на основе ключевых слов."""

from pathlib import Path
import sys


def classify(message: str) -> tuple[str, str]:
    """Вернуть категорию и черновик ответа для одного обращения."""
    text = message.lower()

    if any(word in text for word in ("очеред", "холодн", "пропал", "не работает")):
        return (
            "жалоба",
            "Спасибо, что сообщили. Передадим информацию ответственным сотрудникам "
            "и постараемся решить проблему как можно скорее.",
        )

    if any(word in text for word in ("справк", "где парков", "парковк")):
        return (
            "справка",
            "Здравствуйте! Подскажем порядок получения информации и нужные контакты. "
            "Уточните, пожалуйста, ваш факультет или цель обращения.",
        )

    return (
        "другое",
        "Здравствуйте! Приняли обращение. Уточним возможность записи и вернёмся "
        "к вам с подтверждением.",
    )


def main() -> None:
    # Не падать в Windows-консоли с локальной кодировкой cp1251.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    messages_path = Path(__file__).with_name("messages.txt")
    messages = [line.strip() for line in messages_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    for number, message in enumerate(messages, start=1):
        category, answer = classify(message)
        print(f"{number}. {message}")
        print(f"   Категория: {category}")
        print(f"   Ответ: {answer}")
        print()


if __name__ == "__main__":
    main()
