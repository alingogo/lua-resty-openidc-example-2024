local opts = {
    ssl_verify = "no",
    redirect_uri = "http://localhost/cb",
    discovery = "http://keycloak:8080/realms/demo/.well-known/openid-configuration",
    client_id = "sample-app",
    client_secret = "d59cc875-2546-4bc6-81a9-f34ceb82f662"
}

local res, err, a, session = require("resty.openidc").authenticate(opts)
if err then
    ngx.log(ngx.ERR, err)
    ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
end
ngx.req.set_header("X-USER", res.id_token.sub)

local jwt = require "resty.jwt"
local jwt_token = jwt:sign(
    "secret_key_200a9737bfc6d55b37085f0589f",
    {
        header={typ="JWT", alg="HS256"},
        payload=res.user
    }
)
ngx.log(ngx.INFO, "user info: " .. tostring(res.user))
ngx.log(ngx.INFO, "jwt: " .. tostring(jwt_token))
ngx.req.set_header("X-OIDC-TOKEN", jwt_token)

ngx.var.pass="http://fastapi:3000/"

-- ngx.log(ngx.INFO, "---------------------------------------------")
-- ngx.log(ngx.INFO,  tostring(session:get("enc_id_token")))
-- ngx.log(ngx.INFO, "body: " .. ngx.body)
-- ngx.log(ngx.INFO, "jwt: " .. ngx.req.read_body.client_assertion)
-- ngx.req.set_header("X-OIDC-TOKEN", tostring(session:get("enc_id_token")))
-- ngx.req.set_header("X-OIDC-TOKEN", tostring(session:get("access_token")))
-- ngx.var.pass="http://webapp:3000/"