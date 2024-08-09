import os
import json
from .websocket import ConnectionManager

from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocketDisconnect

router = APIRouter()

basedir = os.path.abspath(os.path.dirname(__file__))
templates = Jinja2Templates(directory=os.path.join(basedir, 'templates'))


manager = ConnectionManager()



# @router.websocket("/ws/{client_id}")
# async def websocket_endpoint(websocket: WebSocket, client_id: str):
#     await manager.connect(websocket, client_id)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             # Process the received data
#     except WebSocketDisconnect:
#         manager.disconnect(client_id)
#         await manager.broadcast(f"Client #{client_id} left the game")


# @router.get('/admin', response_class=HTMLResponse)
# async def admin(request: Request):
#     questions = [
#         {'id': 1, 'body': 'test1'},
#         {'id': 2, 'body': 'test2'},
#         {'id': 3, 'body': 'test3'},
#         {'id': 4, 'body': 'test4'},
#     ]

#     return templates.TemplateResponse(
#         request=request,
#         name='admin.html',
#         context={'questions': questions},
#     )


# @router.post("/admin/start_question")
# async def start_question(question: str):
#     # game.start_question(question)
#     await manager.broadcast(json.dumps({"type": "question", "content": question}))
#     return {"status": "Question started"}


# @router.post("/admin/enable_answers")
# async def enable_answers():
#     # game.enable_answering()
#     await manager.broadcast(json.dumps({"type": "enable_answers"}))
#     return {"status": "Answers enabled"}


# @router.post("/admin/finish_question")
# async def finish_question():
#     # game.finish_question()
#     # Broadcast updated scores
#     return {"status": "Question finished"}


# @router.post("/admin/next_round")
# async def next_round():
#     # game.next_round()
#     # if game.state == GameState.FINISHED:
#     #     await manager.broadcast(json.dumps({"type": "game_over"}))
#     return {
#         # "status": "Next round started" if game.state != GameState.FINISHED else "Game over",
#     }
