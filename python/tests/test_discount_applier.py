from discount_applier import DiscountApplier
from user import User


def test_apply_v1():
    # TODO: write a test that fails due to the bug in
    discount_applier = DiscountApplier(Notifier())
    doppelgangers = [User(name="Matthieu JACQUES", email="m@m.c"), User(name="Matthiehthhu JACQUES", email="mzdz@m.c"), User(name="Matthiehtddvdvdvdvdvhhu JACQUES", email="mzdvdvdz@m.c")]
    discount_applier.apply_v1(10, doppelgangers)
    condition = discount_applier.notifier.counter = 3
    assert condition == len(doppelgangers)

def test_apply_v2():
    # TODO: write a test that fails due to the bug in
    discount_applier = DiscountApplier(Notifier())
    doppelgangers = [User(name="Lou", email="m@m.c"), User(name="Lou", email="mzdz@m.c"), User(name="Lou", email="mzdvdvdz@m.c")]
    discount_applier.apply_v2(10, doppelgangers)
    assert False not in [discount_applier.notifier.sent_messages[user.name] for user in doppelgangers]

class Notifier:
    def __init__(self):
        self.counter = 0
        self.sent_messages = {}
        
    def notify(self, user, message):
        #Notify logique
        self.counter += 1
        self.sent_messages[user.name] = True
