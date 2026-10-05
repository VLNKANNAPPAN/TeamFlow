from fastapi import FastAPI

# FastAPI creates the application instance
app = FastAPI(title="TeamFlow API", version="0.1.0")


# we are registering a get endpoint and health_check executes when we get an request
# at this endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
