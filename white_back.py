from fastapi import FastAPI

app = FastAPI()

position = True

@app.get("/")
def rere(test):
    print("adsa",test)
    return "{True}"

# @app.get("/status")
# async def rere():
#     global position
#     position = not position
#     print("New state",position)
#     return {"New state":position}