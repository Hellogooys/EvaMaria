class script(object):
    START_TXT = """<b>𝙷𝙴𝙻𝙻𝙾 𝙼𝚈 𝙵𝚁𝙸𝙴𝙽𝙳 {}
𝙼𝚈 𝙽𝙰𝙼𝙴 『<a href=https://t.me/CL_FILTER_BOT>𝚃𝙷𝙾𝙼𝙰𝚂 𝚂𝙷𝙴𝙻𝙱𝚈</a>』 ,𝙸𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 , 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁 😌</b>"""
      
    OWNER_TXT = """<b>🔰 𝙷𝙴𝚈 𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 🔰</b>"""
    
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    
    ABOUT_TXT = """<b>⌬ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
⌬ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/NL_MP4>𝙽𝙸𝙷𝙰𝙰𝙻</a>
⌬ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
⌬ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
⌬ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
⌬ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
⌬ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.2 [ 𝙱𝙴𝚃𝙰 ]</b>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and 𝚃𝙷𝙾𝙼𝙰𝚂 𝚂𝙷𝙴𝙻𝙱𝚈 will respond whenever a keyword is found the message

<b>NOTE:</b>
1. 𝚃𝙷𝙾𝙼𝙰𝚂 𝚂𝙷𝙴𝙻𝙱𝚈 should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. 𝚃𝙷𝙾𝙼𝙰𝚂 𝚂𝙷𝙴𝙻𝙱𝚈 supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
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
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
𝑻𝑯𝑬𝑺𝑬 𝑨𝑹𝑬 𝑻𝑯𝑬 𝑬𝑿𝑻𝑹𝑨 𝑭𝑬𝑨𝑼𝑻𝑼𝑹𝑬 𝑶𝑭 𝑻𝑯𝑶𝑴𝑨𝑺 𝑺𝑯𝑬𝑳𝑩𝒀 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    
    ADMIN_TXT = """Help: <b>ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴛs</b>

<b>NOTE:</b>

⚙️ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴛs ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴀᴅᴍɪɴ ⚙️

⚙️ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ

» /delete - Reply Files

» /deleteall - Delete All Files

» /total - How Many Files Saved

» /channel - Add Channel List

⚙️ ᴍᴀɴᴜᴀʟ ғɪʟᴛᴇʀ

» /add - add a new filter

» /filters - see your filters

» /connect - connect a chat

» /delfilter - delete a filter

» /delall_filters - delete all filters from chat

» /disconnect - disconnect a chat 

» /connections - see current connections
"""
    ADMIN_TXT2 = """⚙️ ᴄᴏᴍᴍᴏɴ ᴄᴏᴍᴍᴀɴᴅs

» /broadcast - Reply Any Media Or Message

» /logger - Get Bot Logs 

» /start - check alive

» /help - see helps 

» /about- see about

⚙️ ɢʀᴏᴜᴘ ᴄᴏᴍᴍᴀɴᴅs

» /ban-ban user from group

» /tban - time set ban

» /unban - unban user from group

» /mute - Mute user from group

» /tmute - time set mute

» /unmute - unmute user from group

» /pin - pin message in group 

» /unpin - unpin message in group

» /purge - delete all messages in group"""
    
    STATUS_TXT = """<b>⌬ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
⌬ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
⌬ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⌬ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
⌬ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼  {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼  {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
