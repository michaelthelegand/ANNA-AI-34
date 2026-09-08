from app.brain.router import respond


def test_respond_returns_message():
    assert "Hello!" in respond("Hello ANNA")


def test_respond_handles_empty_input():
    assert respond("   ") == "Please tell me how I can help."

def test_respond_handles_greeting():
    assert "Hello!" in respond("hello")


def test_respond_handles_help():
    assert "questions" in respond("I need help")


def test_respond_handles_health_status():
    assert "healthy" in respond("health status")


def test_respond_handles_thanks():
    assert "welcome" in respond("thank you")


def test_respond_handles_goodbye():
    assert "Goodbye" in respond("bye")


def test_respond_handles_identity():
    assert "ANNA" in respond("who are you")


def test_respond_handles_capabilities():
    assert "answer questions" in respond("what can you do")


def test_respond_handles_project_question():
    assert "personal AI assistant project" in respond("Tell me about the ANNA AI project")
