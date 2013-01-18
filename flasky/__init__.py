from flask import Flask, url_for, render_template
app = Flask(__name__)

import flasky.views
import os