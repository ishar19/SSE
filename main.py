import asyncio
import uvicorn
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from fastapi.middleware.cors import CORSMiddleware

MESSAGE_STREAM_DELAY = 1  # second
MESSAGE_STREAM_RETRY_TIMEOUT = 1500  # milliseconds
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    # Allow all origins, you may want to restrict this in a production environment
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)


@app.get('/events')
async def message_stream(request: Request):
    def new_messages():
        # Implement your logic to check for new messages
        return True  # Placeholder for demonstration purposes

    async def event_generator():
        while True:
            # If the client has closed the connection
            if await request.is_disconnected():
                break

            # Checks for new messages and returns them to the client if any
            if new_messages():
                yield {
                    "event": "new_message",
                    "id": "message_id",
                    "retry": MESSAGE_STREAM_RETRY_TIMEOUT,
                    "data": "message_content"
                }

            await asyncio.sleep(MESSAGE_STREAM_DELAY)

    return EventSourceResponse(event_generator())

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
