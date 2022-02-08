import pytest

from member_account import MemberAccount

def test_valid_path_1 ():
    member_1= MemberAccount ()
    member_1.register()
    member_1.confirm()
    member_1.cancel()
    assert member_1.get_state() == MemberAccount.END

def test_valid_path_2 ():
    member_1= MemberAccount ()
    member_1.register()
    member_1.confirm()
    member_1.change()
    assert member_1.get_state() == MemberAccount.ACTIVE

def test_valid_path_3 ():
    member_1= MemberAccount ()
    member_1.register()
    member_1.confirm()
    member_1.fee_due()
    member_1.transfer()
    assert member_1.get_state() == MemberAccount.ACTIVE

def test_valid_path_4 ():
    member_1= MemberAccount ()
    member_1.register()
    member_1.confirm()
    member_1.suspend()
    member_1.reactivate()
    assert member_1.get_state() == MemberAccount.ACTIVE


def test_valid_path_5 ():
    member_1= MemberAccount ()
    member_1.register()
    with pytest.raises(RuntimeError):
        member_1.cancel()