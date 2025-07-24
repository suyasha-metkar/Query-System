from fastapi import FastAPI, HTTPException                #mainframework, to return rror messages
from fastapi.middleware.cors import CORSMiddleware        #to allow frontend access
from pydantic import BaseModel                            #to validate data
from sqlalchemy import create_engine, text                #to connect to the database
from sqlalchemy.exc import SQLAlchemyError                #to handle database errors
import os                                                 #to handle file paths


Database_URL = os.getenv("DATABASE_URL", "sqlite:///./data/sample.db")               #database URL
if not Database_URL:
    raise ValueError("Database_URL is not set in system environment")
engine = create_engine(Database_URL, connect_args={"check_same_thread": False})      #connecting to the database

app = FastAPI()                                            # Created FastAPI app instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                   # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],                   # Allow all methods
    allow_headers=["*"],                   # Allow all headers
)

class Query(BaseModel):       # Pydantic model for the data
    query: str                # Query string to search in the database other input is rejected

@app.get("/")                   # Root endpoint for health checkup
def root():                     
    return {"message": "Query System is good to go!"}

@app.post("/get_query")            # Endpoint to handle queries
def get_query(request: Query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(request.query))     # Execute the query
            data = [dict(row._mapping) for row in result]
        return {"status": "Query ran successfully", "data": data}
    except ZeroDivisionError:                                    #Handling errors
        raise HTTPException(status_code=422, detail="Division by zero is not allowed.")
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="Ohho! Bad request!Please check your SQL syntax or table/column names.")
    except Exception:
        raise HTTPException(status_code=500, detail="Invalid query or server error")
