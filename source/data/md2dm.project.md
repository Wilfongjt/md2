# project:
1. name: md2dm-api
1. issuer: lyttlebit
1. audience: md2dm-api_client
1. subject: client_api

## owner:
### api_admin:
1. id: api_admin@lyttlebit.com
1. type: ACCOUNT
1. username: api_admin@lyttlebit.com
1. displayname: J
1. password: a1A!aaaa
1. scope: api_admin

### api_guest:
1. id: api_guest@lyttlebit.com
1. type: ACCOUNT
1. username: api_guest@lyttlebit.com
1. displayname: J
1. password: a1A!aaaa
1. scope: api_guest

### api_user:
1. id: api_user@lyttlebit.com
1. type: ACCOUNT
1. username: api_user@lyttlebit.com
1. displayname: J
1. password: a1A!aaaa
1. scope: api_user

## claim:
### api_admin:
1. aud: aad-api_client
1. iss: lyttlebit
1. key: api_admin@lyttlebit.com
1. scope: api_admin
1. user: api_admin@lyttlebit.com

### api_guest:
1. aud: aad-api_client
1. iss: lyttlebit
1. key: api_guest@lyttlebit.com
1. scope: api_guest
1. user: api_guest@lyttlebit.com

### api_user:
1. aud: aad-api_client
1. iss: lyttlebit
1. key: api_user@lyttlebit.com
1. scope: api_user
1. user: api_user@lyttlebit.com

## resource:
### account:
1. resource: account
1. type: account
1. version:000

#### model:
1. id: abc#abc
1. type: ACCOUNT
1. owner: abc@xyz.abc

#### methods:
##### account_delete:
1. active: 1
1. name: account_delete
1. scope: [api_user, api_admin, api_guest]
1. parameter: [token_id=TOKEN, owner_id=OWNERID, primary_key=PRIMARYKEY]

##### account_get:
1. active: 1
1. name: account_get
1. scope: [api_user, api_admin, api_guest]
1. parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY]

##### account_post:
1. active: 1
1. name: account_post
1. scope: [api_user, api_admin, api_guest]
1. parameter: [token_id=TOKEN,owner_id=OWNERID,trip=TRIPLE]

##### account_put:
1. active: 1
1. name: account_put
1. scope: [api_user, api_admin, api_guest]
1. parameter: [token_id=TOKEN,owner_id=OWNERID,primary_key=PRIMARYKEY,trip=TRIPLE]

