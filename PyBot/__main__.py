import os
import aiohttp

from aiohttp import web

from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ Issue Greetings #############################################

@router.register("issues", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    """
    Whenever an issue is opened, greet the author and say thanks.
    """
    url = event.data['issue']['comments_url']
    author = event.data['issue']['user']['login']
    avatar = event.data['issue']['user']['avatar_url']

    message = f"<table><tbody><tr><td>Thanks for opening the issue @{author}! I will look into it ASAP!\n Till then show your love by staring my repos 😋.</td><td> <img alt='Coding' width='100px' height='100px' src='{avatar}'></td></tr></tbody></table>"
    await gh.post(url, data={
        'body': message,
        })



# @routes.post("/")
async def main(request):
    body = await request.read()

    secret = os.environ.get("GH_SECRET")
    oauth_token = os.environ.get("GH_AUTH")

    event = sansio.Event.from_http(request.headers, body, secret=secret)
    async with aiohttp.ClientSession() as session:
        gh = gh_aiohttp.GitHubAPI(session, "vasu-1",
                                  oauth_token=oauth_token)
        await router.dispatch(event, gh)
    return web.Response(status=200)



if __name__ == "__main__":
    app = web.Application()
    app.router.add_post("/", main)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)

    web.run_app(app, port=port)
