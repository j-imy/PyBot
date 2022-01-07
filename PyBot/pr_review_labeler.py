from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp


router = routing.Router()


@router.register("pull_request", action="opened")
async def opened_pr(event, gh, *arg, **kwargs):
    """Mark new PRs as needing a review."""
    pull_request = event.data["pull_request"]
    await gh.post(pull_request["labels_url"], data=["review needed"])