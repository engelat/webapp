import os
# Print the contents of the current directory
print("Contents of the current directory:", os.listdir('.'))
from app import create_app



app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="0.0.0.0", port=port)
