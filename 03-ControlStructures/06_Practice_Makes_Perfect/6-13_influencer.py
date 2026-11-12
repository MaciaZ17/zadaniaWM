###
# Dobry influencer ma co najmniej dwa z trzech kont: Facebook, Twitter, Instagram.
#
facebook = True                                              # czy ma konto na Facebooku
twitter = False                                              # czy ma konto na Twitterze
instagram = True                                             # czy ma konto na Instagramie
accounts = 0                                                 # licznik kont
if facebook:                                                 # jeśli ma Facebooka
    accounts += 1                                            # zwiększamy licznik
if twitter:                                                  # jeśli ma Twittera
    accounts += 1                                            # zwiększamy licznik
if instagram:                                                # jeśli ma Instagram
    accounts += 1                                            # zwiększamy licznik
print(f'facebook = {facebook}')                              # wypisujemy dane wejściowe
print(f'twitter = {twitter}')                                # j.w.
print(f'instagram = {instagram}')                            # j.w.
if accounts >= 2:                                            # co najmniej dwa konta
    print('You are a good influencer!')                      # dobry influencer
else:                                                        # mniej niż dwa
    print('You are not a good influencer yet')               # jeszcze nie
