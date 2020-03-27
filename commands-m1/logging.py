@client.event
async def on_member_update(before, after):
    logs = client.get_channel("686880410139099148")
    if  before.display_name != after.display_name:
          await logs.send(f"Nickname of {before.name} changed from {before.display_name} to {after.display_name}")

    if before.activity != after.activity:
          await logs.send(f"{after.name}'s activity changed from {before.activity} to {after.activity}")

    if before.avatar_url != after.avatar_url:
          await logs.send(f"{after.name}'s avatar has changed from {before.avatar_url} to {after.avatar_url}")