import argparse

# Create the parser
my_parser = argparse.ArgumentParser()

# Path to the .xlsx of bot passwords and usernames
my_parser.add_argument('Path',metavar='path',type=str,help='the path to list')
# url for leader account
my_parser.add_argument('LeaderURL',metavar='LeaderURL',type=str,help='the url for the leader account')
# The number of bot that will run
my_parser.add_argument('NumOfBots',metavar='NumOfBots',type=int,help='the num of bots to run')

# Execute the parse_args() method
args = my_parser.parse_args()

print(args.Path)
print(args.LeaderURL)
print(args.NumOfBots)



print("ran by c#. Yay!")