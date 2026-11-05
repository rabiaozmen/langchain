from dotenv import load_dotenv
import os

load_dotenv()

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    print(api_key is not None)

if __name__ == "__main__":
    main()