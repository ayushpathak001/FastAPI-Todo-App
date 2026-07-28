from fastapi import FastAPI , Body , Path , Query ,HTTPException
from Todo_model import Todo
from todo_request import Todo_Request


app = FastAPI(
    title="Loopkaka FastAPI tutorial..",
    version="1.1.1" , 
    description="This is chapter 2 Project_2"
)



TODOS = [
    Todo(1 , "Task 1" , "My Task" , False , 1),
    Todo(2 , "Task 1" , "My Task" , False , 2),
    Todo(3 , "Task 1" , "My Task" , False , 1),
    Todo(4 , "Task 1" , "My Task" , False , 3),
    Todo(5 , "Task 1" , "My Task" , False , 1)
    
]

@app.get("/todos/all")
def get_all_todos():
    if len(TODOS) ==0:
        return {
            "msg" : "Your Todo is empty.." , 
            "Todo" : TODOS
        }

    return {
        "Msg" : "Todo Found...", 
        "Todo" : TODOS
    }


@app.post("/create/todo")
def create_todo(todo : Todo_Request):
    t = Todo(**todo.dict())
    TODOS.append(get_todo_id(t))
    return t


@app.put("/update/todo")
async def update_todo(todo : Todo_Request):
    t = Todo(**todo.dict())
    for index in range(len(TODOS)):
        if TODOS[index].id == t.id:
            TODOS[index] = t
            
            return {
                "msg" : "Your todo got updated...." , 
                "Todo" : t
            }
    
    raise HTTPException(
        status_code=400 , detail="ID not found.."
        )


@app.delete("/delete/todo{id}")
async def delete_todo(id : int = Path(ge=1 , le=(len(TODOS)))):
    for index in range(len(TODOS)):
        if TODOS[index].id == id:
            del_data = TODOS.pop(index)
            return {
                "msg" : "Your todo got deleted successfully..." , 
                "Deleted data" : del_data
            }
    return {
        "msg" : "Your todo not found....."
    }



@app.get("/get_by_id/todo{id}")
async def get_by_id(id : int = Path(ge=1 , le=(len(TODOS)))):
    for index in range(len(TODOS)):
        if TODOS[index].id == id:
            return {
                "msg" : "Your todo found..." , 
                "Todo" : TODOS[index]
            }
    return {
        "msg" : "your todo not found......"
    }


 


def get_todo_id(todo):
    if len(TODOS) ==1:
        todo.id = 1
    else:
        todo.id = TODOS[-1].id+1

    return todo



