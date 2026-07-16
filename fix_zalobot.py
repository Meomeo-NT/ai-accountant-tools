with open('/root/zalobot/main.py', 'r') as f:
    content = f.read()

if 'import json' not in content:
    content = content.replace('import uvicorn', 'import json\nimport datetime\nimport uvicorn')

if 'def notify_handler' not in content:
    notify_code = '''
# ============ NOTIFICATION ENDPOINTS ============
@app.post("/notify")
async def notify_handler(request: dict):
    message = request.get("message", "Notification")
    print(f"[NOTIFY] {message}")
    return {"status": "ok", "received": message}

@app.get("/notifications")
async def get_notifications():
    try:
        with open("/root/bds-crawler/data/notifications.json") as f:
            history = json.load(f)
        return {"count": len(history), "history": history[-10:]}
    except:
        return {"count": 0, "history": []}

'''
    content = content.replace('uvicorn.run', notify_code + 'uvicorn.run')

with open('/root/zalobot/main.py', 'w') as f:
    f.write(content)

print('FIXED_ZALOBOT')