from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def get_ip_and_redirect():
    # Get the client's IP address
    client_ip = request.remote_addr
    print(f"Client IP: {client_ip}")

    # Log the IP address to a file
    with open('ip_log.txt', 'a') as f:
        f.write(f"{client_ip}\n")

    # Redirect to YouTube
    return redirect("https://www.youtube.com")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
