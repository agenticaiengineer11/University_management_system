from app.menu import main

if __name__ == "__main__":
    main()


from config.logging_config import setup_logging
from app.menu import main


setup_logging()
main()