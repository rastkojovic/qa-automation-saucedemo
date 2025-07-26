from pages.inventory_page import InventoryPage

def test_add_single_item_to_cart(driver, login_standard_user):
    """
    Test Case: TC004 - Add Single Item To Cart
    """
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    
    cart_count = inventory_page.get_cart_count()
    
    assert cart_count == "1", f"Expected cart count to be 1 but got {cart_count}"