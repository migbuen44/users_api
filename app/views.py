from app import app

@app.route('/')
def root():
  return "root"