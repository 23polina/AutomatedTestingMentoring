*** Variables ***
# Navbar
${LOGIN_NAV_BUTTON}         id=login2
${LOGOUT_NAV_BUTTON}        id=logout2
${WELCOME_MESSAGE}          id=nameofuser
${CART_NAV_BUTTON}          id=cartur

# Login modal
${LOGIN_MODAL}              id=logInModal
${LOGIN_USERNAME_FIELD}     id=loginusername
${LOGIN_PASSWORD_FIELD}     id=loginpassword
${LOGIN_SUBMIT_BUTTON}      xpath=//div[@id='logInModal']//button[text()='Log in']

# Catalog
${MONITORS_CATEGORY}        xpath=//a[@id='itemc'][text()='Monitors']
${PRODUCT_TITLES}           css:#tbodyid .card-title a
${PRODUCT_PRICES}           css:#tbodyid .card-block h5
${FIRST_PRODUCT_TITLE}      xpath=(//div[@id='tbodyid']//h4[@class='card-title']/a)[1]

# Product page
${PRODUCT_PAGE_NAME}        css:h2.name
${PRODUCT_PAGE_PRICE}       css:h3.price-container
${ADD_TO_CART_BUTTON}       xpath=//a[text()='Add to cart']
