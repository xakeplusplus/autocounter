<h1>AutoCounter</h1>
change the variables for discord channel id, discord token and other guy's username.

<h2>Fix for crash</h2>
discord doesn't allow self-botting so u have to modify gateway.py in discord.py library for it to work.

change line 466 and 467 in gateway.py to this:
``
if state._intents is not None:
            payload['d']['intents'] = state._intents.value``