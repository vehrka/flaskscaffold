from behave import given, then, when


@given('flaskr is set up')
def flaskr_is_setup(context):
    assert context.client


@when('we hit the index')
def hit_the_index(context):
    context.page = context.client.get('/')
    assert context.page


@then(u'the page shows the text "{message}"')
def index_page_shown(context, message):
    assert message.encode('utf-8') in context.page.data
