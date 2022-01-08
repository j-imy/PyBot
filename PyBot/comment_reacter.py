from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ issue comment reactor #############################################
# https://stackoverflow.com/questions/64112300/how-can-i-get-the-list-of-github-webhook-events



@router.register("issue_comment", action="created")
async def issue__comment_create_event(event, gh, *args, **kwargs):
    url = event.datva['issue_comment']['comment']['reactions']


    message = 1
    await gh.post(url, data={
        '+1': message,
        })