
import ro_py as roblox


# x = roblox_py.JoinGame.get_roblox_auth_ticket()

# print(x)

# roblox_py.JoinGame.join_game(6852386028)
# print("test")

#177263364
# roblox_py.PlayerAuth.get_self(177263364)
# roblox_py.Client.join_game()


with roblox.RobloxSession(username="KmAQKjdizD7tja0TiQ", password="AA12ISGARBAGE378") as rbx:
     rbx.post_status("i love bricks!")  # post status
     print(rbx.friend_count())