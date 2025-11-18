import pywhatkit as wk
import time
from dotenv import load_dotenv
import os

load_dotenv()

# WhatsApp group ID (get via wk.chat.get_group_id())
GROUP_ID = os.getenv("GROUP_ID")  

def block_links():
    while True:
        try:
            # Fetch latest messages (simplified demo)
            last_message = wk.chat.get_messages(GROUP_ID, count=1)[0]
            if 'http://' in last_message or 'www.' in last_message:
                wk.sendwhatmsg_to_group_instantly(
                    group_id=GROUP_ID,
                    message="⚠️ Link deleted!",
                    tab_close=True
                )
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    block_links()
