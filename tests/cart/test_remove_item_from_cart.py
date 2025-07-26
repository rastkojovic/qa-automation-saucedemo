from pages.inventory_page import InventoryPage

def test_remove_item_from_cart(driver, login_standard_user):
    """
    Test Case: TC005 - Remove Item From Cart
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "0", f"Expected cart count to be 0 but got {cart_count}"