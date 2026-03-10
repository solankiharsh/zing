"""
WSGI entrypoint for Vercel and other WSGI servers.
Exposes the Flask app so Vercel can detect and serve it.
"""
from run import app
