json = require "/usr/local/openresty/json"

local opts = {
    ssl_verify = "no",
    redirect_uri = "http://localhost/cb",
    discovery = "http://keycloak:8080/realms/demo/.well-known/openid-configuration",
    client_id = "sample-app",
    client_secret = "d59cc875-2546-4bc6-81a9-f34ceb82f662"
}

local res, err = require("resty.openidc").authenticate(opts) --P1505
if err then
    ngx.log(ngx.ERR, err)
    ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
end

ngx.log(ngx.ERR, res.access_token)

-- local res2, err2 = require("resty.openidc").call_userinfo_endpoint(opts, res.access_token) --P606
-- local res2, err2 = require("resty.openidc").openidc_authorization_response(opts, res.session)
-- if err2 then
--     ngx.log(ngx.ERR, err2)
--     ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
-- end

local user = res.user
if user then
    for key, val in pairs(user) do
        ngx.log(ngx.ERR, key)
        ngx.log(ngx.ERR, val)
     end
end

ngx.req.set_header("X-USER", res.id_token.sub)
ngx.req.set_header("X-USERINFO", json.encode(user))

ngx.var.pass="http://webapp:3000/"