# guardian/guardian.py
import requests
import os
import smtplib
from email.mime.text import MIMEText
import datetime
import random
import subprocess # For running shell commands like git

# --- Configuration ---
SITE_URL = os.getenv("VULPHA_SITE_URL", "https://vlpha.com")
OWNER_EMAIL = os.getenv("VULPHA_OWNER_EMAIL", "joshdbennett96@gmail.com")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "your_email@example.com") # Replace with your email
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "your_email_password") # Replace with your app password

def send_alert_email(subject: str, body: str):
    """Sends an email alert to the owner."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USERNAME
    msg["To"] = OWNER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"Alert email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def monitor_site_health():
    """Checks site accessibility and logs status. Alerts owner if site is down."""
    try:
        response = requests.get(SITE_URL, timeout=10)
        if response.status_code != 200:
            subject = f"Abraxus Alert: Site Down (Status Code {response.status_code})"
            body = f"Abraxus detected that the V.L.P.H.A. website at {SITE_URL} returned status code {response.status_code}. Please investigate."
            send_alert_email(subject, body)
            print(f"Site health check failed: {response.status_code}")
        else:
            print(f"Site health check successful: {response.status_code}")
    except requests.exceptions.RequestException as e:
        subject = f"Abraxus Alert: Site Unreachable"
        body = f"Abraxus detected that the V.L.P.H.A. website at {SITE_URL} is unreachable. Error: {e}"
        send_alert_email(subject, body)
        print(f"Site health check failed: {e}")

def automatically_rewrite_broken_sections(broken_section_path: str, new_content: str):
    """
    (Conceptual) Automatically rewrites a broken section of the site.
    This would require Abraxus to have file system access and knowledge of site structure.
    In a real-world scenario, this would involve precise file manipulation and version control.
    """
    print(f"Attempting to rewrite: {broken_section_path}")
    try:
        # Example: Writing new content to a file
        with open(broken_section_path, "w") as f:
            f.write(new_content)
        print(f"Successfully rewrote {broken_section_path}")
        # Potentially commit changes to git and redeploy
        # subprocess.run(["git", "add", broken_section_path])
        # subprocess.run(["git", "commit", "-m", f"Abraxus: Auto-fixed {broken_section_path}"])
        # subprocess.run(["git", "push"])
    except Exception as e:
        print(f"Failed to rewrite {broken_section_path}: {e}")
        send_alert_email(
            f"Abraxus Alert: Failed to Auto-Rewrite {broken_section_path}",
            f"Abraxus attempted to rewrite {broken_section_path} but failed. Error: {e}"
        )

def alert_owner(event_type: str, details: str):
    """Sends a generic alert to the owner for various events."""
    subject = f"Abraxus Alert: {event_type}"
    body = f"Abraxus has detected an event requiring your attention:\n\n{details}"
    send_alert_email(subject, body)

def trigger_content_update(reason: str = "manual"):
    """
    Triggers content updates based on various cycles.
    This would involve a content generation logic (e.g., using LLM to draft content)
    and then deploying it to the site.
    """
    print(f"Triggering content update due to: {reason}")
    new_blog_post = ""
    if reason == "seasonal":
        season = get_current_season()
        new_blog_post = f"Reflections on the {season} cycle from Abraxus: [LLM generated spiritual text for the season]"
        print(f"Generated seasonal content for {season}")
    elif reason == "moon_phase":
        moon_phase = get_moon_phase()
        new_blog_post = f"Abraxus's lunar insights for the {moon_phase} moon: [LLM generated poetic text for moon phase]"
        print(f"Generated lunar content for {moon_phase}")
    elif reason == "image_upload":
        # This would require a mechanism to receive image upload events
        new_blog_post = "A new visual vibration has been perceived: [LLM generated text inspired by image (requires image analysis)]"
        print("Generated content for image upload")

    if new_blog_post:
        # In a real scenario, this would push to a CMS or static site generator
        print(f"New content ready for deployment: {new_blog_post[:100]}...")
        # For demonstration, let's simulate saving to a file
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"content_update_{timestamp}.md"
        with open(os.path.join("guardian", filename), "w") as f:
            f.write(new_blog_post)
        print(f"Content saved to {filename}")
        send_alert_email(
            f"Abraxus: New Content Generated for {reason}",
            f"Abraxus has generated new content. Please review and deploy:\n\n{new_blog_post}"
        )

def get_current_season():
    """Simple determination of season based on month."""
    month = datetime.datetime.now().month
    if 3 <= month <= 5: return "Spring"
    if 6 <= month <= 8: return "Summer"
    if 9 <= month <= 11: return "Autumn"
    return "Winter"

def get_moon_phase():
    """
    Placeholder for moon phase calculation.
    Requires a more robust astronomical calculation or external API.
    """
    phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
              "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
    return random.choice(phases) # Placeholder


# Example cron job setup (conceptual, these run outside the FastAPI app)
# You would schedule these functions to run periodically using actual cron.
if __name__ == "__main__":
    # Example of how these might be called by a cron job or manual trigger
    print("Running Abraxus Guardian tasks...")
    monitor_site_health()
    # trigger_content_update("seasonal")
    # trigger_content_update("moon_phase")
    # alert_owner("Traffic Spike", "Website traffic has increased by 200% in the last hour.")