from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

LABEL_PREFIX = 'type '
LABEL = LABEL_PREFIX + 'documentation'


@router.register("pull_request", action="opened")
async def opened_pr(event, gh, *arg, **kwargs):
    """Mark new PRs as needing a review."""
    

    # pull_reques = event.data["labels_url"]
    # pull_reques1 = event.data["pull_request"]["labels_url"]
    # pull_reques4 = event.data["pull_request"]["labels"]
    # pull_reques2 = event.data["pull_request"]["head"]["repo"]["labels_url"]
    # pull_reques3 = event.data["pull_request"]["base"]["repo"]["labels_url"]

    author = event.data['pull_request']['user']['login']

    ur = event.data['pull_request']['comments_url']
    # labe = 'review_needed'

    messag = f"<table><tbody><tr><td>Thanks for opening the pull request @{author}! I will look into it ASAP!\n Till then you can improve your code & you can show your love by staring my repos 😋.</td></tr></tbody></table>"
    await gh.post(ur, data={
        'body': messag,
        })

    # messag1 = f"labels_url {pull_reques}"
    # await gh.post(ur, data={
    #     'body': messag1,
    #     })

    # messag33 = f"pull_requests - labels_url {pull_reques1}"
    # await gh.post(ur, data={
    #     'body': messag33,
    #     })


    # messag2 = f"[pull_request][head][repo][labels_url] {pull_reques2}"
    # await gh.post(ur, data={
    #     'body': messag2,
    #     })

    # messag3 = f"[pull_request][base][repo][labels_url] {pull_reques3}"
    # await gh.post(ur, data={
    #     'body': messag3,
    #     })

    # messag4 = f"[pull_request][labels] {pull_reques4}"
    # await gh.post(ur, data={
    #     'body': messag4,
    #     })

    # messag5 = f"[pull_request][comments url] {ur}"
    # await gh.post(ur, data={
    #     'body': messag5,
    #     })




    # await gh.post(pull_reques2, data=[LABEL])
    # await gh.post(pull_reques3, data=[LABEL])
    # await gh.post(pull_reques4, data=[LABEL])



    # f'{event.data["pull_request"]["issue_url"]}/labels',
    #         data=["invalid"]

            