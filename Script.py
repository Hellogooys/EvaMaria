class script(object):
    START_TXT = """<b>π·π΄π»π»πΎ πΌπ π΅ππΈπ΄π½π³ {}
πΌπ π½π°πΌπ΄ γ<a href=https://t.me/CL_FILTER_BOT>ππ·πΎπΌπ°π ππ·π΄π»π±π</a>γ ,πΈπ²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π , πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ ππ΄π΄ πΌπ πΏπΎππ΄π π</b>"""
      
    OWNER_TXT = """<b>π° π·π΄π π·π΄ππ΄ ππΎπ π²π°π½ π²πΎπ½ππ°π²π πΌπ πΎππ½π΄π π°</b>"""
    
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    
    ABOUT_TXT = """<b>β¬ πΌπ π½π°πΌπ΄: {}
β¬ π²ππ΄π°ππΎπ: <a href=https://t.me/NL_MP4>π½πΈπ·π°π°π»</a>
β¬ π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β¬ π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β¬ π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β¬ π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β¬ π±ππΈπ»π³ πππ°πππ: v1.0.2 [ π±π΄ππ° ]</b>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ππ·πΎπΌπ°π ππ·π΄π»π±π will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ππ·πΎπΌπ°π ππ·π΄π»π±π should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ππ·πΎπΌπ°π ππ·π΄π»π±π supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    FILLINGS_TXT = """Help: <b>Fillings</b>
You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the filter message, or mention them in a filter!
<b>Supported fillings:</b>
- <code>{first}</code>: The user's first name.
- <code>{last}</code>: The user's last name.
- <code{username}</code>: The user's username.
- <code>{mention}</code>: Mentions the user with their firstname.
- <code>{id}</code>: The user's ID.
- <code>{dcid}</code>: The user's DC ID.
- <code>{chatname}</code>: The chat's name.
- <code>{query}</code>: Any Replied Message.
<b>Example:</b>
<b>- Save a filter using the mention.</b>
-> <code>/filter test Hello {mention} This Is your Username : {username} And This Is your ID : {id}.</code>
"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    AUTO_MANUAL_TXT = """Help: <b>Filters</b>
<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>
Paste some texts or documents on a website!
<b>Commands and Usage:</b>
β’ /paste [text] - paste the given text on Pasty
β’ /paste [reply] - paste the replied text on Pasty
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>
Do as you wish with telegra.ph module!
<b>Commands and Usage:</b>
β’ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
β’ /id - get id of a specified user.
β’ /info  - get information about a user.
β’ /json - get the json details of a message.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TORRENT_TXT = """Help: <b>Torrent Search</b>
<b>Commands and Usage:</b>
β’ /torrent or /tor <movie name>: Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>
Translate texts to a specific language!
<b>Commands and Usage:</b>
β’ /tr [language code][reply] - translate replied message to specific language.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>
Search many things without leaving telegram!
<b>Commands and Usage:</b>
β’ /imdb  - get the film information from IMDb source.
β’ /search  - get the film information from various sources.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ More search tools can be found on inline.
β’ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>
Need to delete lots of messages? That's what purges are for!
<b>Commands and Usage:</b>
β’ /purge - delete all messages from the replied to message, to the current message.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>
Some people need to be publicly banned; spammers, annoyances, or just trolls.
This module allows you to do that easily, by exposing some common actions, so everyone will see!
<b>Commands and Usage:</b>
β’ /ban - ban a user.
β’ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /mute - mute a user.
β’ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /unban or /unmute - unmute a user & unban a user.
<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>
All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!
<b>Commands and Usage:</b>
β’ /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
β’ /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works only group.
β’ These commands can be used by Only admin."""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
π»π―π¬πΊπ¬ π¨πΉπ¬ π»π―π¬ π¬πΏπ»πΉπ¨ π­π¬π¨πΌπ»πΌπΉπ¬ πΆπ­ π»π―πΆπ΄π¨πΊ πΊπ―π¬π³π©π 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    
    ADMIN_TXT = """Help: <b>α΄α΄α΄ΙͺΙ΄ α΄α΄α΄α΄α΄Ι΄α΄s</b>

<b>NOTE:</b>

βοΈ α΄ΚΙͺs α΄α΄α΄α΄α΄Ι΄α΄s α΄Ι΄ΚΚ α΄‘α΄Κα΄ ?α΄Κ α΄α΄α΄ΙͺΙ΄ βοΈ

βοΈ α΄α΄α΄α΄ ?ΙͺΚα΄α΄Κ

Β» /delete - Reply Files

Β» /deleteall - Delete All Files

Β» /total - How Many Files Saved

Β» /channel - Add Channel List

βοΈ α΄α΄Ι΄α΄α΄Κ ?ΙͺΚα΄α΄Κ

Β» /add - add a new filter

Β» /filters - see your filters

Β» /connect - connect a chat

Β» /delfilter - delete a filter

Β» /delall_filters - delete all filters from chat

Β» /disconnect - disconnect a chat 

Β» /connections - see current connections
"""
    ADMIN_TXT2 = """βοΈ α΄α΄α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄Ι΄α΄s

Β» /broadcast - Reply Any Media Or Message

Β» /logger - Get Bot Logs 

Β» /start - check alive

Β» /help - see helps 

Β» /about- see about

βοΈ Ι’Κα΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄s

Β» /ban-ban user from group

Β» /tban - time set ban

Β» /unban - unban user from group

Β» /mute - Mute user from group

Β» /tmute - time set mute

Β» /unmute - unmute user from group

Β» /pin - pin message in group 

Β» /unpin - unpin message in group

Β» /purge - delete all messages in group"""
    
    STATUS_TXT = """<b>β¬ ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β¬ ππΎππ°π» πππ΄ππ: <code>{}</code>
β¬ ππΎππ°π» π²π·π°ππ: <code>{}</code>
β¬ πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β¬ π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±</b>"""
    MEMES_TXT = """Help: <b>Memes</b>
Some dank memes for fun or whatever!
<b>Commands and Usage:</b>
β’ /throw or /dart - tπ mπΊππΎ drat 
β’ /roll or /dice - roll the dice 
β’ /goal or /shoot - to make a goal or shoot
β’ /luck or /cownd - Spin the Lucky
β’ /runs strings
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>
Some URLs is Shortner
<b>Commands and Usage:</b>
β’ /short <code>(link)</code> - I will send the shorted links.
<b>Example:</b>
<code>/short https://t.me/josprojects</code>
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>
A module to convert text to voice with language support.
<b>Commands and Usage:</b>
β’ /tts - Reply to any text message with language code to convert as audio.
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>
Music download modules, for those who love music.
<b>Commands and Usage:</b>
β’ /song or /mp3 (songname) - download song from yt servers.
β’ /video or /mp4 (songname) - download video from yt servers.
<b>YouTube Thumbnail Download</b>
β’ /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>
There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.
<b>Commands and Usage:</b>
β’ /genpassword or /genpw <code>20</code>
<b>NOTE:</b>
β’ Only Digits Are Allowed
β’ Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    SHARE_TXT = """Help: <b>Sharing Text Maker</b>
a bot to create a link to share text in the telegram.
<b>Commands and Usage:</b>
β’ /share (text or reply to message)
<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    LOG_TEXT_G = """#πππ°ππ«π¨π?π©
    
<b>αβΊ ππ«π¨π?π© βͺΌ  {}(<code>{}</code>)</b>
<b>αβΊ ππ¨π­ππ₯ πππ¦πππ«π¬ βͺΌ <code>{}</code></b>
<b>αβΊ πππππ ππ² βͺΌ  {}</b>
"""
    LOG_TEXT_P = """#πππ°ππ¬ππ«
    
<b>αβΊ ππ - <code>{}</code></b>
<b>αβΊ πππ¦π - {}</b>
"""
