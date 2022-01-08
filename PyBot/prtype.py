"""Label a pull request based on its type."""
from gidgethub import routing, sansio
from gidgethub import aiohttp as gh_aiohttp
import pathlib

from . import util

router = routing.Router()
@router.register("pull_request", action="opened")



async def add_category(gh, issue, category):
    """Apply this type label if there aren't any type labels on the PR."""
    if any(label.startswith("type") for label in util.labels(issue)):
        return
    await gh.post(issue["labels_url"], data=[category])


async def classify_by_filepaths(gh, pull_request, filenames):
    """Categorize the pull request based on the files it has modified.

    If any paths are found which do not fall within a specific classification,
    then no new label is applied.

    The routing is handled by the filepaths module.
    """
    issue = await util.issue_for_PR(gh, pull_request)
    docs = tests = False
    for filename in filenames:
        if util.is_news_dir(filename):
            continue
        filepath = pathlib.PurePath(filename)
        if filepath.suffix == '.rst' or filepath.suffix == '.md':
            docs = True
        elif filepath.name.startswith('test_'):
            tests = True
        else:
            return
    if tests:
        await add_category(gh, issue, 'tests')
    elif docs:
        await add_category(gh, issue, 'documentation')
    return
