#coding=utf-8

def is_element_present(self, how, what):
    try: self.driver.find_element(by=how, value=what)
    except FileNotFoundError: return False
    return True

