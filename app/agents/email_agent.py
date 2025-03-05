# app/agents/email_agent.py

from app.utils.email_service import send_email
from app.utils.otp_generator import generate_otp

class EmailAgent:
    def __init__(self):
        self.current_otp = None

    def send_otp(self, email):
        # Generate a 6-digit OTP and send it via email
        otp = generate_otp()
        self.current_otp = otp
        send_email(email, f"Your OTP code is: {otp}", "Historical AI - Email Verification")
        return otp

    def verify_otp(self, user_otp):
        # Check if the OTP entered by the user matches the generated OTP
        return user_otp.strip() == self.current_otp
