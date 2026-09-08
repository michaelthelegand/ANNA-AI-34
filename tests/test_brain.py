from app.brain.router import respond


def test_respond_returns_message():
    assert respond("Hello ANNA") == "I received your message: Hello ANNA"


def test_respond_handles_empty_input():
    assert respond("   ") == "Please tell me how I can help."

def test_respond_handles_greeting():
    assert "Hello!" in respond("hello")


def test_respond_handles_help():
    assert "questions" in respond("I need help")


def test_respond_handles_health_status():
    assert "healthy" in respond("health status")
