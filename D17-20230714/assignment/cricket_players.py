# cricket_players=[{"name":"M S Dhoni","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":1,"hat trick wickets":0,"Top batting score":224},
#                  {"name":"AB Devilliers","No.of.Centuries":72,"No.of.Half centuries":169,"Wickets taken":11,"hat trick wickets":0,"Top batting score":278},
#                  {"name":"Andre Russel","No.of.Centuries":76,"No.of.Half centuries":108,"Wickets taken":557,"hat trick wickets":7,"Top batting score":132},
#                  {"name":"David Warner","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":10,"hat trick wickets":8,"Top batting score":335},
#                  {"name":"Devon Conway","No.of.Centuries":29,"No.of.Half centuries":61,"Wickets taken":0,"hat trick wickets":6,"Top batting score":327}]

# def player_statistics(cricket_players):
#     print("PLAYERS WITH MORE THAN 10 CENTURIES\n")
    
#     for player in cricket_players:
        

#         name=player["name"]
#         centuries=player["No.of.Centuries"]
       
#         if player["No.of.Centuries"] > 10:
#             print(f"{name}\n{centuries}")
    
#     print("/nPLAYERS WITH MOST HAT TRICK WICKETS/n")
    
#     for player in cricket_players:
#          hat_tricks=player["hat trick wickets"]
#          name=player["name"]
         
#          if player["hat trick wickets"]>5:
#             print(f"{name}\n{hat_tricks}")
    
#     print("/nTOP BATTING SCORE\n")
    
#     for player in cricket_players:
#         top_score=player["Top batting score"]
#         name=player["name"]

#         print(f"{name}\n{top_score}")        

# player_statistics(cricket_players)


cricket_players=[{"name":"M S Dhoni","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":1,"hat trick wickets":0,"Top batting scores":[123,144,156,183,224]},
                 {"name":"AB Devilliers","No.of.Centuries":72,"No.of.Half centuries":169,"Wickets taken":11,"hat trick wickets":0,"Top batting scores":[133,157,201,133,278]},
                 {"name":"Andre Russel","No.of.Centuries":76,"No.of.Half centuries":108,"Wickets taken":557,"hat trick wickets":7,"Top batting scores":[127,132,188,155,235]},
                 {"name":"David Warner","No.of.Centuries":16,"No.of.Half centuries":136,"Wickets taken":10,"hat trick wickets":8,"Top batting scores":[200,124,264,293,335]},
                 {"name":"Devon Conway","No.of.Centuries":29,"No.of.Half centuries":61,"Wickets taken":0,"hat trick wickets":6,"Top batting scores":[327,223,122,193,187]}]

def player_statistics(cricket_players):
    centuries=0
    hat_trick_wickets=[]
    top_batting_scores=[]
    sum=0
    for player in cricket_players:

        if player["No.of.Centuries"] > 10:
            centuries =centuries+1
           

        if player["hat trick wickets"] >5:
            hat_trick_wickets.append(player["name"])

        
        for top in player ["Top batting scores"]:
            if top > sum:
                sum=top
            
        top_score={"Player Name": player["name"],
                    "Top Score": sum}
        top_batting_scores.append(top_score)
    
            
    print("NO.of players scored more than 10 centuries:",centuries)
    print("Players taken than 5 hat trick wickets:",hat_trick_wickets)
    print("Top batting scores of players:\n",top_batting_scores)
     
player_statistics(cricket_players)




