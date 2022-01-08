from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()

############################ pull request review_needed_pr labeler #############################################


LABEL1 = 'review_needed_pr' # label name

@router.register("pull_request", action="opened")
async def issue_opened_event(event, gh, *args, **kwargs):
    label = event.data['pull_request']['labels']

    await gh.post(label, data=[LABEL1]) #event post for key label