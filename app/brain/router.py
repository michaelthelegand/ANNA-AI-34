from datetime import datetime

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

    if normalized in {"what time is it", "what is the time", "current time", "time"}:
        current_time = datetime.now().strftime("%I:%M %p").lstrip("0")
        return f"The current local time is {current_time}."

    if normalized in {"what is today's date", "what is the date", "today's date", "date"}:
        current_date = datetime.now().strftime("%B %d, %Y").replace(" 0", " ")
        return f"Today's date is {current_date}."

    if normalized in {"thanks", "thank you", "thx"}:
        return "You are welcome. I am happy to help."

    if normalized in {"bye", "goodbye", "good night", "see you"}:
        return "Goodbye! I will be here whenever you need me."

    if normalized in {"who are you", "what are you", "what is your name"}:
        return "I am ANNA, your personal AI assistant."

    if normalized in {"how are you", "how are you doing", "are you okay"}:
        return "I am doing well and ready to help."

    if normalized in {"what can you do", "what do you do", "your capabilities"}:
        return "I can answer questions, help with projects, explain concepts, check system health, and support general conversations."

    if "project" in normalized or "anna ai" in normalized:
        return "ANNA AI is a personal AI assistant project designed to grow through modular features like conversation, memory, tools, voice, and learning."

    if "help" in normalized:
        return "I can help with questions, project tasks, health checks, and general conversations."

    if "health" in normalized or "status" in normalized:
        return "ANNA is healthy and ready."

    return f"I received your message: {message}"
