with open('/root/zalobot/main.py', 'r') as f:
    content = f.read()

old_end = '''uvicorn.run(app, host="0.0.0.0", port=8081)


if __name__ == "__main__":

    main()'''

new_end = '''if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)'''

if old_end in content:
    content = content.replace(old_end, new_end)
    with open('/root/zalobot/main.py', 'w') as f:
        f.write(content)
    print('FIXED_OK')
else:
    print('PATTERN_NOT_FOUND')
    # Show what's at the end
    print('TAIL:')
    print(content[-200:])