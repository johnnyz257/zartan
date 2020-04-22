import logging

# import functions
from flask import render_template, session
from flask import Blueprint
from utils.udp import SESSION_INSTANCE_SETTINGS_KEY

from GlobalBehaviorandComponents.validation import is_authenticated, get_userinfo

logger = logging.getLogger(__name__)

# set blueprint
hospitality_views_bp = Blueprint('hospitality_views_bp', __name__, template_folder='templates', static_folder='static', static_url_path='static')


# Required for Login Landing Page
@hospitality_views_bp.route("/profile")
@is_authenticated
def hospitality_profile():
    logger.debug("hospitality_profile()")
    return render_template("hospitality/profile.html", user_info=get_userinfo(), config=session[SESSION_INSTANCE_SETTINGS_KEY])
