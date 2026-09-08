from app.core.logger import get_logger

logger = get_logger("anna.brain")


def respond(user_input: str) -> str:
    """Route a user message to a basic intent response."""
    message = user_input.strip()

    if not message:
        return "Please tell me how I can help."

    logger.info("Processing message through the brain layer")
    normalized = " ".join(message.lower().split())

    if normalized in {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"} or normalized.startswith(("hi ", "hello ", "hey ")):
        return "Hello! I am ANNA. How can I help you today?"

    if normalized in {"thanks", "thank you", "thx"}:
        return "You are welcome. I am happy to help."

    if normalized in {"bye", "goodbye", "good night", "see you"}:
        return "Goodbye! I will be here whenever you need me."

    if normalized in {"who are you", "what are you", "what is your name"}:
        return "I am ANNA, your personal AI assistant."

    if "help" in normalized:
        return "I can help with questions, project tasks, health checks, and general conversations."

    if "health" in normalized or "status" in normalized:
        return "ANNA is healthy and ready."

    return f"I received your message: {message}"
