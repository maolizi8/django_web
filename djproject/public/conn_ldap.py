'''
Created on 2019年7月26日

@author: geqiuli
'''
from ldap3 import Server, Connection, ALL, SUBTREE, ServerPool,ALL_ATTRIBUTES

LDAP_SERVER_POOL = ["xx.xx.xx.xx"]
LDAP_SERVER_PORT = 389
# if the connection need authentication:
ADMIN_DN = "username for auth-connection, provided from IT"
ADMIN_PASSWORD = "password for auth-connection, provided from IT"

SEARCH_BASE = "dc=example,dc=com" # 域，根据实际情况填写，如果需要指定部门，则添加：OU=部门名称,dc=example,dc=com


def ldap_auth(username, password):
    ldap_server_pool = ServerPool(LDAP_SERVER_POOL)
    conn = Connection(ldap_server_pool, user=ADMIN_DN, password=ADMIN_PASSWORD, check_names=True, lazy=False, raise_exceptions=False)
    conn.open()
    r=conn.bind()
    print('bind:',r)
    
    # 默认uid，但是未必能匹配到，可尝试：sAMAccountName
    res = conn.search(
        search_base = SEARCH_BASE,
        search_filter = '(sAMAccountName={})'.format(username),
        search_scope = SUBTREE,
        #attributes = ['cn', 'givenName', 'mail', 'sAMAccountName'],
        #ALL_ATTRIBUTES：获取所有属性值
        attributes=ALL_ATTRIBUTES,
        paged_size = 5
    )
    print('res: ',res)

    if res:
        entry = conn.response[0]
        # print(entry)
        dn = entry['dn']
        attr_dict = entry['attributes']

        # check password by dn
        try:
            conn2 = Connection(ldap_server_pool, user=dn, password=password, check_names=True, lazy=False, raise_exceptions=False)
            conn2.bind()
            if conn2.result["description"] == "success":
                print(attr_dict)
                #根据打印出的实际信息，可知道所需要的映射的字段名
                print((True,attr_dict["sAMAccountName"],password, attr_dict["mail"], attr_dict["cn"],attr_dict["department"], attr_dict["givenName"]))
                return (True, attr_dict["sAMAccountName"],password, attr_dict["mail"],attr_dict["cn"],attr_dict["department"],attr_dict["givenName"])
            else:
                print("auth fail")
                return (False, None, None, None)
        except Exception as e:
            print("auth fail")
            return (False, None, None, None)
    else:
        return (False, None, None, None)


if __name__ == "__main__":
    ldap_auth("xxxxx", "xxxxx")