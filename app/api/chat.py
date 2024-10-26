from fastapi import APIRouter, HTTPException
from app.services.chatgpt_service import ChatGPTService

router = APIRouter()
chatgpt_service = ChatGPTService()

@router.post("/chat")
def chat_with_gpt(prompt: str):
    """
    Endpoint untuk berinteraksi dengan ChatGPT.
    Kirimkan prompt teks dan dapatkan respon dari ChatGPT.
    """
    result = chatgpt_service.get_chatgpt_response(prompt)
    if result:
        return {"response": result.get("choices", [])[0].get("message").get("content")}
    else:
        raise HTTPException(status_code=500, detail="Failed to get response from ChatGPT.")