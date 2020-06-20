from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    # title_tag = context.browser.find_element(*HomePageLocators.TITLE) # * is used for unpacking tuple TITLE
    page = BasePage(context.driver)  # it's improved version of previous line of code
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])
