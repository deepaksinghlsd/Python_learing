import uvicorn
if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",  # <folder_name>.<file_name>:<fastapi_variable>
        host="127.0.0.1",
        port=8500,
        reload=True,
    )
