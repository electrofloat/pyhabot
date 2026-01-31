import dotenv
import os
config = dotenv.dotenv_values(".env")


def main():
    TOKEN = os.getenv("TOKEN", "False") if config.get("TOKEN", "False") == "False" else config.get("TOKEN")
    if TOKEN == "False":
        print(f"Missing bot token.")
        return

    INTEGRATION = os.getenv("INTEGRATION", "Unkown") if config.get("INTEGRATION", "Unknown") == "Unknown" else config.get("INTEGRATION")
    if INTEGRATION == "discord":
        import classes.integrations.discord as DiscordIntegration
        DiscordIntegration.init(TOKEN)
        
    elif INTEGRATION == "telegram":
        import classes.integrations.telegram as TelegramIntegration
        TelegramIntegration.init(TOKEN)

    else:
        print("Expected valid Integration-type at command line argument 1, got " + str(INTEGRATION))

if __name__ == "__main__":
    main()
