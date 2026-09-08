from app.core.logger import get_logger

logger = get_logger("anna.brain")


def respond(user_input: str) -> str:
    """Generate a safe starter response for a normal user message."""
    message = user_input.strip()

    if not message:
        return "Please tell me how I can help."

    logger.info("Processing message through the brain layer")
    return f"I received your message: {message}"
