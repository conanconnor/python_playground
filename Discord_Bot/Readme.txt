Discord bot setup guide:

1.  Go to: https://discord.com/developers/applications
2.  Click on 'New Application' in the top right.
3.  Name the bot and press 'Create'.
4.  On the left side panel click on 'Bot'.
5.  Click 'Add Bot' on the right (may already be added).
6.  Click 'Reset Token' you'll need to enter your password.
7.  Copy this token and put it somewhere safe (Do NOT share this).
8.  Scroll down and make sure 'Message Content Intent' is toggled on.
9.  On the left side panel click on 'OAuth2'.
10. Scroll down to 'OAuth2 URL Generator' and tick the box named 'bot'.
11. Scroll down again and tick the box named 'Send Messages' under test permissions.
12. A url should be generated at the bottome, copy this into your browser and add the bot to a server.
13. Now it's time to run the code. But before you do make sure your put your bot token in the space on
    line 24 of discord_bot.py
14. Once run, everytime you enter '$meme' the bot should send a meme. :)