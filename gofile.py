import requests

def uploadFile(file, token=None, folderId=None):
    
    server = requests.get("https://api.gofile.io/getServer").json()["data"]["server"]
    
    response = requests.post(
        url=f"https://{server}.gofile.io/uploadFile",
        data={
            "token": token,
            "folderId": folderId
        },
        files={"upload_file": open(file, "rb")}
    ).json()
    
    if response["status"] == "ok":
        data = response["data"]
        data["directLink"] = f"https://{server}.gofile.io/download/{data['fileId']}/{data['fileName']"
        return data
    elif "error-" in response["status"]:
        error = response["status"].split("-")[1]
        raise Exception(error)
