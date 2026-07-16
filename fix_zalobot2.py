with open('/root/zalobot/main.py', 'r') as f:
    content = f.read()

# Fix: wrap uvicorn.run inside if __name__ block
old = '''uvicorn.run(app, host="0.0.0.0", port=8081)


if __name__ == "__main__":

    main()'''

new = '''if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)'''

if 'uvicorn.run(app, host="0.0.0.0", port=8081)' in content and 'if __name__ == "__main__":' in content:
    content = content.replace(old, new)
    with open('/root/zalobot/main.py', 'w') as f:
        f.write(content)
    print('FIXED UVICORN RUN')
else:
    # Try alternative
    old2 = 'uvicorn.run(app, host="0.0.0.0", port=8081)'
    content = content.replace(old2, '')
    # Ensure if __name__ block exists with uvicorn
    if 'if __name__' in content:
        content = content.replace('    main()', '    uvicorn.run(app, host="0.0.0.0", port=8081)\n    main()')
    else:
        content += '\n\nif __name__ == "__main__":\n    uvicorn.run(app, host="0.0.0.0", port=8081)\n'
    with open('/root/zalobot/main.py', 'w') as f:
        f.write(content)
    print('FIXED ALT')