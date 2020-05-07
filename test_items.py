import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_be_add_to_cart_button(browser):
    browser.get(link)
    cart_button=browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert cart_button, "No add to cart button"