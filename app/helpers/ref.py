from app.mod_home.models import Ref
from app import db


# ?ref se koristi za praćenje affilate linkova koji se koriste za reklamiranje servisa
def check(request):
    arg = request.args.get('ref')

    if arg:
        ref = Ref.query.filter_by(ref_uri=arg).first()

        if ref:
            ref.status = 1
        else:
            ref = Ref(ref_uri=arg, status=1)
            db.session.add(ref)

        db.session.commit()



