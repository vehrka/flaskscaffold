from app import create_app

def before_feature(context, feature):
    oapp = create_app('testing')
    context.client = oapp.test_client()
