from behave import given, then, when


@given('flaskr is set up')
def flaskr_is_setup(context):
    assert context.browser


@when('we hit the index')
def hit_the_index(context):
    context.browser.get('localhost:5000')


@then(u'the page title shows the text "{message}"')
def index_page_shown(context, message):
    assert message in context.browser.title
