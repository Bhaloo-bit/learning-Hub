from fastapi import FastAPI, HTTPException

app = FastAPI(description="Todo app")

todo = []
@app.get('/')
def home():
    return {'message':"todo app"}

@app.post("/user")
def create(task:str):
    todo.append(task)
    return {'message':f'task added {task}'}

@app.get("/user")
def display_task(todo):
    return {"all task": todo}

@app.delete("/user/{i}")
def remove_task(i : int):
    try:
        removed = todo.pop(i)
        return {"message": f'removed task {removed}'}
    except IndexError:
        raise HTTPException(status_code=404, detail="Out of index")


        