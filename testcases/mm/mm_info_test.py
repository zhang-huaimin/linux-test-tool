


def get_mm_info_test(dev):
    status, data = dev.con.ask("free; echo result:$?", "result:0", 2)
    assert status == True