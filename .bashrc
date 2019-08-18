export OIDC_RP_SIGN_ALGO=RS256

export OIDC_OP_JWKS_ENDPOINT=http://localhost:8080/auth/realms/citizensso/protocol/openid-connect/certs
export client_id=citizen
export client_secret=

export auth_uri=http://localhost:8080/auth/realms/citizensso/protocol/openid-connect/auth
export OIDC_OP_TOKEN_ENDPOINT=http://localhost:8080/auth/realms/citizensso/protocol/openid-connect/token

export OIDC_OP_USER_ENDPOINT=http://localhost:8080/auth/realms/citizensso/protocol/openid-connect/userinfo
export LOGIN_URL=http://localhost:8080/auth/realms/citizensso/protocol/openid-connect/auth

export LOGIN_REDIRECT_URL=http://localhost:8001/profile/

./manage.py runserver localhost:8001
