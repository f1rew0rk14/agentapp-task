import uvicorn


if __name__ == "__main__":
    service = "networks_connector.src.app:api"
    uvicorn.run(service, host="0.0.0.0", port=8888)
