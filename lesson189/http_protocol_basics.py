# HTTP Protocol Basics (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) is a protocol used to send and receive
# data over the Internet. It operates using a client/server model, where a client
# (such as your web browser) makes a request to the server (e.g., a website),
# and the server responds with appropriate data.
#
# A client's HTTP request message typically includes data like:
# - HTTP method
#     - safe methods (read-only): GET, HEAD (headers only), OPTIONS (supported methods)
#     - write methods: POST, PUT (replace resource), PATCH (update partially), DELETE
# - The resource's URL or path being accessed (e.g., /users/)
# - HTTP headers (e.g., Content-Type, Authorization)
# - The request body (when necessary, depending on the HTTP method)
#
# The server's HTTP response message typically includes data such as:
# - HTTP status code (e.g., 200 OK, 404 Not Found, 301 Moved Permanently)
#   https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - HTTP headers (e.g., Content-Type, Accept)
# - The response body (may be empty in some cases)
