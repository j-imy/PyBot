from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()


@router.register("pull_request", action="opened")
async def opened_pr(event, gh, *arg, **kwargs):
    """Mark new PRs as needing a review."""
    pull_reques = event.data["pull_request"]["labels"]
    author = event.data['pull_request']['user']['login']

    ur = event.data['pull_request']['comments_url']


    messag = f"<table><tbody><tr><td>Thanks for opening the pull request @{author}! I will look into it ASAP!\n Till then you can improve your code & you can show your love by staring my repos 😋.</td></tr></tbody></table>"
    await gh.post(ur, data={
        'body': messag,
        })
    await gh.post(pull_reques, data=["review_needed"])




    # f'{event.data["pull_request"]["issue_url"]}/labels',
    #         data=["invalid"]

            