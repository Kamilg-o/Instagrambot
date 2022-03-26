import classes

user=classes.Uzytkownik()
user.log_in()
user.autorisation()
user.searching()
user.action()
for i in range(4):
    user.next_pic()
    user.liked()