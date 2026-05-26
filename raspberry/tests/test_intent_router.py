from robotin.adapters.face_adapter import FaceAdapter
from robotin.adapters.head_adapter import HeadAdapter
from robotin.adapters.light_adapter import LightAdapter
from robotin.ai.mock_intent_service import MockIntentService
from robotin.orchestrator.intent_router import IntentRouter
from robotin.voice.mock_tts import MockTTS


def test_routes_mock_intent_to_adapters() -> None:
    face = FaceAdapter(name="face", simulation=True)
    head = HeadAdapter(name="head", simulation=True)
    lights = LightAdapter(name="light", simulation=True)
    voice = MockTTS()

    router = IntentRouter(face=face, head=head, lights=lights, voice=voice)
    router.route(MockIntentService().next_intent())

    assert face.sent_lines == [
        "FACE EXPR happy",
        "FACE LOOK center",
        "FACE MOUTH talking",
    ]
    assert lights.sent_lines == ["LIGHT MODE warm"]
    assert head.sent_lines == ["HEAD GESTURE small_nod"]
    assert voice.spoken == ["Hola, soy Robotin."]
