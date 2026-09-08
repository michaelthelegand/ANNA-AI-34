from app.brain.router import respond
from app.core.health import health_check
from app.core.logger import get_logger

logger = get_logger("anna.cli")

HELP_TEXT = """Commands:
  /help    Show available commands
  /health  Check ANNA AI system health
  /exit    Exit ANNA AI
"""


def run_cli() -> None:
    print("ANNA AI CLI")
    print("Type /help for commands or /exit to quit.")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not user_input:
            continue

        command = user_input.lower()

        if command in {"/exit", "exit", "quit"}:
            print("Goodbye.")
            break

        if command == "/help":
            print(HELP_TEXT)
            continue

        if command == "/health":
            print(health_check())
            continue

        print(f"ANNA: {respond(user_input)}")


if __name__ == "__main__":
    run_cli()
