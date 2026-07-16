with open('/root/zalobot/main.py', 'r') as f:
    content = f.read()

# Remove standalone uvicorn.run line and fix the if block
import re

# Pattern: uvicorn.run(...) followed by if __name__ block
pattern = r'uvicorn\.run\(app, host="0\.0\.0\.0", port=8081\)\s*if __name__ == "__main__":\s*main\(\)'
new = 'if __name__ == "__main__":\n    uvicorn.run(app, host="0.0.0.0", port=8081)'

if re.search(pattern, content):
    content = re.sub(pattern, new, content)
    with open('/root/zalobot/main.py', 'w') as f:
        f.write(content)
    print('FIXED_REGEX')
else:
    # Fallback: just remove the standalone uvicorn.run line
    content = content.replace('uvicorn.run(app, host="0.0.0.0", port=8081)\n\n\nif __name__ == "__main__":\n\n    main()\n', 'if __name__ == "__main__":\n    uvicorn.run(app, host="0.0.0.0", port=8081)\n')
    with open('/root/zalobot/main.py', 'w') as f:
        f.write(content)
    print('FIXED_MANUAL')