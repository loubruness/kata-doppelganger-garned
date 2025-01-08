from discount_applier import DiscountApplier
from user import User


def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    discount_applier = DiscountApplier(Notifier())
    doppelgangers = [User(name="Matthieu JACQUES", email="m@m.c"), User(name="Matthiehthhu JACQUES", email="mzdz@m.c"), User(name="Matthiehtddvdvdvdvdvhhu JACQUES", email="mzdvdvdz@m.c")]
    discount_applier.apply_v1(10, doppelgangers)
    assert discount_applier.notifier.counter == len(doppelgangers), "Not all users were notified"

def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    discount_applier = DiscountApplier(Notifier())
    doppelgangers = [User(name="Riri", email="m@m.c"), User(name="Lou", email="mzdz@m.c"), User(name="Alpha", email="mzdvdvdz@m.c")]
    discount_applier.apply_v2(10, doppelgangers)
    assert [x.name for x in doppelgangers] == discount_applier.notifier.user_sent, "Not all users were notified"

class Notifier:
    def __init__(self):
        self.counter = 0
        self.user_sent = []
        
    def notify(self, user, message):
        #Notify logique
        self.counter += 1
        self.user_sent.append(user.name)