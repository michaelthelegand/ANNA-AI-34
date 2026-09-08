from app.core.logger import get_logger

logger = get_logger("anna.brain")


def respond(user_input: str) -> str:
    """Route a user message to a basic intent response."""
    message = user_input.strip()

    if not message:
        return "Please tell me how I can help."

    logger.info("Processing message through the brain layer")
    normalized = message.lower()

    if normalized in {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}:
        return "Hello! I’m ANNA. How can I help you today?"

    if "help" in normalized:
        return "I can help with questions, project tasks, health checks, and general conversations."

    if "health" in normalized or "status" in normalized:
        return "ANNA is healthy and ready."

    return f"I received your message: {message}"
