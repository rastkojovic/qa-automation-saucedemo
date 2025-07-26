from pages.inventory_page import InventoryPage

def test_cart_icon_updates(driver, login_standard_user):
    """
    Test Case: TC006 - Cart Icon Updates
    """
    
    inventory_page = InventoryPage(driver)
    
    # Add two items to cart
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    
    # Remove one item form cart
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "1", f"Expected cart count to be 1 but got {cart_count}"