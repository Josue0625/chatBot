from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app

home_bp = Blueprint("home_bp", __name__, template_folder="templates", static_folder="static")

@home_bp.route('/')
def home():
    return render_template("home.html")