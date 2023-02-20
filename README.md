
DESCRIPTION: The Menu and Reservations API provides information about menu items and reservations made

ENDPOINTS INFORMATION:

Base url: http://127.0.0.1:8000/

ON ALL ENDPOINTS YOU MUST PROVIDE AN AUTHENTICATION  TOKEN

USERS

GET /auth/users/ : Gets a list of all users.

GET /auth/users/me: Gets the information of the currently authenticated user.

POST /auth/token/login: Gets an authentication token. You must send a valid username and password.

MENU-ITEMS

GET /restaurant/menu-items: Gets a list of all menu items

POST /restaurant/menu-items: Add a new menu-item


Parameters

-id(required, int):Unique menu-item identifier

GET /restaurant/menu-items/{id}: Get details of a specific menu-item

PUT /restaurant/menu-items/{id}: Completely update a specific menu-item 

PATCH /restaurant/menu-items/{id}: Partially update a specific menu-item 

DELETE /restaurant/menu-items/{id}: Remove a specific menu-item 

BOOKINGS

GET /restaurant/bookings: Gets a list of all bookings

POST /restaurant/bookings: Add a new booking

Parameters

-id(required, int):Unique booking identifier

NOTE: Please put / at the end of each endpoint if it gives an error

GET /restaurant/bookings/{id}: Get details of a specific booking

PUT /restaurant/bookings/{id}: Completely update a specific booking

PATCH /restaurant/bookings/{id}: Partially update a specific booking

DELETE /restaurant/bookings/{id}: Remove a specific booking