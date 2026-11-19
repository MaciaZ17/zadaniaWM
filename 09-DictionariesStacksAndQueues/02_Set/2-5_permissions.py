###
# Checks whether the user has the required permissions
#
required_permissions = {"read", "write", "execute"}                 # uprawnienia potrzebne do akcji
user_permissions = {"read", "write"}                                # uprawnienia użytkownika

has_permissions = required_permissions.issubset(user_permissions)   # issubset() sprawdza, czy każde wymagane uprawnienie użytkownik ma
print(has_permissions)                                              # False, bo brakuje "execute"
